import sys

from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

from UI.frm_main_window import Ui_frm_main_window

class MainWindow(qtw.QMainWindow, Ui_frm_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    with open("Styles/Perstfic.qss", "r") as stylesheet_file:
        app.setStyleSheet(stylesheet_file.read())

    sys.exit(app.exec())

# UIC DATEI UMWANDELN
# pyside6-uic UI/frm_main_window.ui -o UI/frm_main_window.py

# RSC DATEI UMWANDELN
# pyside6-rcc UI/Icons/icons.qrc -o UI/Icons/icons_rc.py
# pyside6-rcc UI/icons.qrc -o UI/icons_rc.py

# build UI ausführen im Terminal
# python UI/build_ui.py