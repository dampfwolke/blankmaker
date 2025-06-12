from pathlib import Path
from time import sleep
import re

from PySide6.QtCore import QObject, Signal, QThread
import pyautogui as pag
import clipboard

from utils.click_image import click_image
from utils.zeitstempel import zeitstempel

class EspritB(QObject):
    # Signal(str) -> sendet eine Statusmeldung als Text
    status_update_b = Signal(str)
    # Signal(str, str) -> sendet Titel und Text für eine Informations-MessageBox
    show_info_dialog_b = Signal(str, str)
    # Signal(bool, str) -> sendet Beendigungsstatus (Erfolg/Fehler) und eine finale Nachricht
    finished_b = Signal(bool, str)
    # Signal Fertigteil Abmasse X Y Z ausgelesen
    ausgelesene_fertig_werte_b = Signal(str, str, str)

    # Konstante Pfade für Rohteilmitnahme und Allmatic 125 Schraubstock
    PFAD_ROHTEILMITNAHME = Path(r"C:\Users\hasanovic\Desktop\Rohteilmitnahme\Hasanovic")
    PFAD_ALLMATIC_125 = Path(r"C:\Users\hasanovic\Desktop\Spannmittel\19_Allmatic_125_EVO_100")

    def __init__(self, pgm_name_b: str, typ_b: str, pfad_b: Path, sleep_timer: int):
        super().__init__()
        self.pgm_name_b = pgm_name_b
        self.typ_b = typ_b
        self.pfad_b = pfad_b
        self.sleep_timer = sleep_timer

        # Verzögerung zwischen den Aktionen (min. 0.2s, max. 10.2s) je nach QSlider Einstellung im main script
        self.verweilzeit: float = round(0.1 + (self.sleep_timer / 20), 2)

        # Fertigteil Abmaße von dem aktuellen Solid Bauteil (werden in dieser Klasse ausgelesen und weiter verarbeitet)
        self.x_fertig = None
        self.y_fertig = None
        self.z_fertig = None

    def abgeschlossen_b(self) -> None:
        """Sendet das finale Erfolgssignal."""
        self.finished_b.emit(True, f"Automatisierung '{self.typ_b}' erfolgreich abgeschlossen.")

    def automations_typ_bestimmen_b(self):
        """ Hier wird entschieden welche Autoaktionsabschnitte ausgeführt werden z.B. nur Ausfüllhilfe oder vollständig etc.
        abhängig von dem übergebenen Wert aus der "cb_bearbeitung_auswahl" im main script.
        :return: None """
        if self.typ_b == "Ausfüllhilfe B":
            self.status_update_b.emit("Starte 'Ausfüllhilfe_B'")
            self.ausfuellhilfe_b()

            if self.esprit_dateiname_pruefen_b():
                self.esprit_datei_speichern_b()

            self.abgeschlossen_b()

        elif self.typ_b == "TEST_B":
            # Hier deine Logik für den Platzhalter-Typ einfügen
            self.status_update_b.emit("Platzhalter-Funktion wurde aufgerufen.")
            self.finished_b.emit(True, "Platzhalter-Funktion beendet.")
            pass  # Platzhalter für Testfunktionen

        else:
            error_msg = "Kein gültiger 'automations_typ' ausgewählt!"
            self.status_update_b.emit(error_msg)
            self.show_info_dialog_b.emit("Auswahlfehler", error_msg)
            self.finished_b.emit(False, error_msg)


    def esprit_dateiname_pruefen_b(self) -> tuple[bool, str]:
        """ Prüfung, ob der Pfad existiert und ob eine Datei mit demselben Namen bereits im Ordner ist.
         :return: (bool, str)"""
        if not self.pfad_b.is_dir():
            error_msg = f"Fehler: Der angegebene Pfad '{self.pfad_b}' existiert nicht oder ist kein Ordner."
            self.status_update_b.emit(error_msg)
            return False, error_msg

        dateiname_mit_endung = f"{self.pgm_name_b}_B.esp"
        zieldatei_pfad = self.pfad_b / dateiname_mit_endung

        if zieldatei_pfad.exists():
            error_msg = f"Die Datei '{dateiname_mit_endung}' existiert bereits im Zielordner."
            self.status_update_b.emit(f"Abbruch: {error_msg}")
            return False, error_msg

        self.status_update_b.emit("Dateiname und Pfad sind gültig.")
        return True, ""

    def esprit_datei_speichern_b(self):
        pag.doubleClick(2109, 668)            # Doppelklick auf Layer
        sleep(self.verweilzeit)                     # Verweilzeit
        pag.click(2109, 668)                  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)                     # Verweilzeit
        pag.hotkey('ctrl', 's')               # A-Seite speichern
        sleep(4)                                    # Verweilzeit
        pag.doubleClick(2109, 668)            # Doppelklick auf Layer
        sleep(self.verweilzeit)                     # Verweilzeit

        # wird evtl. nicht gebraucht --> TESTEN
        pag.click(2109, 668)                  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)                     # Verweilzeit
        pag.click(2197, 728)                  # Klick auf "Alles auswählen"
        sleep(self.verweilzeit)                     # Verweilzeit
        pag.click(2000, 698)                  # Alle Layer ausblenden (Haken)
        sleep(self.verweilzeit)                     # Verweilzeit
        pag.doubleClick(2038, 713)            # Doppelklick auf Solid Layer

    def fertigteil_bounding_box_auslesen(self) -> None:
        """Mithilfe von pyautogui und Hilfsmodul click_image wird in Esprit die Bounding Box des aktuellen Bauteils ausgelesen."""
        self.status_update_b.emit("Starte Fertigteilmaß auslesen....")
        bild_pfad_relativ = Path(".") / "utils" / "automation_bilder" / "bauteil.png"
        bild_pfad_absolut = bild_pfad_relativ.resolve()

        # KÖNNTE evtl. PASSEN --> TESTEN
        pag.click(2109, 668)                  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)                     # Verweilzeit
        pag.click(2197, 728)                  # Klick auf "Alles auswählen"
        sleep(self.verweilzeit)                     # Verweilzeit
        pag.click(2000, 698)                  # Alle Layer ausblenden (Haken)
        sleep(self.verweilzeit)                     # Verweilzeit
        pag.doubleClick(2038, 713)            # Doppelklick auf Solid Layer

        # Anpassen für B-SEITE
        # NACH DEM AUSLESEN MUSS DERSELBE ZUSTAND WIE OHNE AUSLESEN SEIN DAMIT ROHTEILMITNAHME USW. FUNKTIONIEREN

        verweilzeit = self.verweilzeit  # festlegen der Sleep Zeit
        pag.doubleClick(2109, 668)  # Doppelklick auf Layer
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(verweilzeit)  # Verweilzeit
        pag.doubleClick(2038, 713)  # Doppelklick auf Solid Layer
        sleep(verweilzeit)  # Verweilzeit
        self.status_update_b.emit("Fertigteilmaß wird ausgelesen...")
        pag.click(2481, 68)  # Nur Volumenmodell Auswahl anklicken (aufklappen)
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2480, 434)  # Nur Volumenmodell auswählen
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2109, 640)  # Fokussieren Klick
        sleep(verweilzeit)  # Verweilzeit
        pag.hotkey('ctrl', 'a')  # Alles markieren (Solid)
        sleep(verweilzeit)  # Verweilzeit
        click_image(str(bild_pfad_absolut), toleranz=0.65)  # Auf Bauteil Reiter klicken mit Bilderkennung
        self.status_update_b.emit("Reiter Bauteil gefunden...")
        sleep(verweilzeit)  # Verweilzeit
        pag.click(1291, 47)  # Auf Erkunden Reiter im Bauteil Menü klicken
        self.status_update_b.emit("Abmaße werden in Zwischenspeicher kopiert...")
        sleep(verweilzeit)  # Verweilzeit
        pag.doubleClick(1669, 331)  # Doppelklick auf Länge des Bauteils
        sleep(verweilzeit)  # Verweilzeit
        pag.hotkey('ctrl', 'c')  # Abmaße des Fertigteils kopieren
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2481, 68)  # Nur Volmenmodell Auswahl anklicken (aufklappen)
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2472, 88)  # Alles auswählen
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2109, 640)  # Fokussieren Klick
        sleep(verweilzeit)  # Verweilzeit
        pag.click(1308, 1009)  # Auf Feature im Projekt-Manager klicken
        sleep(verweilzeit)  # Verweilzeit
        pag.doubleClick(2038, 697)  # Doppelklick auf Standard Layer
        clipboard_content = clipboard.paste()
        string = clipboard_content.strip("()")
        string = re.sub(r'(\d+),(\d+)', r'\1.\2', string)
        abmasse = string.split(', ')
        self.x_fertig = abmasse[0]
        self.y_fertig = abmasse[1]
        self.z_fertig = abmasse[2]
        self.status_update_b.emit(f"Ausgelesen: X={self.x_fertig}, Y={self.y_fertig}, Z={self.z_fertig}")

    def fertig_abmasse_pruefen_b(self) -> tuple[bool, str]:
        """ Es wird geprüft ob, die Fertigteilmaße korrekt ausgelesen wurden. :return: (bool, str)"""
        try:
            if self.x_fertig is None or self.y_fertig is None or self.z_fertig is None:
                msg = "Fertigteilmaße wurden nicht ausgelesen."
                self.status_update_b.emit(f"Fehler: {msg}")
                return False, msg

            if float(self.x_fertig) > 0 and float(self.y_fertig) > 0 and float(self.z_fertig) > 0:
                self.status_update_b.emit("Fertigteilmaße erfolgreich validiert.")
                return True, ""
            else:
                msg = "Ausgelesene Fertigteilmaße müssen größer als 0 sein."
                self.status_update_b.emit(f"Fehler: {msg}")
                return False, msg
        except (ValueError, TypeError):
            msg = "Ausgelesene Fertigteilmaße sind keine gültigen Zahlen."
            self.status_update_b.emit(f"Fehler: {msg}")
            return False, msg

    def ausfuellhilfe_b(self):
        self.status_update_b.emit("Ausfüllhilfe B-Seite gestartet...")
        pag.click(2438, 122)
        sleep(0.2)
        self.status_update_b.emit("PGM-Name wird auf _B geändert...")
        pag.click(2679, 258)
        for i in range(11):
            sleep(0.05)
            pag.press('tab')
        pag.press('delete')
        sleep(self.verweilzeit)
        pgm_name_mit_endung = f"{self.pgm_name_b}_B".strip()
        clipboard.copy(pgm_name_mit_endung)
        sleep(self.verweilzeit)
        pag.hotkey("ctrl", "v")
        sleep(self.verweilzeit)
        self.status_update_b.emit("Eigenschaften Fenster schließen...")
        pag.press('Enter')
        sleep(self.verweilzeit)
        pag.doubleClick(2109, 668)
        sleep(self.verweilzeit)


    def rohteilmitnahme(self):
        verweilzeit = self.verweilzeit  # festlegen der Sleep Zeit

        pag.doubleClick(2109, 668)  # Doppelklick auf Layer
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2197, 728)  # Klick auf "Alles auswählen"
        sleep(verweilzeit)  # Verweilzeit
        pag.click(1996, 697)  # Alle Layer ausblenden (Haken)
        sleep(verweilzeit)  # Verweilzeit
        pag.doubleClick(2038, 827)  # Doppelklick auf Müll Layer
        sleep(verweilzeit)  # Verweilzeit
        pag.doubleClick(2038, 875)  # Doppelklick auf Spannmittel Layer
        sleep(verweilzeit)  # Verweilzeit
        pag.doubleClick(2109, 668)  # Doppelklick auf Layer
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2094, 591)  # Klick auf Layer (Fokussieren)
        sleep(verweilzeit)  # Verweilzeit
        pag.hotkey('ctrl', 'a')  # Alles markieren im Müll und Spannmittel Layer
        sleep(verweilzeit)  # Verweilzeit
        pag.rightClick(2094, 591)  # Rechtsklick für Kontextmenü
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2154, 625)  # Löschen im Kontextmenü klicken
        sleep(2)  # Verweilzeit 2 Sekunden

        pag.doubleClick(2038, 857)  # Doppelklick auf Rohteilmitnahme Layer
        sleep(verweilzeit)  # Verweilzeit
        pag.click(1973, 63)  # Öffnen Rohteilmitnahme.stl
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2853, 795)  # Koordinaten vom Pfad im Öffnen Fenster
        sleep(verweilzeit)  # Verweilzeit

        sleep(self.verweilzeit)
        self.status_update_b.emit("Rohteilmitnahme STL wird importiert...")
        pfad_rohteilmitnahme = self.PFAD_ROHTEILMITNAHME
        clipboard.copy(str(pfad_rohteilmitnahme))
        sleep(0.1)
        pag.hotkey("ctrl", "v")


        pag.click(3151, 793)  # Öffnen Rohteilmitnahme.stl
        sleep(5)  # Verweilzeit
        pag.click(2109, 668)  # Klick auf Layer

        sleep(verweilzeit)  # Verweilzeit
        pag.click(2246, 96)  # Simulationsparameter
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2071, 192)  # Klick auf Bauteil
        sleep(0.5)  # Verweilzeit
        pag.click(2064, 230)  # Klick auf Rohteil
        sleep(0.5)  # Verweilzeit
        pag.click(2418, 246)  # Volumenmodell auswählen
        sleep(0.5)  # Verweilzeit
        pag.click(2418, 276)  # Volumenmodell anklicken
        sleep(0.5)  # Verweilzeit
        pag.click(2418, 276)  # Volumenmodell anklicken

        sleep(verweilzeit)  # Verweilzeit
        pag.click(2904, 67)  # Arbeitsebenen
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2904, 133)  # Arbeitsebene Vorne
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2175, 294)  # Fertigteil Pfeil anklicken
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2900, 640)  # Solid anklicken (Bauteil definieren)
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2900, 640)  # Solid anklicken bestätigen
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2425, 574)  # Aktualisieren

        sleep(verweilzeit)  # Verweilzeit
        pag.click(2904, 67)  # Arbeitsebenen
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2904, 102)  # Arbeitsebene Oben
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2175, 294)  # Fertigteil Pfeil anklicken
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2900, 640)  # Solid anklicken (Bauteil definieren)
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2900, 640)  # Solid anklicken bestätigen
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2425, 574)  # Aktualisieren

        sleep(verweilzeit)  # Verweilzeit
        pag.click(2904, 67)  # Arbeitsebenen
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2904, 118)  # Arbeitsebene Isometrisch
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2175, 294)  # Fertigteil Pfeil anklicken
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2900, 640)  # Solid anklicken (Bauteil definieren)
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2900, 640)  # Solid anklicken bestätigen
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2425, 574)  # Aktualisieren

        sleep(verweilzeit)  # Verweilzeit
        pag.click(2333, 618)  # OK Klicken
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(verweilzeit)  # Verweilzeit


    # Für Zukünftige Automatisierung --> Prüft ob der NP auf der B-Seite stimmt
    def nullpunkt_pruefen(self):
        pass

    def run_b(self):
        """Hauptmethode des Workers, die beim Start des Threads ausgeführt wird."""
        try:
            self.automations_typ_bestimmen_b()
        except Exception as e:
            # Bei einem Fehler, sende ein Fehlersignal mit der Fehlermeldung
            error_message = f"Ein unerwarteter Fehler ist aufgetreten: {e}"
            self.status_update_b.emit(error_message)
            self.show_info_dialog_b.emit("Kritischer Fehler", error_message)
            self.finished_b.emit(False, error_message)
            print(f"[FEHLER] im EspritA Worker: {e}")