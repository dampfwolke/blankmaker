from pathlib import Path
from time import sleep

from PySide6.QtCore import QObject, Signal
import pyautogui as pag
import clipboard

from click_image import click_image

class EspritA(QObject):
    # --- Signale für die Kommunikation mit der GUI ---
    # Signal(str) -> sendet eine Statusmeldung als Text
    status_update = Signal(str)
    # Signal(str, str) -> sendet Titel und Text für eine Informations-MessageBox
    show_info_dialog = Signal(str, str)
    # Signal(bool, str) -> sendet Beendigungsstatus (Erfolg/Fehler) und eine finale Nachricht
    finished = Signal(bool, str)

    def __init__(self, pgm_name: str, x_roh: str, y_roh: str, z_roh: str, pfad: Path, bearbeitung_auswahl: str, typ: str,
                 sleep_timer: int):
        # Super(:D) Wichtig: super().__init__() aufrufen, da wir von QObject erben
        super().__init__()
        # Parameter für die Instanziierung der EspritA Klasse
        self.pgm_name = pgm_name
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

    def automations_typ_bestimmen(self) -> None:
        """ Hier wird entschieden welche Autoaktionsabschnitte ausgeführt werden z.B. nur Ausfüllhilfe oder vollständig etc.
        abhängig von dem übergebenen Wert aus der "cb_bearbeitung_auswahl" im main script.
        :return: str """
        if self.typ == "Ausfüllhilfe":
            self.status_update.emit("Starte 'Ausfüllhilfe'")
            self.ausfuellhilfe_a()
        elif self.typ == "Gandalf":
            self.status_update.emit("Starte Automatisierung mit 'Gandalf'")
            self.run()
        else:
            self.status_update.emit("Kein gültiger 'automations_typ' ausgewählt!")
            print("Es wurde kein gültiger 'automations_typ' ausgewählt!")

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

    def fertigteil_bounding_box_auslesen(self) -> tuple[str]:
        """Mithilfe von pyautogui und Hilfsmodul click_image wird in Esprit die Bounding Box des aktuellen Bauteils ausgelesen. :return: tuple[str]"""

    def fertig_abmasse_pruefen(self) -> bool:
        """ Es wird geprüft ob, die Fertigteilmaße korrekt ausgelesen wurden. :return: bool"""

    def fertig_und_rohmasse_vergleichen(self) -> bool:
        """ Prüfung ob Rohteil in X > 1.5mm, in Y > 0.8mm, Z > 4.5mm Aufmaß für Fertigteil hat. :return: bool"""

    def esprit_dateiname_pruefen(self) -> bool:
        """ Prüfung, ob der Pfad existiert und korrekt ist, und ob eine Datei mit demselben Dateinamen im Ordner ist. :return: bool"""

    def ausfuellhilfe_a(self) -> None:
        """ Datei und Programmname werden in den Eigenschaften eingefügt."""
        self.status_update.emit("Ausfüllhilfe gestartet...")
        # Automation
        verweilzeit = self.verweilzeit - 0.15
        pag.click(2438, 122)
        sleep(verweilzeit)
        pag.click(2679, 258)
        sleep(verweilzeit)
        pag.doubleClick(2887, 302)
        sleep(verweilzeit)
        pag.press('delete')
        sleep(verweilzeit)
        # Programmname einfügen und "_A" als Endung hinzufügen
        pgm_name_mit_endung = f"{self.pgm_name}_A".strip()
        # mit clipboard in den Zwischenspeicher kopieren
        clipboard.copy(pgm_name_mit_endung)
        sleep(0.1)
        pag.hotkey("ctrl", "v")
        sleep(verweilzeit)
        pag.press('tab')
        sleep(0.1)
        pag.press('tab')
        sleep(0.1)
        pag.press('delete')
        sleep(0.1)
        # Programmname einfügen ohne Endung
        pgm_name_ohne_endung = self.pgm_name.strip()
        clipboard.copy(pgm_name_ohne_endung)
        sleep(0.1)
        pag.hotkey("ctrl", "v")
        sleep(0.1)
        pag.press('tab')
        sleep(0.1)
        pag.hotkey('ctrl', 'a')
        pag.press('delete')
        sleep(0.1)
        # Art der Bearbeitung einfügen z.B. 5 Achs 3 Achs
        clipboard.copy(self.bearbeitung_auswahl)
        sleep(0.1)
        pag.hotkey("ctrl", "v")
        sleep(verweilzeit)
        pag.press('Enter')
        sleep(verweilzeit)
        # Fokussieren Klick
        pag.doubleClick(2109, 668)
        self.status_update.emit("Ausfüllhilfe abgeschlossen!")

    def esprit_datei_speichern(self) -> None:
        """ Datei wird im aktuellen KW-Wochen Ordner gespeichert"""
        self.status_update.emit("Esprit Datei gespeichert!")

    def rohteil_dxf_importieren(self) -> None:
        """dxf Datei wird aus dem aktuellen KW-Wochen Ordner, in Esprit importiert."""
        self.status_update.emit("Rohteil-DXF geladen!")

    def spannmittel_importieren(self) -> None:
        """Spannmittel wird aus dem aktuellen KW-Wochen Ordner, in Esprit importiert und die Automatisierung abgeschlossen."""
        self.status_update.emit("Importiere Schraubstock...")
        self.status_update.emit("Automatisierung abgeschlossen!")

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