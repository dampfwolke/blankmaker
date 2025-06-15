import sys
import csv
from pathlib import Path

from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

from UI.frm_stats_auswertung import Ui_frm_stats_auswertung


class StatsAuswertung(qtw.QMainWindow, Ui_frm_stats_auswertung):
    DIR_PATH_CSV = Path(__file__).parent.parent / "stats"

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lb_zeit_ausgabe.setText("")
        self.lb_roh_ausgabe.setText("")

        # Modell erstellen Zeitersparnis
        self.model_zeit = qtg.QStandardItemModel()
        self.tv_zeit.setModel(self.model_zeit)
        # Modell erstellen Rohteil
        self.model_rohteil = qtg.QStandardItemModel()
        self.tv_rohteil.setModel(self.model_rohteil)

        # CSV laden
        self.csv_laden_zeit("laufzeit.csv")
        self.csv_laden_rohteil("rohteil_fehler.csv")

        # Verbindet den Klick auf den Button mit der Auswertungsmethode.
        self.pb_auswerten_zeit.clicked.connect(self.auswerten_zeit)
        self.pb_aktualisieren_zeit.clicked.connect(self.aktualisieren_zeit)

    @qtc.Slot()
    def aktualisieren_zeit(self):
        self.lb_zeit_ausgabe.setText("")
        font1 = qtg.QFont()
        font1.setPointSize(12)
        self.lb_zeit_ausgabe.setFont(font1)

    def csv_laden_rohteil(self, file):
        filepath = self.DIR_PATH_CSV / file
        self.model_rohteil.clear()
        try:
            with open(filepath, newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile, delimiter=",")

                # Kopfzeile lesen und setzen
                header = next(reader)
                self.model_rohteil.setHorizontalHeaderLabels(header)

                # Datenzeilen lesen und dem Modell hinzufügen
                for row_data in reader:
                    items = [qtg.QStandardItem(field) for field in row_data]
                    self.model_rohteil.appendRow(items)

            # Passt alle Spalten an die Breite ihres Inhalts an.
            self.tv_zeit.resizeColumnsToContents()

        except FileNotFoundError:
            print(f"Fehler: Die Datei {filepath} wurde nicht gefunden.")
            # Optional: Fehlermeldung in der GUI anzeigen
            self.model_rohteil.setHorizontalHeaderLabels(["Fehler"])
            self.model_rohteil.appendRow([qtg.QStandardItem("CSV-Datei nicht gefunden.")])
        except Exception as e:
            print(f"Ein Fehler ist beim Lesen der CSV aufgetreten: {e}")

    def csv_laden_zeit(self, file):
        filepath = self.DIR_PATH_CSV / file
        self.model_zeit.clear()
        try:
            with open(filepath, newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile, delimiter=",")

                # Kopfzeile lesen und setzen
                header = next(reader)
                self.model_zeit.setHorizontalHeaderLabels(header)

                # Datenzeilen lesen und dem Modell hinzufügen
                for row_data in reader:
                    items = [qtg.QStandardItem(field) for field in row_data]
                    self.model_zeit.appendRow(items)

            # Passt alle Spalten an die Breite ihres Inhalts an.
            self.tv_zeit.resizeColumnsToContents()
            # Sorgt dafür, dass die letzte Spalte den restlichen Platz einnimmt.
            if self.model_zeit.columnCount() > 0:
                header_view = self.tv_zeit.horizontalHeader()
                header_view.setSectionResizeMode(self.model_zeit.columnCount() - 1, qtw.QHeaderView.Stretch)

        except FileNotFoundError:
            print(f"Fehler: Die Datei {filepath} wurde nicht gefunden.")
            # Optional: Fehlermeldung in der GUI anzeigen
            self.model_zeit.setHorizontalHeaderLabels(["Fehler"])
            self.model_zeit.appendRow([qtg.QStandardItem("CSV-Datei nicht gefunden.")])
        except Exception as e:
            print(f"Ein Fehler ist beim Lesen der CSV aufgetreten: {e}")

    @qtc.Slot()
    def auswerten_zeit(self):
        """
        Berechnet die Summe der Zeiten aus der dritten Spalte (Index 2)
        und zeigt das Ergebnis im Label an.
        """
        total_sekunden = 0
        spalten_index = 2  # Die dritte Spalte hat den Index 2

        # Durch alle Zeilen des Modells iterieren
        for row in range(self.model_zeit.rowCount()):
            item = self.model_zeit.item(row, spalten_index)

            # Sicherstellen, dass die Zelle nicht leer ist
            if item and item.text():
                zeit_string = item.text()
                try:
                    # Den String "MM:SS" am Doppelpunkt aufteilen
                    minuten, sekunden = map(int, zeit_string.split(':'))
                    # Die Zeit für diese Zeile in Sekunden umrechnen und zur Summe addieren
                    total_sekunden += (minuten * 60) + sekunden
                except (ValueError, IndexError):
                    # Fehlerhafte Formate ignorieren und eine Meldung ausgeben
                    print(f"Warnung: Ungültiges Zeitformat in Zeile {row + 1}: '{zeit_string}'")

        # Die Gesamtsekunden wieder in ein lesbares Format umwandeln (HH:MM:SS)
        stunden, rest_sekunden = divmod(total_sekunden, 3600)
        minuten, sekunden = divmod(rest_sekunden, 60)

        # Das Ergebnis formatiert im Label ausgeben (z.B. "01:23:45")
        self.lb_zeit_ausgabe.setStyleSheet("color: darkred;")
        ergebnis_string = f"{stunden:02d} Stunden {minuten:02d} Minuten {sekunden:02d} Sekunden"
        self.lb_zeit_ausgabe.setText(f"Durch Automatisierung ergaunerte Bildschirmpause:   {ergebnis_string}")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = StatsAuswertung()
    window.show()
    sys.exit(app.exec())