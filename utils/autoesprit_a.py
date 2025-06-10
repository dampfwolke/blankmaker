from pathlib import Path
import clipboard


class EspritA:
    def __init__(self, laenge_roh: str, breite_roh: str, hoehe_roh: str, pfad: Path, maschinenauswahl: str, typ: str,
                 sleep_timer: int):
        self.laenge_roh = laenge_roh
        self.breite_roh = breite_roh
        self.hoehe_roh = hoehe_roh
        self.pfad = pfad
        self.maschinenauswahl = maschinenauswahl
        self.typ = typ
        self.sleep_timer = sleep_timer

    def __str__(self):
        return (f"Abmaße:'X:{self.laenge_roh}'X'Y:{self.breite_roh}'X'Z:{self.hoehe_roh}'\n"
                f"Pfad: {self.pfad}\n"
                f"Bearbeitung: {self.maschinenauswahl}\n"
                f"Umfang der Automation: {self.typ}\n"
                f"Verweilzeit: {self.sleep_timer} Sekunden")

    def abmasse_pruefen(self) -> bool:
        pass


a1 = EspritA(50, 40, 25, "K:/NC-Files/KW20/hasanovic/Montag/", "5 Achs 3 Achs", "Gandalf", 2)
print(a1)