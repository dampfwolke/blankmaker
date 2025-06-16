import sys
import shutil
import math
import subprocess
from functools import partial
from pathlib import Path
import time

from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

# Lokale Imports
from utils.zeitstempel import zeitstempel
from utils.kalenderwoche import kw_ermitteln
from utils.get_settings import load_settings, get_pfad_from_template
from utils.rechteck import rechteck_erstellen
from utils.kreis import kreis_erstellen
from utils.input_validators import validate_dimensions, validate_circle_dimensions, calculate_spanntiefe
from utils.ui_helpers import populate_combobox_with_subfolders
from utils.autoesprit_a import EspritA
from utils.autoesprit_b import EspritB
from utils.stats_to_csv import laufzeit_eintragen
from utils.confirmation_dialog import ConfirmationDialog

# UI Imports
from UI.frm_main_window import Ui_frm_main_window
from UI.animated_tabhelper import AnimatedTabHelper
from einstellungen import Settings


class MainWindow(qtw.QMainWindow, Ui_frm_main_window):
    # --- Python Commander Konstanten ---
    NC_BASE_PATH = Path("K:/NC-PGM")
    MACHINES = ["HERMLE-C40", "HERMLE-C400", "DMU-EVO60", "DMU-100EVO", "DMC650V", "DMC1035V"]

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.frm_settings = Settings()
        self.settings = load_settings()

        # Zeitmessung
        self.startzeit = None
        self.endzeit = None

        # threads Initialisierung (zum Aufräumen später)
        self.wizard_thread = None
        self.wizard_worker = None

        # --- UI-Initialisierung ---
        self.running_processes = {}
        self.process_check_timer = qtc.QTimer(self)
        self.process_check_timer.timeout.connect(self.check_running_processes)
        self.process_check_timer.start(1000)
        self.wg_datum_editieren.setHidden(True)
        self.le_pfad.setDisabled(True)
        self.fr_scripts.setHidden(True)
        self.wg_fertigtielmasse.setHidden(True)
        self.wg_sleep_timer.setHidden(True)
        self.cbx_at_nr_editieren.setChecked(True)
        self.de_datum.setDate(qtc.QDate.currentDate())
        self.pfad_aktualisieren()
        self.anim_tabs = AnimatedTabHelper(self.tw_rohteil_erstellen)

        # --- Einrichten der Validatoren ---
        self.double_validator = qtg.QDoubleValidator(0.001, 99999.999, 3, self)
        self.double_validator.setNotation(qtg.QDoubleValidator.StandardNotation)
        german_locale = qtc.QLocale(qtc.QLocale.Language.German, qtc.QLocale.Country.Germany)
        self.double_validator.setLocale(german_locale)
        self.le_rechteck_laenge.setValidator(self.double_validator)
        self.le_rechteck_breite.setValidator(self.double_validator)
        self.le_rechteck_hoehe.setValidator(self.double_validator)
        self.le_durchmesser.setValidator(self.double_validator)
        self.le_z_kreis.setValidator(self.double_validator)
        self.le_x_fertig.setValidator(self.double_validator)
        self.le_y_fertig.setValidator(self.double_validator)
        self.le_z_fertig.setValidator(self.double_validator)
        self.le_spannmittel.setValidator(qtg.QIntValidator(1, 999, self))
        self.le_spanntiefe_b.setValidator(qtg.QIntValidator(2, 99, self))

        self.initialize_ui_elements()

        # --- Signale verbinden ---
        self.actionEinstellungen.triggered.connect(self.execute_frm_settings)
        self.pb_rechteck.clicked.connect(self.rechteck_erstellen_clicked)
        self.le_rechteck_hoehe.editingFinished.connect(self.rechteck_erstellen_clicked)
        self.pb_kreis.clicked.connect(self.kreis_erstellen_clicked)
        self.le_z_kreis.editingFinished.connect(self.kreis_erstellen_clicked)
        self.de_datum.dateChanged.connect(self.pfad_aktualisieren)
        self.pb_spannmittel.clicked.connect(self.spannmittel_erstellen)
        self.le_rechteck_breite.textChanged.connect(self.update_spannmittel_from_breite)
        self.le_z_fertig.textChanged.connect(self.update_spanntiefe_from_z_fertig)
        self.setup_script_buttons()
        self.pb_esprit_start_makro.clicked.connect(self.on_esprit_makro_clicked)
        self.pb_wizard_a.clicked.connect(self.on_wizard_a_clicked)
        self.pb_wizard_b.clicked.connect(self.on_wizard_b_clicked)

        # --- Python Commander Setup ---
        self.le_at_nr.setDisabled(False)
        projekt_prefix = self.settings.get("projekt_prefix", "").replace("AT-", "")
        self.le_at_nr.setText(projekt_prefix)
        self.pb_rausspielen.clicked.connect(self.on_rausspielen_clicked)

        # Timer für die Programmsuche
        self.nc_file_check_timer = qtc.QTimer(self)
        self.nc_file_check_timer.timeout.connect(self.update_nc_file_count)
        self.nc_file_check_timer.start(2000)
        self.update_nc_file_count()

    @qtc.Slot()
    def on_wizard_a_clicked(self):
        """Sammelt Daten für den A-Seiten-Wizard und startet ihn."""
        pgm_name = self.le_zeichnungsnr.text()
        typ = self.cb_auto_option_a.currentText()

        x_roh = self.le_rechteck_laenge.text()
        y_roh = self.le_rechteck_breite.text()
        z_roh = self.le_rechteck_hoehe.text()
        bearbeitung = self.cb_bearbeitung_auswahl.currentText()

        if not all([x_roh, y_roh, z_roh]) and typ != "Bounding Box auslesen":
            self.statusBar().showMessage("Fehler: Bitte Rohteilmaße für A-Seite sicherstellen.", 7000)
            return

        worker_args = {
            "pgm_name": pgm_name,
            "x_roh": x_roh,
            "y_roh": y_roh,
            "z_roh": z_roh,
            "bearbeitung_auswahl": bearbeitung,
            "typ": typ}

        self.start_wizard(worker_class=EspritA, worker_args=worker_args, description="A-Seite")

    @qtc.Slot()
    def on_wizard_b_clicked(self):
        """Sammelt Daten für den B-Seiten-Wizard und startet ihn."""
        pgm_name = self.le_zeichnungsnr.text()
        typ = self.cb_auto_option_b.currentText()
        x_fertig = self.le_x_fertig.text()
        y_fertig = self.le_y_fertig.text()
        z_fertig = self.le_z_fertig.text()
        spanntiefe = self.le_spanntiefe_b.text()

        worker_args = {
            "pgm_name": pgm_name,
            "typ": typ,
            "x_fertig": x_fertig,
            "y_fertig": y_fertig,
            "z_fertig": z_fertig,
            "spanntiefe": spanntiefe
        }
        self.start_wizard(worker_class=EspritB, worker_args=worker_args, description="B-Seite")

    def start_wizard(self, worker_class, worker_args: dict, description: str):
        """
        Eine zentrale Methode zum Starten von JEDEM Wizard-Typ (A, B, etc.).
        """
        if self.wizard_thread and self.wizard_thread.isRunning():
            self.statusBar().showMessage("Ein Automatisierungs-Prozess läuft bereits.", 5000)
            return

        pfad = self._get_and_validate_target_dir()
        if not pfad: return
        sleep_timer = self.hsl_sleep_timer.value()

        worker_args["pfad"] = pfad
        worker_args["sleep_timer"] = sleep_timer

        self.wizard_thread = qtc.QThread()
        self.wizard_worker = worker_class(**worker_args)
        self.wizard_worker.moveToThread(self.wizard_thread)

        # Standardsignale verbinden
        self.wizard_thread.started.connect(self.wizard_worker.run)
        self.wizard_worker.finished.connect(self.on_wizard_finished)
        self.wizard_worker.status_update.connect(self.statusBar().showMessage)
        self.wizard_worker.show_info_dialog.connect(self.display_worker_message)

        # Spezifische Signale verbinden (robust durch hasattr)
        if hasattr(self.wizard_worker, 'ausgelesene_fertig_werte'):
            self.wizard_worker.ausgelesene_fertig_werte.connect(self.fertig_abmasse_eintragen)

        # NEU: Das Signal für den Bestätigungsdialog verbinden, falls der Worker es besitzt
        if hasattr(self.wizard_worker, 'confirmation_required'):
            self.wizard_worker.confirmation_required.connect(self.show_confirmation_dialog)

        # Aufräum-Logik
        self.wizard_worker.finished.connect(self.wizard_thread.quit)
        self.wizard_thread.finished.connect(self.wizard_worker.deleteLater)
        self.wizard_thread.finished.connect(self.wizard_thread.deleteLater)
        self.wizard_thread.finished.connect(self.clear_wizard_thread_reference)

        # Thread starten und UI anpassen
        self.wizard_thread.start()
        self.pb_wizard_a.setEnabled(False)
        self.pb_wizard_b.setEnabled(False)
        self.startzeit = time.perf_counter()
        self.statusBar().showMessage(f"Automatisierung {description} gestartet...", 3000)

    # NEU: Dieser Slot wird vom Worker-Thread aufgerufen, um den Dialog anzuzeigen.
    @qtc.Slot(str, str)
    def show_confirmation_dialog(self, title: str, text: str):
        """
        Erstellt, zeigt den Bestätigungsdialog an und sendet das Ergebnis zurück an den Worker.
        Diese Methode läuft im Haupt-GUI-Thread.
        """
        # Wir prüfen, ob überhaupt ein Worker aktiv ist, um Fehler zu vermeiden.
        if not self.wizard_worker:
            print("[WARNUNG] show_confirmation_dialog aufgerufen, aber kein Worker aktiv.")
            return

        dialog = ConfirmationDialog(title, text, timeout=10, parent=self)

        # dialog.exec() blockiert die Ausführung DIESES SLOTS (nicht die ganze GUI),
        # bis der Dialog geschlossen wird.
        result = dialog.exec()

        # Das Ergebnis wird an die Methode im Worker-Objekt übergeben,
        # die dann den wartenden Thread aufweckt.
        if result == qtw.QDialog.Accepted:
            self.wizard_worker.set_confirmation_result(True)
        else:
            self.wizard_worker.set_confirmation_result(False)

    @qtc.Slot(bool, str)
    def on_wizard_finished(self, success: bool, message: str):
        """
        Dieser EINE Slot wird aufgerufen, egal ob Wizard A oder B fertig ist.
        """
        print(f"Wizard beendet. Erfolg: {success}. Nachricht: {message}")
        if success:
            self.endzeit = time.perf_counter()
            duration = self.endzeit - self.startzeit
            minutes = int(duration // 60)
            seconds = int(duration % 60)
            laufzeit_csv = f"{minutes}:{seconds}"
            laufzeit_eintragen(laufzeit_csv, message)
            self.statusBar().showMessage(f"Erfolg: {message} (Laufzeit: {minutes}m {seconds}s)", 10000)
        else:
            self.statusBar().showMessage(f"Abbruch: {message} ({zeitstempel(1)})", 12000)

        self.pb_wizard_a.setEnabled(True)
        self.pb_wizard_b.setEnabled(True)

    @qtc.Slot(str, str, str)
    def fertig_abmasse_eintragen(self, x: str, y: str, z: str):
        self.le_x_fertig.setText(x)
        self.le_y_fertig.setText(y)
        self.le_z_fertig.setText(z)
        self.statusBar().showMessage(f"Fertigmaße erfolgreich ausgelesen und eingetragen.", 5000)

    @qtc.Slot()
    def clear_wizard_thread_reference(self):
        print("Räume Thread- und Worker-Referenzen auf.")
        self.wizard_worker = None
        self.wizard_thread = None

    @qtc.Slot(str, str)
    def display_worker_message(self, title: str, text: str):
        msg_box = qtw.QMessageBox(self)
        if "fehler" in title.lower() or "abbruch" in title.lower():
            msg_box.setIcon(qtw.QMessageBox.Icon.Critical)
        else:
            msg_box.setIcon(qtw.QMessageBox.Icon.Warning)

        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setStandardButtons(qtw.QMessageBox.StandardButton.Ok)
        msg_box.exec()

    # --- Rest des Skripts (unverändert) ---

    @qtc.Slot()
    def update_nc_file_count(self):
        wks = self.settings.get("wks")
        if not wks:
            self.lcdn_programme_gefunden.display(0)
            return

        if not self.NC_BASE_PATH.is_dir():
            if self.lcdn_programme_gefunden.intValue() != -1:
                self.statusBar().showMessage(f"Fehler: NC-Basispfad '{self.NC_BASE_PATH}' nicht gefunden!", 10000)
                self.lcdn_programme_gefunden.display(-1)
            return

        wks_folder = f"WKS{wks}"
        found_files_count = 0
        for machine in self.MACHINES:
            source_dir = self.NC_BASE_PATH / machine / wks_folder
            if source_dir.is_dir():
                found_files_count += len(list(source_dir.glob('*.[hH]')))

        self.lcdn_programme_gefunden.display(found_files_count)

        if found_files_count > 0:
            self.pb_rausspielen.setStyleSheet("background-color: #FFA500; color: black;")
        else:
            self.pb_rausspielen.setStyleSheet("")

    @qtc.Slot()
    def on_rausspielen_clicked(self):
        at_prefix = self.le_at_nr.text()
        auftrags_nr = self.le_auftrags_nr.text()

        if not at_prefix:
            self.statusBar().showMessage("Fehler: Bitte eine AT-Nr. angeben.", 7000)
            return
        if not auftrags_nr:
            self.statusBar().showMessage("Fehler: Bitte eine Auftragsnummer angeben.", 7000)
            return

        wks = self.settings.get("wks")
        if not wks:
            self.statusBar().showMessage("Fehler: 'wks' nicht in Einstellungen gefunden.", 7000)
            return

        wks_folder = f"WKS{wks}"

        files_to_move = []
        for machine in self.MACHINES:
            source_dir = self.NC_BASE_PATH / machine / wks_folder
            if source_dir.is_dir():
                files_to_move.extend(source_dir.glob('*.[hH]'))

        if not files_to_move:
            self.statusBar().showMessage("Keine Programme zum Verschieben im WKS-Ordner gefunden.", 7000)
            return

        moved_count = 0
        dest_folder_name = f"AT{at_prefix}-{auftrags_nr}"
        try:
            for source_file in files_to_move:
                machine_name = source_file.parent.parent.name
                destination_dir = self.NC_BASE_PATH / machine_name / dest_folder_name

                destination_dir.mkdir(parents=True, exist_ok=True)
                destination_file = destination_dir / source_file.name

                shutil.copy2(source_file, destination_file)
                source_file.unlink()
                moved_count += 1

            self.statusBar().showMessage(f"{moved_count} Programme erfolgreich nach '{dest_folder_name}' verschoben.",
                                         7000)

        except Exception as e:
            self.statusBar().showMessage(f"Fehler beim Verschieben: {e}", 10000)
            print(f"[FEHLER] Python Commander: {e}")

        self.update_nc_file_count()

    def _get_and_validate_target_dir(self) -> Path | None:
        dir_path_str = self.le_pfad.text()
        if not dir_path_str:
            self.statusBar().showMessage("Fehler: Zielpfad ist nicht angegeben.", 7000)
            return None

        target_dir = Path(dir_path_str)
        if not target_dir.is_dir():
            self.statusBar().showMessage(f"Fehler: Zielordner existiert nicht: {target_dir}", 7000)
            return None

        return target_dir

    @qtc.Slot(str)
    def update_spanntiefe_from_z_fertig(self, text: str):
        is_valid, spanntiefe_value = calculate_spanntiefe(text)
        if is_valid:
            self.le_spanntiefe_b.setText(str(spanntiefe_value))
        else:
            self.le_spanntiefe_b.clear()

    def setup_script_buttons(self):
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

    @qtc.Slot()
    def on_esprit_makro_clicked(self):
        script_path = Path("scripts/esprit_start_makro.py")
        if not script_path.is_file():
            self.statusBar().showMessage(f"Fehler: Makro-Skript nicht gefunden: {script_path}", 7000)
            return
        try:
            self.showMinimized()
            qtc.QTimer.singleShot(200, lambda: self.start_makro_process(script_path))
        except Exception as e:
            self.statusBar().showMessage(f"Fehler bei der Vorbereitung des Makros: {e}", 7000)

    def start_makro_process(self, script_path: Path):
        try:
            command = [sys.executable, str(script_path)]
            subprocess.Popen(command)
            self.statusBar().showMessage("Esprit-Start-Makro wurde ausgeführt.", 5000)
        except Exception as e:
            self.statusBar().showMessage(f"Fehler beim Starten des Makros: {e}", 7000)
            print(f"[FEHLER] Makro-Start fehlgeschlagen: {e}")
            self.showNormal()

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
        source_folder = self._get_and_validate_target_dir()
        if not source_folder:
            self.statusBar().showMessage("Backup-Fehler: Quell-Pfad ungültig oder nicht vorhanden.", 7000)
            return None
        backup_folder = self.settings.get("pfad_backup")
        if not backup_folder:
            self.statusBar().showMessage("Backup-Fehler: 'pfad_backup' nicht in Einstellungen gefunden.", 7000)
            return None
        return ["--source-folder", str(source_folder), "--backup-folder", backup_folder]

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
            self.statusBar().showMessage("Fehler: Bitte eine Spannmittel-Größe angeben.", 7000)
            return

        ziel_ordner = self._get_and_validate_target_dir()
        if not ziel_ordner:
            return

        spannmittel_basis_pfad_str = self.settings.get("spannmittel_basis_pfad")
        if not spannmittel_basis_pfad_str:
            self.statusBar().showMessage("Fehler: 'spannmittel_basis_pfad' nicht in Einstellungen gefunden.", 7000)
            return

        quell_ordner = Path(spannmittel_basis_pfad_str) / spannmittel_typ
        quell_datei = quell_ordner / f"{spannmittel_groesse}.step"
        ziel_datei = ziel_ordner / f"!schraubstock{quell_datei.suffix}"

        try:
            if not quell_datei.is_file():
                self.statusBar().showMessage(f"Fehler: Quelldatei nicht gefunden: {quell_datei.name}", 7000)
                print(f"[FEHLER] Quelldatei nicht gefunden: {quell_datei}")
                return

            shutil.copy2(quell_datei, ziel_datei)
            self.statusBar().showMessage(f"Spannmittel '{ziel_datei.name}' erfolgreich erstellt.", 7000)
            print(f"[INFO] Spannmittel kopiert: '{quell_datei}' -> '{ziel_datei}'")
        except PermissionError:
            self.statusBar().showMessage("Fehler: Keine Berechtigung zum Schreiben im Zielordner.", 7000)
        except Exception as e:
            self.statusBar().showMessage(f"Ein unerwarteter Fehler ist aufgetreten: {e}", 7000)

    @qtc.Slot()
    def rechteck_erstellen_clicked(self):
        length_str = self.le_rechteck_laenge.text()
        width_str = self.le_rechteck_breite.text()
        height_str = self.le_rechteck_hoehe.text()
        is_valid, length, width, height, error_message = validate_dimensions(length_str, width_str, height_str)
        if not is_valid:
            self.statusBar().showMessage(f"Rechteck Fehler: {error_message}", 7000)
            return

        dir_path = self._get_and_validate_target_dir()
        if not dir_path:
            return

        file_name = "!rohteil.dxf"
        full_output_path = str(dir_path / file_name)
        self.statusBar().showMessage(f"Erstelle Rechteck-DXF: {file_name}...", 3000)

        success, message_from_module = rechteck_erstellen(length, width, height, full_output_path)

        if success:
            self.statusBar().showMessage(f"Rechteck erstellt ({zeitstempel(1)})", 7000)
            self.spannmittel_erstellen()
        else:
            self.statusBar().showMessage(f"Rechteck Fehler DXF: {message_from_module}", 7000)

    @qtc.Slot()
    def kreis_erstellen_clicked(self):
        diameter_str = self.le_durchmesser.text()
        height_str = self.le_z_kreis.text()
        is_valid, diameter, height, error_message = validate_circle_dimensions(diameter_str, height_str)
        if not is_valid:
            self.statusBar().showMessage(f"Kreis Fehler: {error_message}", 7000)
            return

        dir_path = self._get_and_validate_target_dir()
        if not dir_path:
            return

        file_name = "!rohteil.dxf"
        full_output_path = str(dir_path / file_name)
        self.statusBar().showMessage(f"Erstelle Kreis-DXF: {file_name}...", 3000)

        success, message_from_module = kreis_erstellen(diameter, height, full_output_path)

        if success:
            self.statusBar().showMessage(f"Kreis erstellt ({zeitstempel(1)})", 7000)
        else:
            self.statusBar().showMessage(f"Kreis Fehler DXF: {message_from_module}", 7000)

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