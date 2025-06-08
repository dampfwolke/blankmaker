import sys
import json
from pathlib import Path

from PySide6 import QtWidgets as qtw
from PySide6.QtWidgets import QFileDialog
from UI.frm_settings import Ui_frm_settings


class Settings(qtw.QWidget, Ui_frm_settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.json_path = Path("settings/einstellungen.json")
        self.styles_laden()
        self.lb_pfad_template.setHidden(True)
        self.le_pfad_template.setHidden(True)

        # Button-Events
        self.pb_laden.clicked.connect(self.einstellungen_laden_dialog)
        self.pb_speichern.clicked.connect(self.einstellungen_speichern)

        # Automatisch laden beim Start
        if self.json_path.exists():
            self.einstellungen_laden()

    def styles_laden(self):
        styles_path = Path("UI/Styles")
        if styles_path.exists() and styles_path.is_dir():
            for qss_file in styles_path.glob("*.qss"):
                self.cb_styles.addItem(qss_file.name)

    def einstellungen_laden(self):
        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                daten = json.load(f)

            for key, value in daten.items():
                widget = getattr(self, f"le_{key}", None)
                if widget:
                    widget.setText(str(value))

            if "styles" in daten:
                index = self.cb_styles.findText(daten["styles"])
                if index >= 0:
                    self.cb_styles.setCurrentIndex(index)
        except Exception as e:
            print("Fehler beim Laden der Einstellungen:", e)

    def einstellungen_laden_dialog(self):
        path, _ = QFileDialog.getOpenFileName(self, "Einstellungen laden", str(self.json_path.parent), "JSON (*.json)")
        if not path:
            return
        self.json_path = Path(path)
        self.einstellungen_laden()

    def einstellungen_speichern(self):
        daten = {}

        for attr in dir(self):
            if attr.startswith("le_"):
                feld = getattr(self, attr)
                key = attr[3:]
                daten[key] = feld.text()

        daten["styles"] = self.cb_styles.currentText()

        path, _ = QFileDialog.getSaveFileName(self, "Einstellungen speichern", str(self.json_path), "JSON (*.json)")
        if not path:
            return

        with open(path, "w", encoding="utf-8") as f:
            json.dump(daten, f, indent=2)

        self.json_path = Path(path)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = Settings()
    window.show()
    sys.exit(app.exec())
