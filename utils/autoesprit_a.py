from pathlib import Path
from time import sleep
import re

from PySide6.QtCore import QObject, Signal, QThread
import pyautogui as pag
import clipboard

from utils.click_image import click_image
from utils.zeitstempel import zeitstempel


class EspritA(QObject):
    # Signal(str) -> sendet eine Statusmeldung als Text
    status_update = Signal(str)
    # Signal(str, str) -> sendet Titel und Text für eine Informations-MessageBox
    show_info_dialog = Signal(str, str)
    # Signal(bool, str) -> sendet Beendigungsstatus (Erfolg/Fehler) und eine finale Nachricht
    finished = Signal(bool, str)
    # Signal Fertigteil Abmasse X Y Z ausgelesen
    ausgelesene_fertig_werte = Signal(str, str, str)

    def __init__(self, pgm_name: str, x_roh: str, y_roh: str, z_roh: str, pfad: Path, bearbeitung_auswahl: str,
                 typ: str,
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

        # Verzögerung zwischen den Aktionen (min. 0.2s, max. 10.2s) je nach QSlider Einstellung im main script
        self.verweilzeit: float = round(0.1 + (self.sleep_timer / 20), 2)

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

    def abgeschlossen(self) -> None:
        """Sendet das finale Erfolgssignal."""
        self.finished.emit(True, f"Automatisierung '{self.typ}' erfolgreich abgeschlossen.")

    def automations_typ_bestimmen(self) -> None:
        """ Hier wird entschieden welche Autoaktionsabschnitte ausgeführt werden z.B. nur Ausfüllhilfe oder vollständig etc.
        abhängig von dem übergebenen Wert aus der "cb_bearbeitung_auswahl" im main script.
        :return: None """
        if self.typ == "Ausfüllhilfe":
            self.status_update.emit("Starte 'Ausfüllhilfe'")
            self.ausfuellhilfe_a()
            self.abgeschlossen()

        elif self.typ == "Gandalf":
            self.status_update.emit("Starte Automatisierung mit 'Gandalf'")
            erfolg, msg = self.roh_abmasse_pruefen()
            if not erfolg:
                self.show_info_dialog.emit("Ungültige Eingabe", msg)
                self.finished.emit(False, "Abbruch wegen ungültiger Rohteilabmaße.")
                return
            erfolg, msg = self.esprit_dateiname_pruefen()
            if not erfolg:
                self.show_info_dialog.emit("Dateifehler", msg)
                self.finished.emit(False, "Abbruch wegen Dateikonflikt.")
                return
            # Aktionen durchführen
            self.ausfuellhilfe_a()
            self.esprit_datei_speichern()
            # Fertigteilmaße auslesen und prüfen
            self.fertigteil_bounding_box_auslesen()
            erfolg, msg = self.fertig_abmasse_pruefen()
            if not erfolg:
                self.show_info_dialog.emit("Fehler beim Auslesen", msg)
                self.finished.emit(False, "Abbruch: Fertigteilmaße konnten nicht validiert werden.")
                return
            # Aufmaß vergleichen
            erfolg, msg = self.fertig_und_rohmasse_vergleichen()
            if not erfolg:
                self.show_info_dialog.emit("Fehler im Aufmaß", msg)
                self.finished.emit(False, "Abbruch: Aufmaß außerhalb der Toleranzen.")
                return

            # Restliche Aktionen
            self.esprit_datei_speichern()
            self.rohteil_erstellen()
            self.spannmittel_importieren()
            self.abgeschlossen()

        elif self.typ == "Bounding Box auslesen":
            self.fertigteil_bounding_box_auslesen()
            erfolg, msg = self.fertig_abmasse_pruefen()
            if not erfolg:
                self.show_info_dialog.emit("Fehler beim Auslesen der Bounding Box", msg)
                self.finished.emit(False, "Fehler beim Validieren der Bounding Box.")
                return
            self.fertig_abmasse_eintragen()
            self.abgeschlossen()

        elif self.typ == "Platzhalter":
            # Hier deine Logik für den Platzhalter-Typ einfügen
            self.status_update.emit("Platzhalter-Funktion wurde aufgerufen.")
            self.finished.emit(True, "Platzhalter-Funktion beendet.")
            pass  # Platzhalter für Testfunktionen

        else:
            error_msg = "Kein gültiger 'automations_typ' ausgewählt!"
            self.status_update.emit(error_msg)
            self.show_info_dialog.emit("Auswahlfehler", error_msg)
            self.finished.emit(False, error_msg)

    def roh_abmasse_pruefen(self) -> tuple[bool, str]:
        """ Prüfung ob Rohteilmaße gültig sind. :return: (bool, str)"""
        try:
            if float(self.x_roh) > 0 and float(self.y_roh) > 0 and float(self.z_roh) > 0:
                return True, ""
            else:
                msg = "Rohteilabmaße müssen größer als 0 sein."
                self.status_update.emit(f"Fehler: {msg}")
                return False, msg
        except (ValueError, TypeError):
            msg = "Rohteilabmaße sind keine gültigen Zahlen."
            self.status_update.emit(f"Fehler: {msg}")
            return False, msg

    def fertigteil_bounding_box_auslesen(self) -> None:
        """Mithilfe von pyautogui und Hilfsmodul click_image wird in Esprit die Bounding Box des aktuellen Bauteils ausgelesen."""
        self.status_update.emit("Starte Fertigteilmaß auslesen....")
        bild_pfad_relativ = Path(".") / "utils" / "automation_bilder" / "bauteil.png"
        bild_pfad_absolut = bild_pfad_relativ.resolve()
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

    def fertig_abmasse_pruefen(self) -> tuple[bool, str]:
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

    def fertig_und_rohmasse_vergleichen(self) -> tuple[bool, str]:
        """ Prüfung ob Rohteil Aufmaß für Fertigteil hat und ob der Rohteil nicht zu groß ist.
        :return: (bool, str)"""
        try:
            x_r, y_r, z_r = float(self.x_roh), float(self.y_roh), float(self.z_roh)
            x_f, y_f, z_f = float(self.x_fertig), float(self.y_fertig), float(self.z_fertig)

            aufmass_x, aufmass_y, aufmass_z = x_r - x_f, y_r - y_f, z_r - z_f

            fehler_liste = []
            if aufmass_x < 1.5: fehler_liste.append(f"• X-Aufmaß zu gering ({aufmass_x:.2f}mm < 1.5mm)")
            if aufmass_y < 0.6: fehler_liste.append(f"• Y-Aufmaß zu gering ({aufmass_y:.2f}mm < 0.6mm)")
            if aufmass_z < 4.5: fehler_liste.append(f"• Z-Aufmaß zu gering ({aufmass_z:.2f}mm < 4.5mm)")
            if aufmass_x > 11.0: fehler_liste.append(f"• X-Aufmaß zu groß ({aufmass_x:.2f}mm > 11mm)")
            if aufmass_y > 14.0: fehler_liste.append(f"• Y-Aufmaß zu groß ({aufmass_y:.2f}mm > 14mm)")
            if aufmass_z > 25.0: fehler_liste.append(f"• Z-Aufmaß zu groß ({aufmass_z:.2f}mm > 25mm)")

            if fehler_liste:
                fehler_nachricht = "Die Aufmaße liegen außerhalb der Toleranzen:\n\n" + "\n".join(fehler_liste)
                self.status_update.emit("Fehler im Aufmaß festgestellt. Abbruch.")
                return False, fehler_nachricht
            else:
                self.status_update.emit("Aufmaße sind innerhalb der Toleranzen.")
                return True, ""
        except (ValueError, TypeError):
            error_msg = "Fehler: Konnte Roh- oder Fertigmaße für den Vergleich nicht in Zahlen umwandeln."
            self.status_update.emit(error_msg)
            return False, error_msg

    def fertig_abmasse_eintragen(self) -> None:
        '''Trägt die ausgelesenen Abmasse ins Hauptprogramm in die entsprechenden lineedits ein.'''
        x = str(self.x_fertig)
        y = str(self.y_fertig)
        z = str(self.z_fertig)
        self.ausgelesene_fertig_werte.emit(x, y, z)

    def esprit_dateiname_pruefen(self) -> tuple[bool, str]:
        """ Prüfung, ob der Pfad existiert und ob eine Datei mit demselben Namen bereits im Ordner ist.
         :return: (bool, str)"""
        if not self.pfad.is_dir():
            error_msg = f"Fehler: Der angegebene Pfad '{self.pfad}' existiert nicht oder ist kein Ordner."
            self.status_update.emit(error_msg)
            return False, error_msg

        dateiname_mit_endung = f"{self.pgm_name}_A.esp"
        zieldatei_pfad = self.pfad / dateiname_mit_endung

        if zieldatei_pfad.exists():
            error_msg = f"Die Datei '{dateiname_mit_endung}' existiert bereits im Zielordner."
            self.status_update.emit(f"Abbruch: {error_msg}")
            return False, error_msg

        self.status_update.emit("Dateiname und Pfad sind gültig.")
        return True, ""

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
        pgm_name_mit_endung = f"{self.pgm_name}_A".strip()
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
        clipboard.copy(self.bearbeitung_auswahl)
        sleep(0.1)
        pag.hotkey("ctrl", "v")
        sleep(verweilzeit)
        pag.press('Enter')
        sleep(verweilzeit)
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
        pag.doubleClick(2109, 668)
        sleep(self.verweilzeit)
        pag.click(1973, 63)
        sleep(self.verweilzeit)
        pag.click(2853, 795)
        sleep(self.verweilzeit)
        self.status_update.emit("Rohteil DXF wird importiert...")
        pfad_rohteil = self.pfad / "!rohteil.dxf"
        clipboard.copy(str(pfad_rohteil))
        sleep(0.1)
        pag.hotkey("ctrl", "v")
        pag.click(3151, 793)
        sleep(self.verweilzeit)
        self.status_update.emit(f"Rohteil DXF eingefügt!  {zeitstempel(1)}")
        pag.click(2914, 66)
        sleep(self.verweilzeit)
        pag.click(2900, 133)
        sleep(self.verweilzeit)
        pag.click(2109, 668)
        sleep(self.verweilzeit)
        self.status_update.emit("Rohteilabmaße werden eingetragen....")
        pag.click(2246, 96)
        sleep(self.verweilzeit)
        pag.click(2071, 192)
        sleep(self.verweilzeit)
        pag.doubleClick(2231, 293)
        sleep(self.verweilzeit)

        length, width, height = float(self.x_roh), float(self.y_roh), float(self.z_roh)

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
        sleep(self.verweilzeit)
        pag.click(2425, 574)
        sleep(self.verweilzeit)
        pag.click(2064, 247)
        sleep(self.verweilzeit)
        pag.click(2175, 294)
        sleep(self.verweilzeit)
        pag.click(2900, 631)
        sleep(self.verweilzeit)
        pag.click(2900, 631)
        sleep(self.verweilzeit)
        pag.click(2425, 574)
        sleep(self.verweilzeit)
        pag.click(2904, 67)
        sleep(self.verweilzeit)
        pag.click(2904, 102)
        sleep(self.verweilzeit)
        pag.click(2175, 294)
        sleep(self.verweilzeit)
        pag.click(2900, 631)
        sleep(self.verweilzeit)
        pag.click(2900, 631)
        sleep(self.verweilzeit)
        pag.click(2425, 574)
        sleep(self.verweilzeit)
        pag.click(2904, 67)
        sleep(self.verweilzeit)
        pag.click(2904, 118)
        sleep(self.verweilzeit)
        pag.click(2175, 294)
        sleep(self.verweilzeit)
        pag.click(2900, 631)
        sleep(self.verweilzeit)
        pag.click(2900, 631)
        sleep(self.verweilzeit)
        pag.click(2425, 574)
        sleep(self.verweilzeit)
        pag.click(2333, 618)

        self.status_update.emit(f"Simulationsbauteile erstellt!   {zeitstempel(1)}")

    def spannmittel_importieren(self) -> None:
        """Spannmittel wird aus dem aktuellen KW-Wochen Ordner, in Esprit importiert und die Automatisierung abgeschlossen."""
        self.status_update.emit(f"Spannmittel Import gestartet.  {zeitstempel(1)}")
        sleep(self.verweilzeit)
        pag.click(2109, 668)
        sleep(self.verweilzeit)
        self.status_update.emit("Layer werden ausgeblendet...")
        pag.click(1995, 713)
        sleep(self.verweilzeit)
        pag.click(1995, 729)
        sleep(self.verweilzeit)
        pag.doubleClick(2038, 827)
        sleep(self.verweilzeit)
        self.status_update.emit("Schraubstock wird geöffnet...")
        pag.click(1973, 63)
        sleep(self.verweilzeit)
        pag.click(2853, 795)
        sleep(self.verweilzeit)

        pfad_schraubstock = self.pfad / "!schraubstock.step"
        clipboard.copy(str(pfad_schraubstock))
        sleep(0.1)
        pag.hotkey("ctrl", "v")
        pag.click(3151, 793)
        sleep(10)  # Längere Wartezeit für STEP-Datei-Import
        self.status_update.emit(f"Schraubstock erfolgreich importiert.  {zeitstempel(1)}")
        pag.click(2109, 640)
        sleep(self.verweilzeit)
        self.status_update.emit("Schraubstock wird als Spannmittel definiert...")
        pag.hotkey('ctrl', 'a')
        sleep(self.verweilzeit)
        pag.click(2373, 126)
        sleep(self.verweilzeit)
        pag.click(2766, 659)
        pag.click(2109, 640)
        sleep(self.verweilzeit)
        pag.click(1995, 825)
        sleep(0.2)
        self.status_update.emit("Layer werden wieder eingeblendet...")
        pag.click(1995, 713)
        sleep(0.2)
        pag.click(1995, 729)
        sleep(0.2)
        pag.doubleClick(2038, 745)
        sleep(0.2)
        pag.click(2246, 96)
        sleep(self.verweilzeit)
        self.status_update.emit(f"Automatisierung abgeschlossen! {zeitstempel(1)}")
        # Der finale 'finished'-Aufruf wird jetzt in `automations_typ_bestimmen` gemacht.

    def run(self):
        """Hauptmethode des Workers, die beim Start des Threads ausgeführt wird."""
        try:
            self.automations_typ_bestimmen()
        except Exception as e:
            # Bei einem Fehler, sende ein Fehlersignal mit der Fehlermeldung
            error_message = f"Ein unerwarteter Fehler ist aufgetreten: {e}"
            self.status_update.emit(error_message)
            self.show_info_dialog.emit("Kritischer Fehler", error_message)
            self.finished.emit(False, error_message)
            print(f"[FEHLER] im EspritA Worker: {e}")