from pathlib import Path
from time import sleep

from PySide6.QtCore import QObject, Signal
import pyautogui as pag
import clipboard

from utils.click_image import click_image
from utils.zeitstempel import zeitstempel

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
        self.verweilzeit: float = round(0.1 + (self.sleep_timer / 10), 2)

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
            self.ausfuellhilfe_a()
            self.esprit_datei_speichern()
            self.rohteil_erstellen()
            self.spannmittel_importieren()
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
        self.status_update.emit(f"Ausfüllhilfe gestartet...  {zeitstempel(1)}")
        verweilzeit = self.verweilzeit - 0.15
        pag.click(2438, 122)
        sleep(verweilzeit)
        pag.click(2679, 258)
        sleep(verweilzeit)
        pag.doubleClick(2887, 302)
        self.status_update.emit("Eigenschaften werden ausgefüllt...")
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
        self.status_update.emit(f"Ausfüllhilfe abgeschlossen!  {zeitstempel(1)}")

    def esprit_datei_speichern(self) -> None:
        """ Datei wird im aktuellen KW-Wochen Ordner gespeichert"""
        self.status_update.emit("Bereite speichern vor..")
        pag.click(1965, 36)
        sleep(self.verweilzeit)
        pag.click(2007, 172)
        sleep(0.5)
        pgm_name_mit_endung = f"{self.pgm_name}_A".strip()
        abs_path_mit_pgm_name = Path(self.pfad) / pgm_name_mit_endung
        clipboard.copy(str(abs_path_mit_pgm_name))
        sleep(0.1)
        pag.hotkey("ctrl", "v")
        sleep(0.5)
        pag.press('Enter')
        self.status_update.emit("Esprit wird Datei gespeichert...")
        sleep(4)
        self.status_update.emit(f"Esprit Datei erfolgreich gespeichert. {zeitstempel(1)}")

    def rohteil_erstellen(self) -> None:
        """dxf Datei wird aus dem aktuellen KW-Wochen Ordner in Esprit importiert und die Simulationsbauteile werden erstellt."""

        pag.doubleClick(2109, 668)          # Doppelklick auf Layer
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(1973, 63)                 # Öffnen !rohteil.dxf
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2853, 795)                # Koordinaten vom Pfad im Öffnen Fenster
        sleep(self.verweilzeit)                   # verweilzeit
        self.status_update.emit("Rohteil DXF wird importiert...")
        pfad_rohteil = self.pfad / "!rohteil.dxf"
        clipboard.copy(str(pfad_rohteil))
        sleep(0.1)
        pag.hotkey("ctrl", "v")             # Einfügen des Rohteil.dxf Pfads
        pag.click(3151, 793)                # Öffnen !rohteil.dxf
        sleep(self.verweilzeit)                   # verweilzeit
        self.status_update.emit(f"Rohteil DXF eingefügt!  {zeitstempel(1)}")
        pag.click(2914, 66)                 # Klick auf Ansichten
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2900, 133)                # Klick auf Ansicht Vorne
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2109, 668)                # Klick auf Layer
        sleep(self.verweilzeit)                   # verweilzeit
        self.status_update.emit("Rohteilabmaße werden eingetragen....")
        pag.click(2246, 96)                 # Simulationsparameter
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2071, 192)                # Klick auf Bauteil
        sleep(self.verweilzeit)                   # verweilzeit
        pag.doubleClick(2231, 293)          # Doppelklick auf Länge
        sleep(self.verweilzeit)                   # verweilzeit

        length = float(self.x_roh)
        width = float(self.y_roh)
        height = float(self.z_roh)

        pag.typewrite(str(length))
        pag.press('tab')
        pag.typewrite(str(width))
        pag.press('tab')
        pag.typewrite(str(height))
        pag.press('tab')
        pag.typewrite(str(-length / 2))
        pag.press('tab')
        pag.typewrite(str(-width / 2))
        pag.press('tab')
        pag.typewrite('-4')
        pag.press('tab')

        self.status_update.emit("Simulationsbauteil (Fertigteil) wird erstellt....")

        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2425, 574)                # Aktualisieren
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2064, 247)                # Fertigteil anklicken
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2175, 294)                # Fertigteil Pfeil anklicken
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2900, 631)                # Solid anklicken (Bauteil definieren)
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2900, 631)                # Solid anklicken bestätigen
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2425, 574)                # Aktualisieren

        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2904, 67)                 # Arbeitsebenen
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2904, 102)                # Arbeitsebene Oben
        sleep(self.verweilzeit)                   # self.verweilzeit
        pag.click(2175, 294)                # Fertigteil Pfeil anklicken
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2900, 631)                # Solid anklicken (Bauteil definieren)
        sleep(self.verweilzeit)                   # self.verweilzeit
        pag.click(2900, 631)                # Solid anklicken bestätigen
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2425, 574)                # Aktualisieren

        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2904, 67)                 # Arbeitsebenen
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2904, 118)                # Arbeitsebene Isometrisch
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2175, 294)                # Fertigteil Pfeil anklicken
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2900, 631)                # Solid anklicken (Bauteil definieren)
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2900, 631)                # Solid anklicken bestätigen
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2425, 574)                # Aktualisieren
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2333, 618)                # OK Klicken

        self.status_update.emit(f"Simulationsbauteile erstellt!   {zeitstempel(1)}")

    def spannmittel_importieren(self) -> None:
        """Spannmittel wird aus dem aktuellen KW-Wochen Ordner, in Esprit importiert und die Automatisierung abgeschlossen."""
        self.status_update.emit(f"Spannmittel Import gestartet.  {zeitstempel(1)}")
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2109, 668)                # Klick auf Layer (Fokussieren)
        sleep(0.2)                                # verweilzeit
        self.status_update.emit("Layer werden ausgeblendet...")
        pag.click(1995, 713)                # Solid Layer ausblenden (Haken)
        sleep(0.2)                                # verweilzeit
        pag.click(1995, 729)                # Rohteil Layer ausblenden (Haken)
        sleep(0.2)                                # verweilzeit
        pag.doubleClick(2038, 827)          # Doppelklick auf Müll Layer
        sleep(self.verweilzeit)                   # verweilzeit
        self.status_update.emit("Schraubstock wird geöffnet...")
        pag.click(1973, 63)                 # Öffnen !schraubstock.step
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2853, 795)                # Koordinaten vom Pfad im Öffnen Fenster
        sleep(self.verweilzeit)                   # verweilzeit

        pfad_schraubstock = self.pfad / "!schraubstock"
        clipboard.copy(str(pfad_schraubstock))
        sleep(0.1)
        pag.hotkey("ctrl", "v")             # Einfügen des schraubstock.step Pfads

        pag.click(3151, 793)                # Öffnen !schraubstock.step
        sleep(10)                                 # self.verweilzeit 10 sec (Warten auf Laden von STEP)
        self.status_update.emit(f"Schraubstock erfolgreich importiert.  {zeitstempel(1)}")
        pag.click(2109, 640)                # Fokussieren Klick
        sleep(self.verweilzeit)                   # verweilzeit
        self.status_update.emit("Schraubstock wird als Spannmittel definiert...")
        pag.hotkey('ctrl', 'a')             # Alles markieren im Müll Layer
        sleep(self.verweilzeit)                   # self.verweilzeit
        pag.click(2373, 126)                # Simulationsbauteil erstellen
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(2766, 659)                # Übernehmen
        pag.click(2109, 640)                # Fokussieren Klick
        sleep(self.verweilzeit)                   # verweilzeit
        pag.click(1995, 825)                # Müll Layer ausblenden (Haken)
        sleep(0.2)                                # verweilzeit
        self.status_update.emit("Layer werden wieder eingeblendet...")
        pag.click(1995, 713)                # Solid Layer einblenden (Haken)
        sleep(0.2)                                # verweilzeit
        pag.click(1995, 729)                # Rohteil Layer einblenden (Haken)
        sleep(0.2)                                # verweilzeit
        pag.doubleClick(2038, 745)          # Doppelklick auf Feature
        sleep(0.2)                                # verweilzeit
        pag.click(2246, 96)                 # Simulationsparameter öffnen
        sleep(self.verweilzeit)                   # verweilzeit
        self.status_update.emit(f"Automatisierung abgeschlossen! {zeitstempel(1)}")
        # self.finished.emit(True, "Wizard A erfolgreich abgeschlossen.")

