from pathlib import Path
from time import sleep
import re

from PySide6.QtCore import QObject, Signal
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

    def abgeschlossen(self) ->None:
        self.finished.emit(True, f"{self.typ} erfolgreich abgeschlossen.")

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
            self.ausfuellhilfe_a()
            if not self.fertig_abmasse_pruefen():
                self.fertigteil_bounding_box_auslesen()
                print(f"FEHLER beim auslesen der Bounding Box!!!")
                return
            if not self.esprit_dateiname_pruefen():
                print(f"FEHLER! Datei {self.pgm_name}_A existiert bereits!!!")
                return
            self.esprit_datei_speichern()
            if not self.roh_abmasse_pruefen():
                print(f"FEHLER! Rohteil Maß passt nicht!")
                return
            self.rohteil_erstellen()
            self.spannmittel_importieren()
            self.abgeschlossen()
        elif self.typ == "Bounding Box auslesen":
            self.fertigteil_bounding_box_auslesen()
            self.abgeschlossen()
            # Platzhalter für Testfunktionen
        elif self.typ == "Platzhalter":
            self.fertig_abmasse_eintragen()
            self.status_update.emit("Starte Automatisierung mit 'Bounding Box auslesen'")
            self.ausfuellhilfe_a()
            self.esprit_datei_speichern()
            self.rohteil_erstellen()
            self.spannmittel_importieren()
            self.abgeschlossen()
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

    def fertigteil_bounding_box_auslesen(self) -> None:
        """Mithilfe von pyautogui und Hilfsmodul click_image wird in Esprit die Bounding Box des aktuellen Bauteils ausgelesen."""
        self.status_update.emit("Starte Fertigteilmaß auslesen....")
        bild_pfad_relavtiv = Path(".") / "utils" / "automation_bilder" / "bauteil.png"
        bild_pfad_absolut = bild_pfad_relavtiv.resolve()
        verweilzeit = self.verweilzeit         # festlegen der Sleep Zeit
        pag.doubleClick(2109, 668)            # Doppelklick auf Layer
        sleep(verweilzeit)                     # Verweilzeit
        pag.click(2109, 668)                  # Klick auf Layer (Fokussieren)
        sleep(verweilzeit)                     # Verweilzeit
        pag.doubleClick(2038, 713)            # Doppelklick auf Solid Layer
        sleep(verweilzeit)                     # Verweilzeit
        self.status_update.emit("Fertigteilmaß wird ausgelesen...")
        pag.click(2481, 68)                   # Nur Volumenmodell Auswahl anklicken (aufklappen)
        sleep(verweilzeit)                     # Verweilzeit
        pag.click(2480, 434)                  # Nur Volumenmodell auswählen
        sleep(verweilzeit)                     # Verweilzeit
        pag.click(2109, 668)                  # Klick auf Layer (Fokussieren)
        sleep(verweilzeit)                     # Verweilzeit
        pag.click(2109, 640)                  # Fokussieren Klick
        sleep(verweilzeit)                     # Verweilzeit
        pag.hotkey('ctrl', 'a')               # Alles markieren (Solid)
        sleep(verweilzeit)                     # Verweilzeit
        click_image(str(bild_pfad_absolut), toleranz=0.65)  # Auf Bauteil Reiter klicken mit Bilderkennung
        self.status_update.emit("Reiter Bauteil gefunden...")
        sleep(verweilzeit)                     # Verweilzeit
        pag.click(1291, 47)                   # Auf Erkunden Reiter im Bauteil Menü klicken
        self.status_update.emit("Abmaße werden in Zwischenspeicher kopiert...")
        sleep(verweilzeit)                     # Verweilzeit
        pag.doubleClick(1669, 331)            # Doppelklick auf Länge des Bauteils
        sleep(verweilzeit)                     # Verweilzeit
        pag.hotkey('ctrl', 'c')               # Abmaße des Fertigteils kopieren
        sleep(verweilzeit)                     # Verweilzeit
        pag.click(2481, 68)                   # Nur Volmenmodell Auswahl anklicken (aufklappen)
        sleep(verweilzeit)                     # Verweilzeit
        pag.click(2472, 88)                   # Alles auswählen
        sleep(verweilzeit)                     # Verweilzeit
        pag.click(2109, 668)                  # Klick auf Layer (Fokussieren)
        sleep(verweilzeit)                     # Verweilzeit
        pag.click(2109, 640)                  # Fokussieren Klick
        sleep(verweilzeit)                     # Verweilzeit
        pag.click(1308, 1009)                 # Auf Feature im Projekt-Manager klicken
        sleep(verweilzeit)                     # Verweilzeit
        pag.doubleClick(2038, 697)            # Doppelklick auf Standard Layer
        clipboard_content = clipboard.paste()
        string = clipboard_content.strip("()")
        string = re.sub(r'(\d+),(\d+)', r'\1.\2', string)
        abmasse = string.split(', ')
        self.x_fertig = abmasse[0]
        self.y_fertig = abmasse[1]
        self.z_fertig = abmasse[2]
        self.status_update.emit(f"X={self.x_fertig}, Y={self.y_fertig}, Z={self.z_fertig}")
        print(self.x_fertig, self.y_fertig, self.z_fertig)
        self.finished.emit(True, "Fertigteilmaß ausgelesen erfolgreich abgeschlossen.")


    def fertig_abmasse_pruefen(self) -> bool:
        """
        Es wird geprüft, ob die Fertigteilmaße korrekt ausgelesen wurden.
        :return: bool
        """
        try:
            # Prüfen, ob die Werte überhaupt gesetzt wurden (nicht mehr None sind)
            if self.x_fertig is None or self.y_fertig is None or self.z_fertig is None:
                self.status_update.emit("Fehler: Fertigteilmaße wurden nicht ausgelesen.")
                return False

            # Versuchen, die Werte in Fließkommazahlen umzuwandeln
            x_f = float(self.x_fertig)
            y_f = float(self.y_fertig)
            z_f = float(self.z_fertig)

            # Prüfen, ob die Abmaße physikalisch sinnvoll sind (größer als 0)
            if x_f > 0 and y_f > 0 and z_f > 0:
                self.status_update.emit("Fertigteilmaße erfolgreich validiert.")
                return True
            else:
                self.status_update.emit("Fehler: Fertigteilmaße müssen größer als 0 sein.")
                return False
        except (ValueError, TypeError):
            # Dieser Fehler tritt auf, wenn die Umwandlung zu float fehlschlägt
            self.status_update.emit("Fehler: Ausgelesene Fertigteilmaße sind keine gültigen Zahlen.")
            return False

    def fertig_und_rohmasse_vergleichen(self) -> bool:
        """ Prüfung ob Rohteil in X > 1.5mm, in Y > 0.6mm, Z > 4.5mm Aufmaß für Fertigteil hat.
        Es wird auch geprüft, ob der Rohteil nicht zu viel größer als der Fertigteil ist. Hier gelten folgende Regeln:
        Aufmaß in X darf nicht größer als 11mm sein.
        Aufmaß in Y darf nicht größer als 14mm sein.
        Aufmaß in Z darf nicht größer als 25mm sein.
        :return: bool"""
        try:
            # Konvertiere alle relevanten Maße in Fließkommazahlen
            x_r = float(self.x_roh)
            y_r = float(self.y_roh)
            z_r = float(self.z_roh)
            x_f = float(self.x_fertig)
            y_f = float(self.y_fertig)
            z_f = float(self.z_fertig)

            # Berechne das Aufmaß (Differenz zwischen Roh- und Fertigteil)
            aufmass_x = x_r - x_f
            aufmass_y = y_r - y_f
            aufmass_z = z_r - z_f

            # Sammle alle Fehler, um eine umfassende Rückmeldung zu geben
            fehler_liste = []

            # 1. Prüfung: Mindestaufmaß
            if aufmass_x < 1.5:
                fehler_liste.append(f"X-Aufmaß ist {aufmass_x:.2f}mm, muss aber min. 1.5mm sein.")
            if aufmass_y < 0.6:
                fehler_liste.append(f"Y-Aufmaß ist {aufmass_y:.2f}mm, muss aber min. 0.6mm sein.")
            if aufmass_z < 4.5:
                fehler_liste.append(f"Z-Aufmaß ist {aufmass_z:.2f}mm, muss aber min. 4.5mm sein.")

            # 2. Prüfung: Maximalaufmaß
            if aufmass_x > 11.0:
                fehler_liste.append(f"X-Aufmaß ist {aufmass_x:.2f}mm, darf aber max. 11mm sein.")
            if aufmass_y > 14.0:
                fehler_liste.append(f"Y-Aufmaß ist {aufmass_y:.2f}mm, darf aber max. 14mm sein.")
            if aufmass_z > 25.0:
                fehler_liste.append(f"Z-Aufmaß ist {aufmass_z:.2f}mm, darf aber max. 25mm sein.")

            # Überprüfen, ob Fehler aufgetreten sind
            if fehler_liste:
                # Alle gefundenen Fehler zu einer Nachricht zusammenfügen
                fehler_nachricht = "Aufmaß-Prüfung fehlgeschlagen: " + " | ".join(fehler_liste)
                self.status_update.emit(fehler_nachricht)
                self.show_info_dialog.emit("Fehler im Aufmaß", fehler_nachricht) # Evtl. als Dialog anzeigen
                return False
            else:
                self.status_update.emit("Aufmaße sind innerhalb der Toleranzen.")
                return True

        except (ValueError, TypeError):
            self.status_update.emit("Fehler: Konnte Roh- oder Fertigmaße für den Vergleich nicht in Zahlen umwandeln.")
            return False

    def fertig_abmasse_eintragen(self) -> None:
        '''Trägt die ausgelesenen Abmasse ins Hauptprogramm in die entsprechenden lineedits ein.'''
        x = str(self.x_fertig)
        y = str(self.y_fertig)
        z = str(self.z_fertig)
        self.ausgelesene_fertig_werte.emit(x, y, z)

    def esprit_dateiname_pruefen(self) -> bool:
        """
        Prüfung, ob der Pfad existiert und ob bereits eine Datei mit der Endung '_A.esp' im Zielordner liegt,
        um ein versehentliches Überschreiben zu verhindern.
        :return: bool
        """
        # 1. Prüfen, ob der Zielordner (das Path-Objekt) existiert und ein Verzeichnis ist.
        if not self.pfad.is_dir():
            error_msg = f"Fehler: Der angegebene Pfad '{self.pfad}' existiert nicht oder ist kein Ordner."
            self.status_update.emit(error_msg)
            return False

        # 2. Den vollständigen Dateinamen für die Prüfung erstellen
        # Wichtig: Annahme, dass die Esprit-Dateien die Endung .esp haben. Passe dies bei Bedarf an.
        dateiname_mit_endung = f"{self.pgm_name}_A.esp"
        zieldatei_pfad = self.pfad / dateiname_mit_endung

        # 3. Prüfen, ob die Zieldatei bereits existiert
        if zieldatei_pfad.exists():
            error_msg = f"Abbruch: Die Datei '{dateiname_mit_endung}' existiert bereits im Zielordner."
            self.status_update.emit(error_msg)
            # Hier wäre ein show_info_dialog eventuell auch sinnvoll
            self.show_info_dialog.emit("Datei existiert bereits", error_msg)
            return False

        self.status_update.emit("Dateiname und Pfad sind gültig.")
        return True

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

        pfad_schraubstock = self.pfad / "!schraubstock.step"
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
        self.finished.emit(True, "Wizard A erfolgreich abgeschlossen.")

#####################################################################################################

    def run(self):
        """Hauptmethode des Workers, die beim Start des Threads ausgeführt wird."""
        try:
            self.automations_typ_bestimmen()
        except Exception as e:
            # Bei einem Fehler, sende ein Fehlersignal mit der Fehlermeldung
            error_message = f"Ein unerwarteter Fehler ist aufgetreten: {e}"
            self.status_update.emit(error_message)
            self.finished.emit(False, error_message)
            print(f"[FEHLER] im EspritA Worker: {e}")
