import sys

from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

from UI.frm_stats_auswertung import Ui_frm_stats_auswertung

class StatsAuswertung(qtw.QMainWindow, Ui_frm_stats_auswertung):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = StatsAuswertung()
    window.show()
    sys.exit(app.exec())