import sys
import shutil
import math
import subprocess
from functools import partial
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

        self.running_processes = {}
        self.process_check_timer = qtc.QTimer(self)
        self.process_check_timer.timeout.connect(self.check_running_processes)
        self.process_check_timer.start(1000)

        self.wg_datum_editieren.setHidden(True)
        self.le_pfad.setDisabled(True)
        self.fr_scripts.setHidden(True)
        self.le_at_nr.setDisabled(True)
        self.wg_fertigtielmasse.setHidden(True)
        self.wg_sleep_timer.setHidden(True)

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

        self.setup_script_buttons()

        # NEU: Signal für das Makro-Skript
        self.pb_esprit_start_makro.clicked.connect(self.on_esprit_makro_clicked)

    def setup_script_buttons(self):
        """Konfiguriert die Buttons für die langlebigen Skripte."""
        scripts_to_manage = {
            self.pb_prozess_oeffnen: ("scripts/prozess_oeffnen.py", self.get_args_for_hotkey_script),
            self.pb_error_closer: ("scripts/error_closer.py", self.get_args_for_error_closer_script),
            self.pb_auto_speichern: ("scripts/backup.py", self.get_args_for_backup_script),
        }

        for button, (script_path_str, arg_func) in scripts_to_manage.items():
            script_path = Path(script_path_str)
            button.clicked.connect(
                partial(self.toggle_script_process, button=button, script_path=script_path, arg_func=arg_func)
            )
            self.update_button_style(button, is_running=False)

    @qtc.Slot()  # NEU: Slot für das einmalige Starten des Makro-Skripts
    def on_esprit_makro_clicked(self):
        """Startet das Esprit-Start-Makro als einmaligen Prozess."""
        script_path = Path("scripts/esprit_start_makro.py")

        if not script_path.is_file():
            self.statusBar().showMessage(f"Fehler: Makro-Skript nicht gefunden: {script_path}", 7000)
            return

        try:
            # Popen startet das Skript und die GUI läuft sofort weiter (nicht-blockierend)
            command = [sys.executable, str(script_path)]
            subprocess.Popen(command)
            self.statusBar().showMessage("Esprit-Start-Makro wurde ausgeführt.", 5000)
        except Exception as e:
            self.statusBar().showMessage(f"Fehler beim Starten des Makros: {e}", 7000)
            print(f"[FEHLER] Makro-Start fehlgeschlagen: {e}")

    # ... (der Rest deines Codes bleibt unverändert) ...
    def toggle_script_process(self, button: qtw.QPushButton, script_path: Path, arg_func):
        if button in self.running_processes:
            process = self.running_processes[button]
            process.terminate()
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill()
            del self.running_processes[button]
            self.update_button_style(button, is_running=False)
            self.statusBar().showMessage(f"Skript '{script_path.name}' gestoppt.", 5000)
            return
        if not script_path.is_file():
            self.statusBar().showMessage(f"Fehler: Skript-Datei nicht gefunden: {script_path}", 7000)
            return
        args = arg_func()
        if args is None:
            return
        try:
            command = [sys.executable, str(script_path)] + args
            print(f"Starte Befehl: {' '.join(command)}")
            process = subprocess.Popen(command)
            self.running_processes[button] = process
            self.update_button_style(button, is_running=True)
            self.statusBar().showMessage(f"Skript '{script_path.name}' gestartet...", 5000)
        except Exception as e:
            self.statusBar().showMessage(f"Fehler beim Starten von '{script_path.name}': {e}", 7000)

    def get_args_for_hotkey_script(self):
        return []

    def get_args_for_error_closer_script(self):
        return []

    def get_args_for_backup_script(self):
        source_folder = self.le_pfad.text()
        if not source_folder:
            self.statusBar().showMessage("Backup-Fehler: Quell-Pfad (le_pfad) ist leer.", 7000)
            return None
        backup_folder = self.settings.get("pfad_backup")
        if not backup_folder:
            self.statusBar().showMessage("Backup-Fehler: 'pfad_backup' nicht in Einstellungen gefunden.", 7000)
            return None
        return ["--source-folder", source_folder, "--backup-folder", backup_folder]

    def initialize_ui_elements(self):
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
        text = text.replace(',', '.')
        if not text:
            self.le_spannmittel.clear()
            return
        try:
            breite_val = float(text)
            if breite_val > 0:
                gerundeter_wert = math.ceil(breite_val / 5.0) * 5
                self.le_spannmittel.setText(str(gerundeter_wert))
            else:
                self.le_spannmittel.clear()
        except ValueError:
            self.le_spannmittel.clear()

    def closeEvent(self, event: qtg.QCloseEvent):
        if self.running_processes:
            self.statusBar().showMessage("Beende laufende Skripte...", 2000)
            for process in self.running_processes.values():
                process.terminate()
            qtc.QTimer.singleShot(500, self.close)
            event.ignore()
        else:
            event.accept()

    def check_running_processes(self):
        for button, process in list(self.running_processes.items()):
            if process.poll() is not None:
                del self.running_processes[button]
                self.update_button_style(button, is_running=False)
                exit_code = process.returncode
                self.statusBar().showMessage(f"Skript für '{button.text()}' unerwartet beendet (Code: {exit_code}).",
                                             7000)

    def update_button_style(self, button: qtw.QPushButton, is_running: bool):
        if is_running:
            button.setStyleSheet("background-color: #4CAF50; color: white;")
        else:
            button.setStyleSheet("")

    @qtc.Slot()
    def execute_frm_settings(self):
        if self.frm_settings:
            self.frm_settings.close()
        self.frm_settings = Settings()
        self.statusBar().showMessage(f"Einstellungen geöffnet. ({zeitstempel(1)})", 7000)
        self.frm_settings.show()

    @qtc.Slot()
    def spannmittel_erstellen(self):
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