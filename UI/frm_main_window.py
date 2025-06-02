# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QWidget)

class Ui_frm_main_window(object):
    def setupUi(self, frm_main_window):
        if not frm_main_window.objectName():
            frm_main_window.setObjectName(u"frm_main_window")
        frm_main_window.resize(520, 600)
        self.centralwidget = QWidget(frm_main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tw_rohteil_erstellen = QTabWidget(self.centralwidget)
        self.tw_rohteil_erstellen.setObjectName(u"tw_rohteil_erstellen")
        self.tw_rohteil_erstellen.setGeometry(QRect(70, 40, 316, 188))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(12)
        font.setBold(False)
        self.tw_rohteil_erstellen.setFont(font)
        self.tw_rohteil_erstellen.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tab_rechteck = QWidget()
        self.tab_rechteck.setObjectName(u"tab_rechteck")
        self.gridLayout = QGridLayout(self.tab_rechteck)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_rechteck_laenge = QLabel(self.tab_rechteck)
        self.lb_rechteck_laenge.setObjectName(u"lb_rechteck_laenge")
        self.lb_rechteck_laenge.setFont(font)
        self.lb_rechteck_laenge.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_rechteck_laenge, 0, 0, 1, 1)

        self.le_rechteck_laenge = QLineEdit(self.tab_rechteck)
        self.le_rechteck_laenge.setObjectName(u"le_rechteck_laenge")

        self.gridLayout.addWidget(self.le_rechteck_laenge, 0, 1, 1, 1)

        self.lb_rechteck_breite = QLabel(self.tab_rechteck)
        self.lb_rechteck_breite.setObjectName(u"lb_rechteck_breite")
        self.lb_rechteck_breite.setFont(font)
        self.lb_rechteck_breite.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_rechteck_breite, 1, 0, 1, 1)

        self.le_rechteck_breite = QLineEdit(self.tab_rechteck)
        self.le_rechteck_breite.setObjectName(u"le_rechteck_breite")
        self.le_rechteck_breite.setFont(font)

        self.gridLayout.addWidget(self.le_rechteck_breite, 1, 1, 1, 1)

        self.lb_rechteck_hoehe = QLabel(self.tab_rechteck)
        self.lb_rechteck_hoehe.setObjectName(u"lb_rechteck_hoehe")
        self.lb_rechteck_hoehe.setFont(font)
        self.lb_rechteck_hoehe.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_rechteck_hoehe, 2, 0, 1, 1)

        self.le_rechteck_hoehe = QLineEdit(self.tab_rechteck)
        self.le_rechteck_hoehe.setObjectName(u"le_rechteck_hoehe")
        self.le_rechteck_hoehe.setFont(font)

        self.gridLayout.addWidget(self.le_rechteck_hoehe, 2, 1, 1, 1)

        self.pb_rechteck = QPushButton(self.tab_rechteck)
        self.pb_rechteck.setObjectName(u"pb_rechteck")
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.pb_rechteck.setFont(font1)
        self.pb_rechteck.setAutoDefault(True)

        self.gridLayout.addWidget(self.pb_rechteck, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.tw_rohteil_erstellen.addTab(self.tab_rechteck, "")
        self.tab_kreis = QWidget()
        self.tab_kreis.setObjectName(u"tab_kreis")
        self.gridLayout_2 = QGridLayout(self.tab_kreis)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.le_kreis_durchmesser = QLineEdit(self.tab_kreis)
        self.le_kreis_durchmesser.setObjectName(u"le_kreis_durchmesser")

        self.gridLayout_2.addWidget(self.le_kreis_durchmesser, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.lb_kreis_durchmesser = QLabel(self.tab_kreis)
        self.lb_kreis_durchmesser.setObjectName(u"lb_kreis_durchmesser")
        self.lb_kreis_durchmesser.setFont(font)
        self.lb_kreis_durchmesser.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_kreis_durchmesser, 0, 0, 1, 1)

        self.le_kreis_hoehe = QLineEdit(self.tab_kreis)
        self.le_kreis_hoehe.setObjectName(u"le_kreis_hoehe")

        self.gridLayout_2.addWidget(self.le_kreis_hoehe, 1, 1, 1, 1)

        self.lb_kreis_hoehe = QLabel(self.tab_kreis)
        self.lb_kreis_hoehe.setObjectName(u"lb_kreis_hoehe")
        self.lb_kreis_hoehe.setFont(font)
        self.lb_kreis_hoehe.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_kreis_hoehe, 1, 0, 1, 1)

        self.pb_kreis = QPushButton(self.tab_kreis)
        self.pb_kreis.setObjectName(u"pb_kreis")
        self.pb_kreis.setFont(font1)

        self.gridLayout_2.addWidget(self.pb_kreis, 2, 1, 1, 1)

        self.tw_rohteil_erstellen.addTab(self.tab_kreis, "")
        frm_main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 520, 33))
        frm_main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_main_window)
        self.statusbar.setObjectName(u"statusbar")
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setHintingPreference(QFont.PreferFullHinting)
        self.statusbar.setFont(font2)
        frm_main_window.setStatusBar(self.statusbar)

        self.retranslateUi(frm_main_window)

        self.tw_rohteil_erstellen.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(frm_main_window)
    # setupUi

    def retranslateUi(self, frm_main_window):
        frm_main_window.setWindowTitle(QCoreApplication.translate("frm_main_window", u"MainWindow", None))
        self.lb_rechteck_laenge.setText(QCoreApplication.translate("frm_main_window", u"L\u00e4nge X:", None))
        self.le_rechteck_laenge.setText(QCoreApplication.translate("frm_main_window", u"100", None))
        self.lb_rechteck_breite.setText(QCoreApplication.translate("frm_main_window", u"Breite Y:", None))
        self.le_rechteck_breite.setText(QCoreApplication.translate("frm_main_window", u"100", None))
        self.lb_rechteck_hoehe.setText(QCoreApplication.translate("frm_main_window", u"H\u00f6he Z:", None))
        self.le_rechteck_hoehe.setText(QCoreApplication.translate("frm_main_window", u"100", None))
        self.pb_rechteck.setText(QCoreApplication.translate("frm_main_window", u"Rechteck erstellen", None))
        self.tw_rohteil_erstellen.setTabText(self.tw_rohteil_erstellen.indexOf(self.tab_rechteck), QCoreApplication.translate("frm_main_window", u"Rechteck erstellen", None))
        self.le_kreis_durchmesser.setText(QCoreApplication.translate("frm_main_window", u"100", None))
        self.lb_kreis_durchmesser.setText(QCoreApplication.translate("frm_main_window", u"Durchmesser:", None))
        self.le_kreis_hoehe.setText(QCoreApplication.translate("frm_main_window", u"100", None))
        self.lb_kreis_hoehe.setText(QCoreApplication.translate("frm_main_window", u"H\u00f6he:", None))
        self.pb_kreis.setText(QCoreApplication.translate("frm_main_window", u"Kreis erstellen", None))
        self.tw_rohteil_erstellen.setTabText(self.tw_rohteil_erstellen.indexOf(self.tab_kreis), QCoreApplication.translate("frm_main_window", u"Kreis erstellen", None))
    # retranslateUi

