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
    status_update = Signal(str)
    # Signal(str, str) -> sendet Titel und Text für eine Informations-MessageBox
    show_info_dialog = Signal(str, str)
    # Signal(bool, str) -> sendet Beendigungsstatus (Erfolg/Fehler) und eine finale Nachricht
    finished = Signal(bool, str)
    # Signal Fertigteil Abmasse X Y Z ausgelesen
    ausgelesene_fertig_werte = Signal(str, str, str)

    # Konstante Pfade für Rohteilmitnahme und Allmatic 125 Schraubstock
    PFAD_ROHTEILMITNAHME = Path(r"C:\Users\hasanovic\Desktop\Rohteilmitnahme\Hasanovic.stl")
    PFAD_DIR_ALLMATIC_125 = Path(r"C:\Users\hasanovic\Desktop\Spannmittel\19_Allmatic_125_EVO_100")

    def __init__(self, pgm_name: str, typ: str, pfad: Path, sleep_timer: int):
        super().__init__()
        self.pgm_name = pgm_name
        self.typ = typ
        self.pfad = pfad
        self.sleep_timer = sleep_timer

        # Verzögerung zwischen den Aktionen (min. 0.081s, max. 3.175s) je nach QSlider Einstellung im main script
        self.verweilzeit: float = round(0.1 + (self.sleep_timer / 32), 2)

        # Fertigteil Abmaße von dem aktuellen Solid Bauteil (werden in dieser Klasse ausgelesen und weiter verarbeitet)
        self.x_fertig = None
        self.y_fertig = None
        self.z_fertig = None
        self.spanntiefe = None


    def automations_typ_bestimmen_b(self):
        """ Hier wird entschieden welche Autoaktionsabschnitte ausgeführt werden z.B. nur Ausfüllhilfe oder vollständig etc.
        abhängig von dem übergebenen Wert aus der "cb_bearbeitung_auswahl_b" im main script.
        :return: None """
        if self.typ == "Saruman":
            self.status_update.emit("Starte 'Saruman'")
        elif self.typ == "Saruman light":
            self.status_update.emit("Starte 'Saruman light'")
        elif self.typ == "Ausfüllhilfe B":
            self.status_update.emit("Starte 'Ausfüllhilfe_B'")
            self.esprit_a_sicherung_speichern_b()
            self.ausfuellhilfe_b()
            self.abgeschlossen_b()
        elif self.typ == "Bounding Box auslesen B":
            self.status_update.emit("Starte 'Saruman light'")
            self.fertigteil_bounding_box_auslesen_b()
            self.finished.emit(True, "Starte 'Saruman light' beendet.")
        else:
            error_msg = "Kein gültiger 'automations_typ' ausgewählt!"
            self.status_update.emit(error_msg)
            self.show_info_dialog.emit("Auswahlfehler", error_msg)
            self.finished.emit(False, error_msg)

    def esprit_dateiname_pruefen_b(self) -> tuple[bool, str]:
        """ Prüfung, ob der Pfad existiert und ob eine Datei mit demselben Namen bereits im Ordner ist.
         :return: (bool, str)"""
        if not self.pfad.is_dir():
            error_msg = f"Fehler: Der angegebene Pfad '{self.pfad}' existiert nicht oder ist kein Ordner."
            self.status_update.emit(error_msg)
            return False, error_msg

        dateiname_mit_endung = f"{self.pgm_name}_B.esp"
        zieldatei_pfad = self.pfad / dateiname_mit_endung

        if zieldatei_pfad.exists():
            error_msg = f"Die Datei '{dateiname_mit_endung}' existiert bereits im Zielordner."
            self.status_update.emit(f"Abbruch: {error_msg}")
            return False, error_msg

        self.status_update.emit("Dateiname und Pfad sind gültig.")
        return True, ""

    def esprit_a_sicherung_speichern_b(self) -> None:
        '''Speichert noch einmal die A-Seite zur Sicherheit ab, bevor Automation für B-Seite beginnt.'''
        pag.doubleClick(2109, 668)            # Doppelklick auf Layer
        sleep(self.verweilzeit)                     # Verweilzeit
        pag.click(2109, 668)                  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)                     # Verweilzeit
        pag.hotkey('ctrl', 's')               # A-Seite speichern
        sleep(4)                                    # Verweilzeit
        pag.doubleClick(2109, 668)            # Doppelklick auf Layer
        sleep(self.verweilzeit)                     # Verweilzeit
        pag.click(2109, 668)                  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)                     # Verweilzeit
        pag.click(2197, 728)                  # Klick auf "Alles auswählen"
        sleep(self.verweilzeit)                     # Verweilzeit
        pag.click(2000, 698)                  # Alle Layer ausblenden (Haken)
        sleep(self.verweilzeit)                     # Verweilzeit
        pag.doubleClick(2038, 713)            # Doppelklick auf Solid Layer

    def ausfuellhilfe_b(self):
        self.status_update.emit("Ausfüllhilfe B-Seite gestartet...")
        pag.click(2094, 591)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # Verweilzeit
        pag.click(2438, 122) # # eigenschaften öffnen
        sleep(self.verweilzeit)
        self.status_update.emit("PGM-Name wird auf _B geändert...")
        pag.click(2679, 258) # reiter in eigenschaften öffnen
        for i in range(10):
            sleep(0.05)
            pag.press('tab')
        pag.press('delete')
        sleep(self.verweilzeit)
        pgm_name_mit_endung = f"{self.pgm_name}_B".strip()
        clipboard.copy(pgm_name_mit_endung)
        sleep(self.verweilzeit)
        pag.hotkey("ctrl", "v")
        sleep(self.verweilzeit)
        self.status_update.emit("Eigenschaften Fenster schließen...")
        pag.press('Enter')
        sleep(self.verweilzeit)
        pag.click(2109, 668)                  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)                     # Verweilzeit
        # pag.doubleClick(2109, 668)
        # sleep(self.verweilzeit)
        # pag.click(2000, 700) # Standard layer einblenden
        # sleep(self.verweilzeit)
        # pag.click(2000, 716) # Solid layer einblenden

    def fertigteil_bounding_box_auslesen_b(self) -> None:
        """Mithilfe von pyautogui und Hilfsmodul click_image wird in Esprit die Bounding Box des aktuellen Bauteils ausgelesen."""
        self.status_update.emit("Starte Fertigteilmaß auslesen....")
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
        self.status_update.emit("Fertigteilmaß wird ausgelesen...")
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
        self.status_update.emit("Reiter Bauteil gefunden...")
        sleep(verweilzeit)  # Verweilzeit
        pag.click(1291, 47)  # Auf Erkunden Reiter im Bauteil Menü klicken
        self.status_update.emit("Abmaße werden in Zwischenspeicher kopiert...")
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
        self.status_update.emit(f"Ausgelesen: X={self.x_fertig}, Y={self.y_fertig}, Z={self.z_fertig}")

    def fertig_abmasse_pruefen_b(self) -> tuple[bool, str]:
        """ Es wird geprüft ob, die Fertigteilmaße korrekt ausgelesen wurden. :return: (bool, str)"""
        try:
            if self.x_fertig is None or self.y_fertig is None or self.z_fertig is None:
                msg = "Fertigteilmaße wurden nicht ausgelesen."
                self.status_update.emit(f"Fehler: {msg}")
                return False, msg

            if float(self.x_fertig) > 0 and float(self.y_fertig) > 0 and float(self.z_fertig) > 0:
                self.status_update.emit("Fertigteilmaße erfolgreich validiert.")
                return True, ""
            else:
                msg = "Ausgelesene Fertigteilmaße müssen größer als 0 sein."
                self.status_update.emit(f"Fehler: {msg}")
                return False, msg
        except (ValueError, TypeError):
            msg = "Ausgelesene Fertigteilmaße sind keine gültigen Zahlen."
            self.status_update.emit(f"Fehler: {msg}")
            return False, msg
    
    def fertig_abmasse_eintragen_b(self):
        x = str(self.x_fertig)
        y = str(self.y_fertig)
        z = str(self.z_fertig)
        self.ausgelesene_fertig_werte.emit(x, y, z)

    def esprit_datei_speichern_b(self):
        '''Datei von A-Seite auf B-Seite mit _B speichern'''
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)
        pag.click(1965, 36)
        sleep(self.verweilzeit)
        pag.click(2007, 188)
        sleep(self.verweilzeit)
        pgm_name_mit_endung = f"{self.pgm_name}_B".strip()
        clipboard.copy(pgm_name_mit_endung)
        sleep(self.verweilzeit)
        pag.hotkey("ctrl", "v")
        sleep(self.verweilzeit)
        sleep(self.verweilzeit)
        pag.press('Enter')
        sleep(4)

    def abgeschlossen_b(self) -> None:
        """Sendet das finale Erfolgssignal."""
        self.finished.emit(True, f"Automatisierung '{self.typ}' erfolgreich abgeschlossen.")

