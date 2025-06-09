import sys
import shutil
import math
from pathlib import Path
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

from utils.zeitstempel import zeitstempel
from utils.kalenderwoche import kw_ermitteln
from utils.get_settings import load_settings, get_pfad_from_template
from utils.rechteck import rechteck_erstellen
from utils.kreis import kreis_erstellen
from utils.input_validators import validate_dimensions, validate_circle_dimensions
from utils.ui_helpers import populate_combobox_with_subfolders

from UI.frm_main_window import Ui_frm_main_window
from UI.animated_tabhelper import AnimatedTabHelper

from einstellungen import Settings


class MainWindow(qtw.QMainWindow, Ui_frm_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.frm_settings = Settings()
        self.settings = load_settings()
        self.wg_datum_editieren.setHidden(True)
        self.le_pfad.setDisabled(True)
        self.fr_scripts.setHidden(True)

        self.de_datum.setDate(qtc.QDate.currentDate())
        self.pfad_aktualisieren()
        self.anim_tabs = AnimatedTabHelper(self.tw_rohteil_erstellen)

        self.double_validator = qtg.QDoubleValidator(0.001, 99999.999, 3, self)
        self.double_validator.setNotation(qtg.QDoubleValidator.StandardNotation)
        german_locale = qtc.QLocale(qtc.QLocale.Language.German, qtc.QLocale.Country.Germany)
        self.double_validator.setLocale(german_locale)
        self.le_rechteck_laenge.setValidator(self.double_validator)
        self.le_rechteck_breite.setValidator(self.double_validator)
        self.le_rechteck_hoehe.setValidator(self.double_validator)
        self.le_durchmesser.setValidator(self.double_validator)
        self.le_z_kreis.setValidator(self.double_validator)
        self.le_spannmittel.setValidator(qtg.QIntValidator(1, 999, self))

        self.initialize_ui_elements()

        # Signale verbinden
        self.actionEinstellungen.triggered.connect(self.execute_frm_settings)
        self.pb_rechteck.clicked.connect(self.rechteck_erstellen_clicked)
        self.le_rechteck_hoehe.editingFinished.connect(self.rechteck_erstellen_clicked)
        self.pb_kreis.clicked.connect(self.kreis_erstellen_clicked)
        self.le_z_kreis.editingFinished.connect(self.kreis_erstellen_clicked)
        self.de_datum.dateChanged.connect(self.pfad_aktualisieren)
        self.pb_spannmittel.clicked.connect(self.spannmittel_erstellen)
        self.le_rechteck_breite.textChanged.connect(self.update_spannmittel_from_breite)

    def initialize_ui_elements(self):
        """Initialisiert UI-Elemente, die Daten aus den Settings benötigen."""
        populate_combobox_with_subfolders(
            combobox=self.cb_spannmittel,
            settings=self.settings,
            settings_key="spannmittel_basis_pfad",
            status_bar=self.statusBar()
        )
        if self.cb_spannmittel.count() > 0:
            self.cb_spannmittel.setCurrentIndex(0)

    @qtc.Slot(str)
    def update_spannmittel_from_breite(self, text: str):
        """
        Aktualisiert das le_spannmittel basierend auf dem Wert in le_rechteck_breite.
        Rundet den Wert auf den nächsten 5er-Schritt auf.
        """
        # Ersetze Komma durch Punkt für die Konvertierung
        text = text.replace(',', '.')

        if not text:
            self.le_spannmittel.clear()
            return

        try:
            breite_val = float(text)
            if breite_val > 0:
                # Auf den nächsten 5er-Schritt aufrunden
                # math.ceil(x) rundet x auf die nächste ganze Zahl auf.
                # z.B. 143.78 / 5 = 28.756 -> ceil -> 29. Dann 29 * 5 = 145.
                gerundeter_wert = math.ceil(breite_val / 5.0) * 5
                self.le_spannmittel.setText(str(gerundeter_wert))
            else:
                self.le_spannmittel.clear()
        except ValueError:
            # Wenn der Text keine gültige Zahl ist (z.B. während der Eingabe),
            # passiert nichts oder das Feld wird geleert.
            self.le_spannmittel.clear()

    @qtc.Slot()
    def execute_frm_settings(self):
        if self.frm_settings:
            self.frm_settings.close()
        self.frm_settings = Settings()
        self.statusBar().showMessage(f"Einstellungen geöffnet. ({zeitstempel(1)})", 7000)
        self.frm_settings.show()

    @qtc.Slot()
    def spannmittel_erstellen(self):
        """Kopiert eine ausgewählte Spannmittel-Datei in den Zielordner."""
        spannmittel_typ = self.cb_spannmittel.currentText()
        if not spannmittel_typ or "Fehler" in spannmittel_typ or "Keine" in spannmittel_typ:
            self.statusBar().showMessage("Fehler: Bitte gültiges Spannmittel aus der Liste wählen.", 7000)
            return

        spannmittel_groesse = self.le_spannmittel.text()
        if not spannmittel_groesse:
            self.statusBar().showMessage("Fehler: Bitte eine Spannmittel-Größe (z.B. 50) angeben.", 7000)
            return

        ziel_ordner_str = self.le_pfad.text()
        if not ziel_ordner_str:
            self.statusBar().showMessage("Fehler: Zielpfad konnte nicht ermittelt werden.", 7000)
            return

        spannmittel_basis_pfad_str = self.settings.get("spannmittel_basis_pfad")
        if not spannmittel_basis_pfad_str:
            self.statusBar().showMessage("Fehler: 'spannmittel_basis_pfad' nicht in Einstellungen gefunden.", 7000)
            return

        quell_ordner = Path(spannmittel_basis_pfad_str) / spannmittel_typ
        quell_datei = quell_ordner / f"{spannmittel_groesse}.step"

        ziel_ordner = Path(ziel_ordner_str)
        ziel_datei = ziel_ordner / f"!schraubstock{quell_datei.suffix}"

        try:
            if not quell_datei.exists():
                self.statusBar().showMessage(f"Fehler: Quelldatei nicht gefunden: {quell_datei.name}", 7000)
                print(f"[FEHLER] Quelldatei nicht gefunden: {quell_datei}")
                return

            ziel_ordner.mkdir(parents=True, exist_ok=True)
            shutil.copy2(quell_datei, ziel_datei)

            self.statusBar().showMessage(f"Spannmittel '{ziel_datei.name}' erfolgreich erstellt. ({zeitstempel(1)})",
                                         7000)
            print(f"[INFO] Spannmittel kopiert: '{quell_datei}' -> '{ziel_datei}'")

        except PermissionError:
            self.statusBar().showMessage("Fehler: Keine Berechtigung zum Schreiben im Zielordner.", 7000)
            print(f"[FEHLER] Keine Berechtigung für Pfad: {ziel_ordner}")
        except Exception as e:
            self.statusBar().showMessage(f"Ein unerwarteter Fehler ist aufgetreten: {e}", 7000)
            print(f"[FEHLER] Beim Kopieren des Spannmittels: {e}")

    @qtc.Slot()
    def rechteck_erstellen_clicked(self):
        length_str = self.le_rechteck_laenge.text()
        width_str = self.le_rechteck_breite.text()
        height_str = self.le_rechteck_hoehe.text()
        is_valid, length, width, height, error_message = validate_dimensions(length_str, width_str, height_str)
        if not is_valid:
            self.statusBar().showMessage(f"Rechteck Fehler: {error_message} ({zeitstempel(1)})", 7000)
            return

        dir_path_str = self.le_pfad.text()
        if not dir_path_str:
            self.statusBar().showMessage(f"'Fehler beim Erstellen von !rohteil.dxf'. ({zeitstempel(1)})", 7000)
            return

        file_name = "!rohteil.dxf"
        full_output_path = str(Path(dir_path_str) / file_name)

        self.statusBar().showMessage(f"Erstelle Rechteck-DXF: {file_name}...", 3000)
        success, message_from_module = rechteck_erstellen(length, width, height, full_output_path)

        if success:
            self.statusBar().showMessage(f"Rechteck erstellt ({zeitstempel(1)})", 7000)
            self.spannmittel_erstellen()
        else:
            self.statusBar().showMessage(f"Rechteck Fehler DXF: {message_from_module} ({zeitstempel(1)})", 7000)

    @qtc.Slot()
    def kreis_erstellen_clicked(self):
        diameter_str = self.le_durchmesser.text()
        height_str = self.le_z_kreis.text()
        is_valid, diameter, height, error_message = validate_circle_dimensions(diameter_str, height_str)
        if not is_valid:
            self.statusBar().showMessage(f"Kreis Fehler: {error_message} ({zeitstempel(1)})", 7000)
            return

        dir_path_str = self.le_pfad.text()
        if not dir_path_str:
            self.statusBar().showMessage(f"Fehler beim Erstellen von '!rohteil.dxf'. ({zeitstempel(1)})", 7000)
            return

        file_name = "!rohteil.dxf"
        full_output_path = str(Path(dir_path_str) / file_name)

        self.statusBar().showMessage(f"Erstelle Kreis-DXF: {file_name}...", 3000)
        success, message_from_module = kreis_erstellen(diameter, height, full_output_path)

        if success:
            self.statusBar().showMessage(f"Kreis erstellt ({zeitstempel(1)})", 7000)
        else:
            self.statusBar().showMessage(f"Kreis Fehler DXF: {message_from_module} ({zeitstempel(1)})", 7000)

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
            self.statusBar().showMessage("Warnung: Pfad konnte nicht generiert werden.", 5000)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    settings = load_settings()

    style_filename = settings.get("styles")

    if style_filename:
        script_dir = Path(__file__).resolve().parent
        styles_folder = script_dir / "UI" / "Styles"
        full_stylesheet_path = styles_folder / style_filename

        if full_stylesheet_path.is_file():
            try:
                with full_stylesheet_path.open("r", encoding="utf-8") as f:
                    app.setStyleSheet(f.read())
                print(f"[Info] Stylesheet geladen: {full_stylesheet_path}")
            except Exception as e:
                print(f"[Warnung] Stylesheet konnte nicht geladen werden: {full_stylesheet_path} - {e}")
        else:
            print(f"[Warnung] Stylesheet-Datei nicht gefunden unter: {full_stylesheet_path}")
    else:
        print("[Info] Kein Stylesheet in den Einstellungen ('styles') angegeben.")

    window = MainWindow()
    window.show()
    sys.exit(app.exec())