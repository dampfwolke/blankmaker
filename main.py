import sys

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


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # with open("UI/Styles/Perstfic.qss", "r") as stylesheet_file:
    #     app.setStyleSheet(stylesheet_file.read())

    sys.exit(app.exec())
