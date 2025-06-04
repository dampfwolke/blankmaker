import sys
import pathlib
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6.QtWidgets import QMessageBox # Wichtig für Pop-up-Nachrichten

# Deine bestehenden Imports
from utils.zeitstempel import zeitstempel
from utils.kalenderwoche import kw_ermitteln
from utils.get_settings import load_settings, get_stylesheet_path, get_pfad_from_template
from utils.rechteck import rechteck_erstellen 

from UI.frm_main_window import Ui_frm_main_window
from UI.animated_tabhelper import AnimatedTabHelper

class MainWindow(qtw.QMainWindow, Ui_frm_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings = load_settings()
        self.wg_datum_editieren.setHidden(True)
        self.le_pfad.setDisabled(True) # Der Pfad wird automatisch generiert

        self.de_datum.setDate(qtc.QDate.currentDate())
        self.pfad_aktualisieren() # Initialen Pfad setzen

        self.anim_tabs = AnimatedTabHelper(self.tw_rohteil_erstellen)

        # Signale verbinden
        self.pb_rechteck.clicked.connect(self.rechteck_erstellen_clicked)
        self.le_rechteck_hoehe.editingFinished.connect(self.rechteck_erstellen_clicked) 

        self.de_datum.dateChanged.connect(self.pfad_aktualisieren)

    @qtc.Slot()
    def rechteck_erstellen_clicked(self):
        """
        Liest Werte aus den LineEdits, validiert sie und ruft die 
        rechteck_erstellen Funktion auf.
        """
        try:
            # Werte aus den LineEdits holen und in float konvertieren
            # Ersetze Komma durch Punkt für internationale Dezimaltrennzeichen
            length_str = self.le_rechteck_laenge.text().replace(',', '.')
            width_str = self.le_rechteck_breite.text().replace(',', '.')
            height_str = self.le_rechteck_hoehe.text().replace(',', '.')

            if not all([length_str, width_str, height_str]):
                QMessageBox.warning(self, "Eingabe fehlt", "Bitte füllen Sie alle Felder für Länge, Breite und Höhe aus.")
                return

            length = float(length_str)
            width = float(width_str)
            height = float(height_str)

            # Grundlegende Validierung
            if length <= 0 or width <= 0 or height <= 0:
                QMessageBox.warning(self, "Ungültige Eingabe", 
                                    "Länge, Breite und Höhe müssen positive Zahlen sein.")
                return

        except ValueError:
            QMessageBox.warning(self, "Ungültige Eingabe", 
                                "Bitte geben Sie gültige Zahlen für Länge, Breite und Höhe ein.")
            return
        
        # Pfad aus dem LineEdit 'le_pfad' holen
        # Dieser Pfad ist ein Verzeichnispfad, wir brauchen einen Dateinamen
        dir_path_str = self.le_pfad.text()
        if not dir_path_str:
            QMessageBox.warning(self, "Fehlender Pfad", 
                                "Der Zielpfad konnte nicht ermittelt werden. Bitte Datum überprüfen.")
            return

        file_name = "!rohteil.dxf" 
        full_output_path = str(pathlib.Path(dir_path_str) / file_name)
        success, message = rechteck_erstellen(length, width, height, full_output_path)

        if success:
            self.statusBar().showMessage(f"Rechteck wurde erstellt! {zeitstempel(1)}", 7000)
        else:
            QMessageBox.critical(self, "Fehler", message)
            self.statusBar().showMessage(f"Fehler: {message} ({zeitstempel(1)})", 7000)
            print(f"Fehler: {message} ({zeitstempel(1)})")


    @qtc.Slot()
    def pfad_aktualisieren(self):
        qt_date = self.de_datum.date()
        py_date = qt_date.toPython()
        kw, wochentag = kw_ermitteln(py_date)
        
        # get_pfad_from_template sollte sicherstellen, dass ein gültiger Pfadstring zurückkommt
        # oder None/Fehler, falls etwas schiefgeht.
        pfad_template_result = get_pfad_from_template(self.settings, kw, wochentag)
        
        if pfad_template_result:
            # Stelle sicher, dass pfad_template_result ein String ist.
            # Wenn es ein pathlib.Path Objekt ist, konvertiere es.
            self.le_pfad.setText(str(pfad_template_result))
        else:
            self.le_pfad.setText("") # Oder eine Fehlermeldung / Standardpfad
            self.statusBar().showMessage("Konnte Pfad nicht aus Template generieren.", 5000)
            print("[Warnung] Pfad konnte nicht aus Template generiert werden.")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    settings = load_settings()
    stylesheet_path = get_stylesheet_path(settings)

    if stylesheet_path:
        try:
            # Stelle sicher, dass stylesheet_path ein pathlib.Path Objekt ist
            if isinstance(stylesheet_path, str):
                stylesheet_path = pathlib.Path(stylesheet_path)
                
            with stylesheet_path.open("r", encoding="utf-8") as f:
                app.setStyleSheet(f.read())
            print(f"[Info] Stylesheet geladen: {stylesheet_path}")
        except Exception as e:
            print(f"[Warnung] Stylesheet konnte nicht geladen werden: {stylesheet_path} - {e}")
    else:
        print("[Info] Kein Stylesheet verwendet.")

    window = MainWindow()
    window.show()
    sys.exit(app.exec())