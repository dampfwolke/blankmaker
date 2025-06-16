from pathlib import Path
from time import sleep
import re

from PySide6.QtCore import QObject, Signal, QMutex, QWaitCondition, QThread
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

    # NEUES Signal, um den Dialog vom Haupt-Thread anzufordern
    # Signal(str, str) -> sendet Titel und Text für den Dialog
    confirmation_required = Signal(str, str)

    # Konstante Pfade für Rohteilmitnahme und Allmatic 125 Schraubstock
    PFAD_ROHTEILMITNAHME = Path(r"C:\Users\hasanovic\Desktop\Rohteilmitnahme\Hasanovic")
    PFAD_DIR_ALLMATIC_125 = Path(r"C:\Users\hasanovic\Desktop\Spannmittel\19_Allmatic_125_EVO_100")

    def __init__(self, pgm_name: str, typ: str, pfad: Path, sleep_timer: int, x_fertig: str, y_fertig: str, z_fertig: str, spanntiefe: str):
        super().__init__()
        self.pgm_name = pgm_name
        self.typ = typ
        self.pfad = pfad
        self.sleep_timer = sleep_timer
        self.x_fertig = x_fertig
        self.y_fertig = y_fertig
        self.z_fertig = z_fertig
        self.spanntiefe = spanntiefe
        # Verzögerung zwischen den Aktionen (min. 0.081s, max. 3.175s) je nach QSlider Einstellung im main script
        self.verweilzeit: float = round(0.1 + (self.sleep_timer / 32), 2)

        # NEU: Synchronisationsobjekte für das Warten auf den Dialog
        self.mutex = QMutex()
        self.wait_condition = QWaitCondition()
        self.confirmation_result = False # Hier wird das Ergebnis gespeichert


    def automations_typ_bestimmen_b(self):
        """ Hier wird entschieden welche Autoaktionsabschnitte ausgeführt werden z.B. nur Ausfüllhilfe oder vollständig etc.
        abhängig von dem übergebenen Wert aus der "cb_bearbeitung_auswahl_b" im main script.
        :return: None """
        if self.typ == "Saruman":
            self.esprit_dateiname_pruefen_b()
            self.status_update.emit("Starte 'Saruman'")
            self.esprit_a_sicherung_speichern_b()
            self.ausfuellhilfe_b()
            self.esprit_datei_speichern_b()
            self.zusammenfassung_funktionen()
            # --- HIER KOMMT DIE NEUE LOGIK ---
            self.status_update.emit("Warte auf Bestätigung für Allmatic 125...")
            # 1. Signal senden, um den Dialog anzufordern
            self.confirmation_required.emit(
                "Bestätigung erforderlich",
                "Soll die Allmatic 125 Spannsituation eingefügt werden?")
            # 2. Mutex sperren und auf das Signal vom Haupt-Thread warten
            self.mutex.lock()
            self.wait_condition.wait(self.mutex)
            self.mutex.unlock()
            # 3. Nach dem Aufwecken das Ergebnis prüfen
            if self.confirmation_result:
                self.status_update.emit("Bestätigung erhalten. Füge Allmatic 125 ein.")
                self.allmatic_125() # Hier deine Funktion aufrufen
            else:
                self.status_update.emit("Allmatic 125 wurde übersprungen.")
            # --- ENDE DER NEUEN LOGIK ---
            self.abgeschlossen_b()

        elif self.typ == "Saruman light":
            self.esprit_dateiname_pruefen_b()
            self.status_update.emit("Starte 'Saruman light'")
            self.esprit_a_sicherung_speichern_b()
            self.ausfuellhilfe_b()
            self.esprit_datei_speichern_b()
            self.rohteilmitnahme()
            self.rotieren()
            self.z_verschieben()
            self.abgeschlossen_b()

        elif self.typ == "Ausfüllhilfe B":
            self.status_update.emit("Starte 'Ausfüllhilfe_B'")
            self.esprit_a_sicherung_speichern_b()
            self.ausfuellhilfe_b()
            self.esprit_datei_speichern_b()
            self.abgeschlossen_b()

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

    def set_confirmation_result(self, result: bool):
        """
        Diese Methode wird vom HAUPT-THREAD aufgerufen, um das Ergebnis zu setzen
        und den wartenden Worker-Thread aufzuwecken.
        """
        self.mutex.lock()
        self.confirmation_result = result
        self.wait_condition.wakeAll() # Weckt den wartenden Thread auf
        self.mutex.unlock()


    def esprit_a_sicherung_speichern_b(self) -> None:
        '''Speichert noch einmal die A-Seite zur Sicherheit ab, bevor Automation für B-Seite beginnt.'''
        self.status_update.emit("A-Seite wird gespeichert...")
        pag.doubleClick(2109, 668)            # Doppelklick auf Layer
        sleep(self.verweilzeit)                     # Verweilzeit
        pag.click(2109, 668)                  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)                     # Verweilzeit
        pag.hotkey('ctrl', 's')               # A-Seite speichern
        sleep(4)                                    # Verweilzeit
        pag.doubleClick(2109, 668)            # Doppelklick auf Layer
        # sleep(self.verweilzeit)                     # Verweilzeit
        # pag.click(2109, 668)                  # Klick auf Layer (Fokussieren)
        # sleep(self.verweilzeit)                     # Verweilzeit
        # pag.click(2197, 728)                  # Klick auf "Alles auswählen"
        # sleep(self.verweilzeit)                     # Verweilzeit
        # pag.click(2000, 698)                  # Alle Layer ausblenden (Haken)
        # sleep(self.verweilzeit)                     # Verweilzeit
        # pag.doubleClick(2038, 713)            # Doppelklick auf Solid Layer

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
        self.finished.emit(True, f"'{self.typ}' abgeschlossen.")

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
        self.status_update.emit("Klicke von Ansicht oben...")
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
        self.status_update.emit("Klicke von Ansicht isometrisch...")
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2904, 67)  # Arbeitsebenen
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2904, 118)  # Arbeitsebene Isometrisch
        sleep(verweilzeit)  # Verweilzeit
        pag.click(2175, 294)  # Fertigteil Pfeil anklicken
        sleep(verweilzeit)  # Verweilzeit
        self.status_update.emit("Rohteilmitnahme wird als Bauteil definiert...")
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
        self.status_update.emit("Beginne mit Rotation...")
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
        self.status_update.emit("Teil wird um 180° rotiert...")
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
        self.status_update.emit("Arbeitsebene wird wieder auf XYZ gesetzt...")
        pag.click(2684, 102)  # Arbeitsebene XYZ anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2000, 652)  # Fokussieren Klick
        sleep(self.verweilzeit)  # self.verweilzeit

    def z_verschieben(self):
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        self.status_update.emit("Beginne mit Z-Verschiebung..")
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2000, 652)  # Fokussieren Klick
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.hotkey('ctrl', 'a')  # Alles markieren im Solid- und Rohteilmitnahme Layer
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.rightClick(2070, 599)  # Rechtsklick für Kontextmenü
        self.status_update.emit("Z-Verschiebung Wert in mm wird eingetragen..")
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
        sleep(1)

    def feature_symmetrie(self):
        self.status_update.emit("Beginne mit Feature symmetrieren..")
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2197, 728)  # Klick auf "Alles auswählen"
        self.status_update.emit("Alle Layer werden eingeblendet..")
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(1995, 697)  # Alle Layer einblenden (Haken Standard)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2481, 68)  # Nur Feature Auswahl anklicken (aufklappen)
        self.status_update.emit("Nur Feature wird ausgewählt...")
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2477, 119)  # Nur Feature anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2000, 652)  # Fokussieren Klick
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.hotkey('ctrl', 'a')  # Alle Feature markieren
        sleep(self.verweilzeit)  # self.verweilzeit
        self.status_update.emit("Feature symmetriert..")
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
        self.status_update.emit("Warte bis Esprit fertig ist mit rechnen :D ...")
        sleep(5)  # self.verweilzeit 5 sec
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        self.status_update.emit("Fehlermeldung wird weggeklickt...")
        pag.click(2879, 489)  # Klick auf Fehlermeldung (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2997, 569)  # Klick auf Fehlermeldung "OK"
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit

    def konturzug_links(self):
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        self.status_update.emit("Konturzüge werden auf links gesetzt..")
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2481, 68)  # Nur Feature Auswahl anklicken (aufklappen)
        sleep(self.verweilzeit)  # self.verweilzeit
        self.status_update.emit("Nur Feature wird ausgewählt...")
        pag.click(2477, 237)  # Nur Konturzüge anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2047, 699)  # Klick auf Standard um Markierung aufzuheben
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2000, 652)  # Fokussieren Klick
        sleep(self.verweilzeit)  # self.verweilzeit
        self.status_update.emit("Alle Feature werden markiert...")
        pag.hotkey('ctrl', 'a')  # Alle Feature markieren
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(1124, 211)  # Klick in Eigenschaften auf Bearbeitungsseite
        self.status_update.emit("Bearbeitunsseite wird auf links gesetzt...")
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
        self.status_update.emit("Beginne mit XY-Verschiebung...")
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
        self.status_update.emit("Verschieben wird ausgewählt...")
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.press("v")  # Verschieben mit "v" anwählen
        sleep(0.1)  # self.verweilzeit
        pag.click(2756, 470)  # Original modifizieren Haken anklicken
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2755, 539)  # Haken neben dem XYZ anklicken
        self.status_update.emit("Werte werden eingetragen...")
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
        self.status_update.emit("Beginne Aktualisierung der Bauteile...")
        pag.doubleClick(2109, 668)  # Doppelklick auf Layer
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2109, 668)  # Klick auf Layer (Fokussieren)
        sleep(self.verweilzeit)  # self.verweilzeit
        pag.click(2000, 652)  # Fokussieren Klick
        sleep(self.verweilzeit)  # self.verweilzeit
        self.status_update.emit("Simulationsbauteile werden aktualisiert...")
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
            pfad = str(f"{self.PFAD_DIR_ALLMATIC_125}\\{40}.step")
        else:
            # Sicherstellen, dass spanntiefe nicht negativ ist (optional)
            spanntiefe = max(0, spanntiefe)
            pfad = str(f"{self.PFAD_DIR_ALLMATIC_125}\\{spanntiefe}.step")

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