#####################################################################################################

    def run(self):
        self.automations_typ_bestimmen()
        self.finished.emit(True, "Wizard A erfolgreich abgeschlossen.")


    # def run(self):
    #     """
    #     Hauptmethode, die den Automationsprozess startet.
    #     Hier kommt deine eigentliche Logik hin.
    #     """
    #     self.status_update.emit("Starte Wizard A...")
    #     print(f"Wizard A gestartet mit folgenden Daten:\n{self}")
    #
    #     if not self.roh_abmasse_pruefen():
    #         # Prozess mit Fehlermeldung beenden
    #         self.finished.emit(False, "Validierung der Abmaße fehlgeschlagen.")
    #         return
    #
    #     # --- Hier deine Logik einfügen ---
    #     # Beispiel: Simuliere Arbeitsschritte und sende Updates an die GUI
    #     try:
    #         self.status_update.emit("Schritt 1: Analysiere Geometrie...")
    #         sleep(self.sleep_timer / 2.0)  # Simuliere Arbeit
    #
    #         self.status_update.emit("Schritt 2: Generiere Werkzeugwege...")
    #         sleep(self.sleep_timer / 2.0)  # Simuliere Arbeit
    #
    #         # Beispiel für eine Interaktion: Zeige eine Info-Box über die GUI
    #         self.show_info_dialog.emit("Hinweis", f"Die Bearbeitung '{self.bearbeitung_auswahl}' wurde ausgewählt.")
    #
    #         # Wenn alles gut geht, sende ein Erfolgssignal
    #         self.finished.emit(True, "Wizard A erfolgreich abgeschlossen.")
    #
    #     except Exception as e:
    #         # Bei einem Fehler, sende ein Fehlersignal
    #         error_message = f"Ein Fehler ist im Wizard A aufgetreten: {e}"
    #         self.finished.emit(False, error_message)