# autoesprit_a.py
from pathlib import Path
import time
from PySide6.QtCore import QObject, Signal


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
        # Wichtig: super().__init__() aufrufen, da wir von QObject erben
        super().__init__()

        self.x_roh = x_roh
        self.y_roh = y_roh
        self.z_roh = z_roh
        self.pfad = pfad
        self.bearbeitung_auswahl = bearbeitung_auswahl
        self.typ = typ
        self.sleep_timer = sleep_timer

    def __str__(self):
        # Korrigierter Name von maschinenauswahl zu bearbeitung_auswahl
        return (f"Abmaße: 'X:{self.x_roh}' x 'Y:{self.y_roh}' x 'Z:{self.z_roh}'\n"
                f"Pfad: {self.pfad}\n"
                f"Bearbeitung: {self.bearbeitung_auswahl}\n"
                f"Umfang der Automation: {self.typ}\n"
                f"Verweilzeit: {self.sleep_timer} Sekunden")

    def abmasse_pruefen(self) -> bool:
        """Platzhalter für eine Validierungsfunktion innerhalb der Klasse."""
        try:
            # Beispiel-Prüfung: Alle Maße müssen > 0 sein
            if float(self.x_roh) > 0 and float(self.y_roh) > 0 and float(self.z_roh) > 0:
                return True
            else:
                self.status_update.emit("Fehler: Rohteilabmaße müssen größer als 0 sein.")
                return False
        except (ValueError, TypeError):
            self.status_update.emit("Fehler: Rohteilabmaße sind keine gültigen Zahlen.")
            return False

    def run(self):
        """
        Hauptmethode, die den Automationsprozess startet.
        Hier kommt deine eigentliche Logik hin.
        """
        self.status_update.emit("Starte Wizard A...")
        print(f"Wizard A gestartet mit folgenden Daten:\n{self}")

        if not self.abmasse_pruefen():
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