import sys
from datetime import datetime

from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

from UI.frm_main_window import Ui_frm_main_window
from UI.animated_tabhelper import AnimatedTabHelper  # <-- Animation importieren

class MainWindow(qtw.QMainWindow, Ui_frm_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Füge Animationen für das TabWidget hinzu
        self.anim_tabs = AnimatedTabHelper(self.tw_rohteil_erstellen)
        # TEST
        self.pb_rechteck.clicked.connect(self.rechteck_erstellen)
        self.le_rechteck_hoehe.editingFinished.connect(self.rechteck_erstellen)

    @qtc.Slot()
    def rechteck_erstellen(self):
        self.statusBar().showMessage(f"Rechteck wurde erstellt. {self.zeitstempel()}", 5000)
        print(f"Rechteck wurde erstellt! {self.zeitstempel()}")

    def zeitstempel(self) -> str:
        aktuelle_zeit = datetime.now()
        zeitstempel = aktuelle_zeit.strftime("%H:%M:%S")
        return zeitstempel

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # with open("UI/Styles/Perstfic.qss", "r") as stylesheet_file:
    #     app.setStyleSheet(stylesheet_file.read())

    sys.exit(app.exec())
