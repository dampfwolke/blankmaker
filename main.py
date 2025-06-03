import sys
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc

from utils.zeitstempel import zeitstempel
from utils.kalenderwoche import kw_ermitteln
from utils.get_settings import load_settings, get_stylesheet_path, get_pfad_from_template

from UI.frm_main_window import Ui_frm_main_window
from UI.animated_tabhelper import AnimatedTabHelper

class MainWindow(qtw.QMainWindow, Ui_frm_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings = load_settings()
        self.wg_datum_editieren.setHidden(True)
        self.le_pfad.setDisabled(True)

        self.de_datum.setDate(qtc.QDate.currentDate())
        self.pfad_aktualisieren()

        self.anim_tabs = AnimatedTabHelper(self.tw_rohteil_erstellen)

        self.pb_rechteck.clicked.connect(self.rechteck_erstellen)
        self.le_rechteck_hoehe.editingFinished.connect(self.rechteck_erstellen)

        self.de_datum.dateChanged.connect(self.pfad_aktualisieren)

    @qtc.Slot()
    def rechteck_erstellen(self) -> None:
        self.statusBar().showMessage(f"Rechteck wurde erstellt. {zeitstempel(1)}", 5000)
        print(f"Rechteck wurde erstellt! {zeitstempel(1)}")

    @qtc.Slot()
    def pfad_aktualisieren(self):
        qt_date = self.de_datum.date()
        py_date = qt_date.toPython()
        kw, wochentag = kw_ermitteln(py_date)
        pfad = get_pfad_from_template(self.settings, kw, wochentag)
        self.le_pfad.setText(pfad)

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    settings = load_settings()
    stylesheet_path = get_stylesheet_path(settings)

    if stylesheet_path:
        try:
            with stylesheet_path.open("r", encoding="utf-8") as f:
                app.setStyleSheet(f.read())
            print(f"[Info] Stylesheet geladen: {stylesheet_path}")
        except Exception as e:
            print(f"[Warnung] Stylesheet konnte nicht geladen werden: {e}")
    else:
        print("[Info] Kein Stylesheet verwendet.")

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