############################# MUSS ALLES NOCH GETESTET WERDEN   #################################################
    def rohteilmitnahme(self):
        verweilzeit = self.verweilzeit  # festlegen der Sleep Zeit
        self.status_update.emit("Rohteilmitnahme gestartet...")
        pag.doubleClick(2109, 668)  # Doppelklick auf Layer
        sleep(verweilzeit)  # Verweilzeit
        self.status_update.emit("Richtiger Layer wird ausgewählt...")
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
        self.status_update.emit("Müll- und Spannmittel-Layer werden gelöscht...")
        pag.hotkey('ctrl', 'a')  # Alles markieren im Müll und Spannmittel Layer
        sleep(verweilzeit)  # Verweilzeit
        pag.rightClick(2094, 591)  # Rechtsklick für Kontextmenü
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2154, 625)  # Löschen im Kontextmenü klicken
        sleep(2.5)  # Verweilzeit 2 Sekunden
        self.status_update.emit("Öffne Rohteilmitnahme...")
        pag.doubleClick(2038, 857)  # Doppelklick auf Rohteilmitnahme Layer
        sleep(verweilzeit)  # Verweilzeit
        pag.click(1973, 63)  # Öffnen Rohteilmitnahme.stl
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2853, 795)  # Koordinaten vom Pfad im Öffnen Fenster
        sleep(verweilzeit)  # Verweilzeit
        sleep(self.verweilzeit)
        self.status_update.emit("Rohteilmitnahme STL wird importiert...")
        pfad_rohteilmitnahme = self.PFAD_ROHTEILMITNAHME
        clipboard.copy(str(pfad_rohteilmitnahme))
        sleep(0.1)
        pag.hotkey("ctrl", "v")
        pag.click(3151, 793)  # Öffnen Rohteilmitnahme.stl
        sleep(5)  # Verweilzeit
        pag.click(2109, 668)  # Klick auf Layer
        self.status_update.emit("Rohteilmitnahme wird als Simulationsbauteil definiert...")
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

    def rotieren(self):
        pag.doubleClick(2109, 668)  # Doppelklick auf Layer
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(1995, 713)  # Solid Layer einblenden (Haken)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2684, 67)  # Arbeitsebenen anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.moveTo(2684, 102)  # Arbeitsebene XYZ Maus zur Position bewegen
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.scroll(15)  # Mausrad 15 Mal nach oben bewegen
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2684, 176)  # Arbeitsebene hinten anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.hotkey('ctrl', 'a')  # Alles markieren im Solid- und Rohteilmitnahme Layer
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.rightClick(2070, 599)  # Rechtsklick für Kontextmenü
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2158, 609)  # Modifizieren im Kontextmenü klicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2943, 400)  # Modifizieren fokussieren
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.press("r")  # Rotieren mit "r" anwählen
        sleep(self.verweilzeit)  # self.verweilzeit

        pag.click(2756, 470)  # Original modifizieren Haken anklicken
        sleep(self.verweilzeit)  # self.verweilzeit

        pag.click(2755, 588)  # Haken bei "Wähle Nullpunkt als Rotation" klicken
        sleep(self.verweilzeit)  # self.verweilzeit

        pag.click(2840, 625)  # Rotieren mit Mausklick auf "OK" bestätigen
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2684, 67)  # Arbeitsebenen anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.scroll(15)  # Mausrad 15 Mal nach oben bewegen
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2684, 102)  # Arbeitsebene XYZ anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2000, 652)  # Fokussieren Klick
        sleep(self.verweilzeit)  # self.verweilzeit

    def z_verschieben(self):
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2000, 652)  # Fokussieren Klick
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.hotkey('ctrl', 'a')  # Alles markieren im Solid- und Rohteilmitnahme Layer
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.rightClick(2070, 599)  # Rechtsklick für Kontextmenü
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2158, 609)  # Modifizieren im Kontextmenü klicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2943, 400)  # Modifizieren fokussieren
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.press("v")  # Verschieben mit "v" anwählen
        sleep(self.verweilzeit)  # self.verweilzeit

        pag.click(2756, 470)  # Original modifizieren Haken anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2755, 539)  # Haken neben dem XYZ anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.press('tab')  # Tabulator
        sleep(0.05)  # self.verweilzeit
        pag.typewrite("0")  # "0" in X eingeben
        sleep(0.05)  # self.verweilzeit
        pag.press('tab')  # Tabulator
        sleep(0.05)  # self.verweilzeit
        pag.typewrite("0")  # "0" in Y eingeben
        sleep(0.05)  # self.verweilzeit
        pag.press('tab')  # Tabulator
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.typewrite(str(self.z_fertig))  # Fertigteilhöhe in Z eingeben
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2840, 625)  # Verschieben mit Mausklick auf "OK" bestätigen
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit

    def feature_symmetrie(self):
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2197, 728)  # Klick auf "Alles auswählen"
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(1995, 697)  # Alle Layer einblenden (Haken Standard)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2481, 68)  # Nur Feature Auswahl anklicken (aufklappen)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2477, 119)  # Nur Feature anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2000, 652)  # Fokussieren Klick
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.hotkey('ctrl', 'a')  # Alle Feature markieren
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.rightClick(2070, 599)  # Rechtsklick für Kontextmenü
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2158, 609)  # Modifizieren im Kontextmenü klicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2943, 400)  # Modifizieren fokussieren
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.press("s")  # Symmetrie mit "s" anwählen
        sleep(0.1)  # self.verweilzeit
        pag.press("y")  # Symmetrie mit "y" anwählen
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2756, 470)  # Original modifizieren Haken anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2755, 562)  # Haken neben dem Y Achse anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2840, 625)  # Verschieben mit Mausklick auf "OK" bestätigen
        sleep(5)  # self.verweilzeit 5 sec
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2879, 489)  # Klick auf Fehlermeldung (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2997, 569)  # Klick auf Fehlermeldung "OK"
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit

    def konturzug_links(self):
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2481, 68)  # Nur Feature Auswahl anklicken (aufklappen)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2477, 237)  # Nur Konturzüge anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2047, 699)  # Klick auf Standard um Markierung aufzuheben
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2000, 652)  # Fokussieren Klick
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.hotkey('ctrl', 'a')  # Alle Feature markieren
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(1124, 211)  # Klick in Eigenschaften auf Bearbeitungsseite
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.press("l")  # Mit "L" auf Links setzen
        sleep(0.5)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2481, 68)  # Nur Feature Auswahl anklicken (aufklappen)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2472, 88)  # Alles auswählen
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit

    def xy_verschieben(self):
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2000, 652)  # Fokussieren Klick
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.hotkey('ctrl', 'a')  # Alles markieren
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.rightClick(2070, 599)  # Rechtsklick für Kontextmenü
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2158, 609)  # Modifizieren im Kontextmenü klicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2943, 400)  # Modifizieren fokussieren
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.press("v")  # Verschieben mit "v" anwählen
        sleep(0.1)  # self.verweilzeit
        pag.click(2756, 470)  # Original modifizieren Haken anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2755, 539)  # Haken neben dem XYZ anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        x_verschiebung = float(self.x_fertig)
        y_verschiebung = float(self.y_fertig)
        pag.press('tab')  # Tabulator
        pag.typewrite(str(-x_verschiebung / 2))
        pag.press('tab')
        pag.typewrite(str(-y_verschiebung / 2))
        pag.press('tab')
        pag.typewrite(str("0"))
        pag.press('tab')

        pag.click(2840, 625)  # Verschieben mit Mausklick auf "OK" bestätigen
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(5)  # self.verweilzeit 5 sec

    def solid_aktualisieren(self):
        pag.doubleClick(2109, 668)  # Doppelklick auf Layer
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2000, 652)  # Fokussieren Klick
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2246, 96)  # Simulationsparameter
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2071, 192)  # Klick auf Bauteil
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2064, 230)  # Klick auf Rohteil
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2425, 574)  # Aktualisieren
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2064, 247)  # Fertigteil anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2425, 574)  # Aktualisieren
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2333, 618)  # OK Klicken

    def zusammenfassung_funktionen(self):
        """Eine Zusammenfassung folgender Funktionen: 1. rohteilmitnahme, 2. rotieren, 3. z_verschieben,
        4. feature_symmetrie, 5. konturzug_links, 6. xy_verschieben, 7. solid_aktualisieren"""
        self.rohteilmitnahme()
        self.rotieren()
        self.z_verschieben()
        self.feature_symmetrie()
        self.konturzug_links()
        self.xy_verschieben()
        self.solid_aktualisieren()

    def allmatic_125(self):
        pag.doubleClick(2109, 668) # Doppelklick auf Layer
        sleep(self.verweilzeit)
        pag.click(2000, 652) # Fokussieren Klick
        sleep(self.verweilzeit)
        pag.click(2197, 728) # Klick auf "Alles auswählen"
        sleep(self.verweilzeit)
        pag.click(1996, 697) # Alle Layer ausblenden (Haken)
        sleep(self.verweilzeit)
        pag.doubleClick(2038, 827) # Doppelklick auf Müll Layer

        ###########################################################
        # Hier muss eine Abfrage mit einer Msg-Box programmiert werden!!!

        spanntiefe = int(self.spanntiefe) # Spanntiefe in integer umwandeln

        if spanntiefe >= 40:
            pfad = str(f"{self.PFAD_DIR_ALLMATIC_125}{40}.step")
        else:
            # Sicherstellen, dass spanntiefe nicht negativ ist (optional)
            spanntiefe = max(0, spanntiefe)
            pfad = str(f"{self.PFAD_DIR_ALLMATIC_125}{spanntiefe}.step")

        print(f"Öffne Pfad: {pfad}") # Zum Debuggen
        pag.click(1973, 63) # Öffnen Allmatic.Step
        sleep(self.verweilzeit) # Verweilzeit
        pag.click(2853, 795) # Koordinaten vom Pfad im Öffnen Fenster
        sleep(self.verweilzeit) # Verweilzeit
        clipboard.copy(pfad)
        sleep(self.verweilzeit)
        pag.hotkey("ctrl", "v")
        sleep(self.verweilzeit)
        pag.click(3151, 793) # Öffnen Allmatic.Step
        sleep(2) # Längere self.verweilzeit nach dem Öffnen

    # Für zukünftige Automatisierung → Prüft ob der NP auf der B-Seite stimmt
    def nullpunkt_pruefen(self):
        pass

    def run(self):
        """Hauptmethode des Workers, die beim Start des Threads ausgeführt wird."""
        try:
            self.automations_typ_bestimmen_b()
        except Exception as e:
            # Bei einem Fehler, sende ein Fehlersignal mit der Fehlermeldung
            error_message = f"Ein unerwarteter Fehler ist aufgetreten: {e}"
            self.status_update.emit(error_message)
            self.show_info_dialog.emit("Kritischer Fehler", error_message)
            self.finished.emit(False, error_message)
            print(f"[FEHLER] im EspritA Worker: {e}")