import csv
from pathlib import Path

from utils.zeitstempel import zeitstempel

STATS_DIR = (Path(__file__).parent.parent / "stats").resolve()
CSV_FILE_PATH = STATS_DIR  / "laufzeit.csv"


def laufzeit_eintragen(laufzeit: str="0", kommentar: str="---") -> None:
    """Trägt die Daten in 'stats/laufzeit.csv' ein. :return:None"""
    datum = zeitstempel(2)
    uhrzeit = zeitstempel(1)
    formatierte_laufzeit = laufzeit.replace(",", ".")
    formatierter_kommentar = kommentar.replace(",", " ")
    data = (datum, uhrzeit, formatierte_laufzeit, formatierter_kommentar)
    with open(CSV_FILE_PATH, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)

def rohteil_fehler_eintragen(zeichnungsnummer: str, x_roh: str, y_roh: str, z_roh: str, x_fertig: str, y_fertig: str, z_fertig: str):
    """Trägt die Daten in 'stats/rohteil_fehler.csv' ein. :return:None"""
    datum = zeitstempel(2)
    uhrzeit = zeitstempel(1)


def main() -> None:
    laufzeit_eintragen(kommentar="erfolgreich abgeschlossen", laufzeit="19,58")

if __name__ == "__main__":
    main()

