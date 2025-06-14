import csv
from pathlib import Path

from utils.zeitstempel import zeitstempel

STATS_DIR = (Path(__file__).parent.parent / "stats").resolve()
LAUFZEIT_FILE_PATH = STATS_DIR  / "laufzeit.csv"
ROHTEIL_FEHLER_FILE_PATH = STATS_DIR  / "rohteil_fehler.csv"


def laufzeit_eintragen(laufzeit: str="0", kommentar: str="---") -> None:
    """Trägt die Daten in 'stats/laufzeit.csv' ein. :return:None"""
    datum = zeitstempel(2)
    uhrzeit = zeitstempel(1)
    # Komma "," wird durch "." ersetzt da sonst csv datei nicht richtig funktioniert
    formatierte_laufzeit = laufzeit.replace(",", ".")
    formatierter_kommentar = kommentar.replace(",", " ")

    data = (datum, uhrzeit, formatierte_laufzeit, formatierter_kommentar)
    with open(LAUFZEIT_FILE_PATH, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)

def rohteil_fehler_eintragen(zeichnung_nr: str, x_roh: str, y_roh: str, z_roh: str, x_fertig: str, y_fertig: str, z_fertig: str) ->None:
    """Trägt die Daten in 'stats/rohteil_fehler.csv' ein. :return:None"""
    datum = zeitstempel(2)
    uhrzeit = zeitstempel(1)
    # Komma "," wird durch "." ersetzt da sonst csv datei nicht richtig funktioniert
    formatierte_zeichnung_nr = zeichnung_nr.replace(",", ".")
    r_x_roh = x_roh.replace(",", ".")
    r_y_roh = y_roh.replace(",", ".")
    r_z_roh = z_roh.replace(",", ".")
    r_x_fertig = x_fertig.replace(",", ".")
    r_y_fertig = y_fertig.replace(",", ".")
    r_z_fertig = z_fertig.replace(",", ".")

    data = (datum, uhrzeit, formatierte_zeichnung_nr, r_x_roh, r_y_roh, r_z_roh, r_x_fertig, r_y_fertig, r_z_fertig)
    with open(ROHTEIL_FEHLER_FILE_PATH, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)

def main() -> None:
    laufzeit_eintragen(kommentar="erfolgreich abgeschlossen", laufzeit="19,58")
    rohteil_fehler_eintragen("25T00846", "85", "70", "25", "90.55", "60,854785", "18")

if __name__ == "__main__":
    main()

