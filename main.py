import sys

from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

from utils.zeitstempel import zeitstempel
from utils.kalenderwoche import kw_ermitteln

from UI.frm_main_window import Ui_frm_main_window
from UI.animated_tabhelper import AnimatedTabHelper  # <-- Animation importieren

class MainWindow(qtw.QMainWindow, Ui_frm_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.wg_datum_editieren.setHidden(True)
        self.le_pfad.setDisabled(True)
        self.de_datum.setDate(qtc.QDate.currentDate())
        self.statusBar()
        # Füge Animationen für das TabWidget hinzu
        self.anim_tabs = AnimatedTabHelper(self.tw_rohteil_erstellen)

        # TEST Noch nicht fertig
        self.pb_rechteck.clicked.connect(self.rechteck_erstellen)
        self.le_rechteck_hoehe.editingFinished.connect(self.rechteck_erstellen)

        self.le_pfad.setText(f"K:\\Esprit\\NC-Files\\AT-25-KW{kw_ermitteln()[0]}\\Hasanovic\\{kw_ermitteln()[1]}")

    @qtc.Slot()
    def rechteck_erstellen(self) -> None:
        self.statusBar().showMessage(f"Rechteck wurde erstellt. {zeitstempel(1)}", 5000)
        print(f"Rechteck wurde erstellt! {zeitstempel(1)}")



if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # with open("UI/Styles/Dtor.qss", "r") as stylesheet_file:
    #     app.setStyleSheet(stylesheet_file.read())

    sys.exit(app.exec())
