import sys
import pathlib
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6.QtGui import QDoubleValidator 

from utils.zeitstempel import zeitstempel
from utils.kalenderwoche import kw_ermitteln
from utils.get_settings import load_settings, get_stylesheet_path, get_pfad_from_template
from utils.rechteck import rechteck_erstellen 
from utils.kreis import kreis_erstellen # NEU: Import für Kreis-Erstellung
from utils.input_validators import validate_dimensions, validate_circle_dimensions # NEU: validate_circle_dimensions

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

        # Universeller DoubleValidator für alle Maß-Eingaben
        # Die Genauigkeit von 9 Nachkommastellen ist sehr hoch, üblich sind 2-3 für mm.
        # Kannst du bei Bedarf anpassen. Z.B. auf 3: (0.001, 99999.999, 3, self)
        self.double_validator = QDoubleValidator(0.000000001, 99999.999999999, 9, self)
        self.double_validator.setNotation(QDoubleValidator.StandardNotation)
        german_locale = qtc.QLocale(qtc.QLocale.Language.German, qtc.QLocale.Country.Germany)
        self.double_validator.setLocale(german_locale)

        # Validatoren für Rechteck-LineEdits
        self.le_rechteck_laenge.setValidator(self.double_validator)
        self.le_rechteck_breite.setValidator(self.double_validator)
        self.le_rechteck_hoehe.setValidator(self.double_validator)

        # NEU: Validatoren für Kreis-LineEdits
        # Annahme: LineEdits heißen self.le_durchmesser und self.le_z_kreis
        self.le_durchmesser.setValidator(self.double_validator)
        self.le_z_kreis.setValidator(self.double_validator)


        # Signale verbinden
        self.pb_rechteck.clicked.connect(self.rechteck_erstellen_clicked)
        self.le_rechteck_hoehe.editingFinished.connect(self.rechteck_erstellen_clicked) 

        # NEU: Signale für Kreis verbinden
        # Annahme: Button heißt self.pb_kreis
        self.pb_kreis.clicked.connect(self.kreis_erstellen_clicked)
        self.le_z_kreis.editingFinished.connect(self.kreis_erstellen_clicked) # Optional

        self.de_datum.dateChanged.connect(self.pfad_aktualisieren)

    @qtc.Slot()
    def rechteck_erstellen_clicked(self):
        length_str = self.le_rechteck_laenge.text()
        width_str = self.le_rechteck_breite.text()
        height_str = self.le_rechteck_hoehe.text()

        is_valid, length, width, height, error_message = validate_dimensions(
            length_str, width_str, height_str
        )

        if not is_valid:
            self.statusBar().showMessage(f"Rechteck Fehler: {error_message} ({zeitstempel(1)})", 7000)
            print(f"[VALIDIERUNG RECHTECK] Fehler: {error_message}")
            return
        
        dir_path_str = self.le_pfad.text()
        if not dir_path_str:
            self.statusBar().showMessage(f"Rechteck Fehler: Zielpfad nicht ermittelt. Datum prüfen. ({zeitstempel(1)})", 7000)
            print("[PFAD RECHTECK] Fehler: Zielpfad nicht ermittelt.")
            return

        file_name = "!rohteil.dxf" # Eindeutiger Name für Rechteck
        full_output_path = str(pathlib.Path(dir_path_str) / file_name)
        
        self.statusBar().showMessage(f"Erstelle Rechteck-DXF: {file_name}...", 3000)
        
        success, message_from_module = rechteck_erstellen(length, width, height, full_output_path)

        if success:
            self.statusBar().showMessage(f"Rechteck wurde erstellt! {zeitstempel(1)}", 7000)
            print(f"[DXF RECHTECK] {message_from_module}")
        else:
            self.statusBar().showMessage(f"Rechteck Fehler DXF: {message_from_module} ({zeitstempel(1)})", 7000)
            print(f"[DXF RECHTECK] Fehler: {message_from_module}")

    # NEU: Slot für Kreis-Erstellung
    @qtc.Slot()
    def kreis_erstellen_clicked(self):
        """
        Liest Werte aus den LineEdits für Kreis, validiert sie und ruft die 
        kreis_erstellen Funktion auf. Rückmeldungen über Statusleiste.
        """
        diameter_str = self.le_durchmesser.text()
        height_str = self.le_z_kreis.text() # Annahme: 'le_z_kreis' ist für die Höhe

        # Eingaben mit dem ausgelagerten Validator prüfen
        is_valid, diameter, height, error_message = validate_circle_dimensions(
            diameter_str, height_str
        )

        if not is_valid:
            self.statusBar().showMessage(f"Kreis Fehler: {error_message} ({zeitstempel(1)})", 7000)
            print(f"[VALIDIERUNG KREIS] Fehler: {error_message}")
            return
        
        # Pfad aus dem LineEdit 'le_pfad' holen (gemeinsam für alle Rohteile)
        dir_path_str = self.le_pfad.text()
        if not dir_path_str:
            self.statusBar().showMessage(f"Kreis Fehler: Zielpfad nicht ermittelt. Datum prüfen. ({zeitstempel(1)})", 7000)
            print("[PFAD KREIS] Fehler: Zielpfad nicht ermittelt.")
            return

        file_name = "!rohteil.dxf" # Eindeutiger Name für Kreis
        full_output_path = str(pathlib.Path(dir_path_str) / file_name)
        
        self.statusBar().showMessage(f"Erstelle Kreis-DXF: {file_name}...", 3000)
        
        # Die Funktion kreis_erstellen gibt (success_bool, message_str) zurück
        # Der Parameter base_offset_factor wird mit dem Default-Wert aus der Funktion verwendet
        success, message_from_module = kreis_erstellen(diameter, height, full_output_path)

        if success:
            self.statusBar().showMessage(f"Kreis wurde erstellt! {zeitstempel(1)}", 7000)
            print(f"[DXF KREIS] {message_from_module}")
        else:
            self.statusBar().showMessage(f"Kreis Fehler DXF: {message_from_module} {zeitstempel(1)}", 7000)
            print(f"[DXF KREIS] Fehler: {message_from_module}")


    @qtc.Slot()
    def pfad_aktualisieren(self):
        qt_date = self.de_datum.date()
        py_date = qt_date.toPython()
        kw, wochentag = kw_ermitteln(py_date)
        
        pfad_template_result = get_pfad_from_template(self.settings, kw, wochentag)
        
        if pfad_template_result:
            self.le_pfad.setText(str(pfad_template_result))
        else:
            self.le_pfad.setText("")
            self.statusBar().showMessage("Warnung: Pfad konnte nicht aus Template generiert werden.", 5000)
            print("[Warnung] Pfad konnte nicht aus Template generiert werden.")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    settings = load_settings()
    stylesheet_path = get_stylesheet_path(settings)

    if stylesheet_path:
        try:
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