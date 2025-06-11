from pathlib import Path
import time
from PySide6.QtCore import QObject, Signal

from click_image import click_image

class EspritA(QObject):
    # --- Signale für die Kommunikation mit der GUI ---
    # Signal(str) -> sendet eine Statusmeldung als Text
    status_update = Signal(str)
    # Signal(str, str) -> sendet Titel und Text für eine Informations-MessageBox
    show_info_dialog = Signal(str, str)
    # Signal(bool, str) -> sendet Beendigungsstatus (Erfolg/Fehler) und eine finale Nachricht
    finished = Signal(bool, str)

    def __init__(self, x_roh: str, y_roh: str, z_roh: str, pfad: Path, bearbeitung_auswahl: str, typ: str,
                 sleep_timer: int):
        # Super(:D) Wichtig: super().__init__() aufrufen, da wir von QObject erben
        super().__init__()
        # Parameter für die Instanziierung der EspritA Klasse
        self.x_roh = x_roh
        self.y_roh = y_roh
        self.z_roh = z_roh
        self.pfad = pfad
        self.bearbeitung_auswahl = bearbeitung_auswahl
        self.typ = typ
        self.sleep_timer = sleep_timer

        # Verzögerung zwischen den Aktionen (min. 0.3s, max. 10.2s) je nach QSlider Einstellung im main script
        self.verweilzeit: float = round(0.2 + (self.sleep_timer / 10), 2)

        # Fertigteil Abmaße von dem aktuellen Solid Bauteil (werden in dieser Klasse ausgelesen und weiter verarbeitet)
        self.x_fertig = None
        self.y_fertig = None
        self.z_fertig = None

    def __str__(self):
        return (f"Abmaße: 'X:{self.x_roh}' x 'Y:{self.y_roh}' x 'Z:{self.z_roh}'\n"
                f"Pfad: {self.pfad}\n"
                f"Bearbeitung: {self.bearbeitung_auswahl}\n"
                f"Umfang der Automation: {self.typ}\n"
                f"Verweilzeit: {self.sleep_timer} Sekunden")

    def automations_typ_bestimmen(self) -> str:
        """ Hier wird entschieden welche Autoaktionsabschnitte ausgeführt werden z.B. nur Ausfüllhilfe oder vollständig etc.
        abhängig von dem übergebenen Wert aus der "cb_bearbeitung_auswahl" im main script
        :return: str """
        pass

    def roh_abmasse_pruefen(self) -> bool:
        """ Prüfung ob Rohteilmaße gültig sind :return: bool"""
        try:
            if float(self.x_roh) > 0 and float(self.y_roh) > 0 and float(self.z_roh) > 0:
                return True
            else:
                self.status_update.emit("Fehler: Rohteilabmaße müssen größer als 0 sein.")
                return False
        except (ValueError, TypeError):
            self.status_update.emit("Fehler: Rohteilabmaße sind keine gültigen Zahlen.")
            return False

#####################################################################################################
    def fertigteil_bounding_box_auslesen(self) -> tuple[str]:
        """Mithilfe von pyautogui und Hilfsmodul click_image wird in Esprit die Bounding Box des aktuellen Bauteils ausgelesen. :return: tuple[str]"""

    def fertig_abmasse_pruefen(self) -> bool:
        pass

    def fertig_und_rohmasse_vergleichen(self) -> bool:
        pass

    def esprit_dateiname_pruefen(self) -> bool:
        pass

    def esprit_datei_speichern(self):
        pass

    def ausfuellhilfe_a(self):
        pass

    def rohteil_dxf_importieren(self):
        pass

    def spannmittel_importieren(self):
        pass

#####################################################################################################


    def run(self):
        """
        Hauptmethode, die den Automationsprozess startet.
        Hier kommt deine eigentliche Logik hin.
        """
        self.status_update.emit("Starte Wizard A...")
        print(f"Wizard A gestartet mit folgenden Daten:\n{self}")

        if not self.roh_abmasse_pruefen():
            # Prozess mit Fehlermeldung beenden
            self.finished.emit(False, "Validierung der Abmaße fehlgeschlagen.")
            return

        # --- Hier deine Logik einfügen ---
        # Beispiel: Simuliere Arbeitsschritte und sende Updates an die GUI
        try:
            self.status_update.emit("Schritt 1: Analysiere Geometrie...")
            time.sleep(self.sleep_timer / 2.0)  # Simuliere Arbeit

            self.status_update.emit("Schritt 2: Generiere Werkzeugwege...")
            time.sleep(self.sleep_timer / 2.0)  # Simuliere Arbeit

            # Beispiel für eine Interaktion: Zeige eine Info-Box über die GUI
            self.show_info_dialog.emit("Hinweis", f"Die Bearbeitung '{self.bearbeitung_auswahl}' wurde ausgewählt.")

            # Wenn alles gut geht, sende ein Erfolgssignal
            self.finished.emit(True, "Wizard A erfolgreich abgeschlossen.")

        except Exception as e:
            # Bei einem Fehler, sende ein Fehlersignal
            error_message = f"Ein Fehler ist im Wizard A aufgetreten: {e}"
            self.finished.emit(False, error_message)