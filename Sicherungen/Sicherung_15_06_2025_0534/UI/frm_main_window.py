# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QTabWidget, QToolButton, QVBoxLayout, QWidget)

class Ui_frm_main_window(object):
    def setupUi(self, frm_main_window):
        if not frm_main_window.objectName():
            frm_main_window.setObjectName(u"frm_main_window")
        frm_main_window.resize(489, 966)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frm_main_window.sizePolicy().hasHeightForWidth())
        frm_main_window.setSizePolicy(sizePolicy)
        frm_main_window.setMinimumSize(QSize(350, 700))
        frm_main_window.setMaximumSize(QSize(600, 1000))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(8)
        frm_main_window.setFont(font)
        self.actionEinstellungen = QAction(frm_main_window)
        self.actionEinstellungen.setObjectName(u"actionEinstellungen")
        self.actionBeenden = QAction(frm_main_window)
        self.actionBeenden.setObjectName(u"actionBeenden")
        self.actionAktualisieren = QAction(frm_main_window)
        self.actionAktualisieren.setObjectName(u"actionAktualisieren")
        self.centralwidget = QWidget(frm_main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(300, 650))
        self.centralwidget.setMaximumSize(QSize(16777215, 900))
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tw_rohteil_erstellen = QTabWidget(self.centralwidget)
        self.tw_rohteil_erstellen.setObjectName(u"tw_rohteil_erstellen")
        sizePolicy.setHeightForWidth(self.tw_rohteil_erstellen.sizePolicy().hasHeightForWidth())
        self.tw_rohteil_erstellen.setSizePolicy(sizePolicy)
        self.tw_rohteil_erstellen.setMinimumSize(QSize(400, 170))
        self.tw_rohteil_erstellen.setMaximumSize(QSize(800, 180))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(8)
        font1.setBold(False)
        self.tw_rohteil_erstellen.setFont(font1)
        self.tw_rohteil_erstellen.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tw_rohteil_erstellen.setTabPosition(QTabWidget.TabPosition.North)
        self.tw_rohteil_erstellen.setIconSize(QSize(12, 12))
        self.tab_rechteck = QWidget()
        self.tab_rechteck.setObjectName(u"tab_rechteck")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tab_rechteck.sizePolicy().hasHeightForWidth())
        self.tab_rechteck.setSizePolicy(sizePolicy2)
        self.tab_rechteck.setMinimumSize(QSize(400, 130))
        self.tab_rechteck.setMaximumSize(QSize(800, 200))
        self.verticalLayout = QVBoxLayout(self.tab_rechteck)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.wg_x_roh = QWidget(self.tab_rechteck)
        self.wg_x_roh.setObjectName(u"wg_x_roh")
        sizePolicy2.setHeightForWidth(self.wg_x_roh.sizePolicy().hasHeightForWidth())
        self.wg_x_roh.setSizePolicy(sizePolicy2)
        self.wg_x_roh.setMinimumSize(QSize(0, 20))
        self.wg_x_roh.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout = QHBoxLayout(self.wg_x_roh)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.lb_rechteck_laenge = QLabel(self.wg_x_roh)
        self.lb_rechteck_laenge.setObjectName(u"lb_rechteck_laenge")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lb_rechteck_laenge.sizePolicy().hasHeightForWidth())
        self.lb_rechteck_laenge.setSizePolicy(sizePolicy3)
        self.lb_rechteck_laenge.setMinimumSize(QSize(0, 20))
        self.lb_rechteck_laenge.setMaximumSize(QSize(200, 25))
        self.lb_rechteck_laenge.setFont(font1)
        self.lb_rechteck_laenge.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lb_rechteck_laenge)

        self.horizontalSpacer_14 = QSpacerItem(71, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_14)

        self.le_rechteck_laenge = QLineEdit(self.wg_x_roh)
        self.le_rechteck_laenge.setObjectName(u"le_rechteck_laenge")
        sizePolicy3.setHeightForWidth(self.le_rechteck_laenge.sizePolicy().hasHeightForWidth())
        self.le_rechteck_laenge.setSizePolicy(sizePolicy3)
        self.le_rechteck_laenge.setMinimumSize(QSize(100, 20))
        self.le_rechteck_laenge.setMaximumSize(QSize(150, 20))
        self.le_rechteck_laenge.setFont(font1)

        self.horizontalLayout.addWidget(self.le_rechteck_laenge)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_17)


        self.verticalLayout.addWidget(self.wg_x_roh)

        self.wg_y_roh = QWidget(self.tab_rechteck)
        self.wg_y_roh.setObjectName(u"wg_y_roh")
        sizePolicy2.setHeightForWidth(self.wg_y_roh.sizePolicy().hasHeightForWidth())
        self.wg_y_roh.setSizePolicy(sizePolicy2)
        self.wg_y_roh.setMinimumSize(QSize(0, 20))
        self.wg_y_roh.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.wg_y_roh)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.lb_rechteck_breite = QLabel(self.wg_y_roh)
        self.lb_rechteck_breite.setObjectName(u"lb_rechteck_breite")
        sizePolicy3.setHeightForWidth(self.lb_rechteck_breite.sizePolicy().hasHeightForWidth())
        self.lb_rechteck_breite.setSizePolicy(sizePolicy3)
        self.lb_rechteck_breite.setMinimumSize(QSize(0, 20))
        self.lb_rechteck_breite.setMaximumSize(QSize(200, 25))
        self.lb_rechteck_breite.setFont(font1)
        self.lb_rechteck_breite.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lb_rechteck_breite)

        self.horizontalSpacer_15 = QSpacerItem(69, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_15)

        self.le_rechteck_breite = QLineEdit(self.wg_y_roh)
        self.le_rechteck_breite.setObjectName(u"le_rechteck_breite")
        sizePolicy3.setHeightForWidth(self.le_rechteck_breite.sizePolicy().hasHeightForWidth())
        self.le_rechteck_breite.setSizePolicy(sizePolicy3)
        self.le_rechteck_breite.setMinimumSize(QSize(100, 20))
        self.le_rechteck_breite.setMaximumSize(QSize(150, 20))
        self.le_rechteck_breite.setFont(font1)

        self.horizontalLayout_2.addWidget(self.le_rechteck_breite)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_18)


        self.verticalLayout.addWidget(self.wg_y_roh)

        self.wg_z_roh = QWidget(self.tab_rechteck)
        self.wg_z_roh.setObjectName(u"wg_z_roh")
        sizePolicy2.setHeightForWidth(self.wg_z_roh.sizePolicy().hasHeightForWidth())
        self.wg_z_roh.setSizePolicy(sizePolicy2)
        self.wg_z_roh.setMinimumSize(QSize(0, 20))
        self.wg_z_roh.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_3 = QHBoxLayout(self.wg_z_roh)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.lb_rechteck_hoehe = QLabel(self.wg_z_roh)
        self.lb_rechteck_hoehe.setObjectName(u"lb_rechteck_hoehe")
        sizePolicy3.setHeightForWidth(self.lb_rechteck_hoehe.sizePolicy().hasHeightForWidth())
        self.lb_rechteck_hoehe.setSizePolicy(sizePolicy3)
        self.lb_rechteck_hoehe.setMinimumSize(QSize(0, 20))
        self.lb_rechteck_hoehe.setMaximumSize(QSize(200, 25))
        self.lb_rechteck_hoehe.setFont(font1)
        self.lb_rechteck_hoehe.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lb_rechteck_hoehe)

        self.horizontalSpacer_16 = QSpacerItem(71, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_16)

        self.le_rechteck_hoehe = QLineEdit(self.wg_z_roh)
        self.le_rechteck_hoehe.setObjectName(u"le_rechteck_hoehe")
        sizePolicy3.setHeightForWidth(self.le_rechteck_hoehe.sizePolicy().hasHeightForWidth())
        self.le_rechteck_hoehe.setSizePolicy(sizePolicy3)
        self.le_rechteck_hoehe.setMinimumSize(QSize(100, 20))
        self.le_rechteck_hoehe.setMaximumSize(QSize(150, 20))
        self.le_rechteck_hoehe.setFont(font1)

        self.horizontalLayout_3.addWidget(self.le_rechteck_hoehe)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_19)


        self.verticalLayout.addWidget(self.wg_z_roh)

        self.wg_button_roh = QWidget(self.tab_rechteck)
        self.wg_button_roh.setObjectName(u"wg_button_roh")
        sizePolicy2.setHeightForWidth(self.wg_button_roh.sizePolicy().hasHeightForWidth())
        self.wg_button_roh.setSizePolicy(sizePolicy2)
        self.wg_button_roh.setMinimumSize(QSize(0, 20))
        self.wg_button_roh.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_4 = QHBoxLayout(self.wg_button_roh)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(118, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pb_rechteck = QPushButton(self.wg_button_roh)
        self.pb_rechteck.setObjectName(u"pb_rechteck")
        self.pb_rechteck.setMinimumSize(QSize(0, 20))
        self.pb_rechteck.setMaximumSize(QSize(16777215, 25))
        self.pb_rechteck.setFont(font1)
        self.pb_rechteck.setAutoDefault(True)

        self.horizontalLayout_4.addWidget(self.pb_rechteck)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.wg_button_roh)

        self.tw_rohteil_erstellen.addTab(self.tab_rechteck, "")
        self.tab_kreis = QWidget()
        self.tab_kreis.setObjectName(u"tab_kreis")
        sizePolicy.setHeightForWidth(self.tab_kreis.sizePolicy().hasHeightForWidth())
        self.tab_kreis.setSizePolicy(sizePolicy)
        self.tab_kreis.setMinimumSize(QSize(400, 100))
        self.tab_kreis.setMaximumSize(QSize(800, 200))
        self.verticalLayout_2 = QVBoxLayout(self.tab_kreis)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.wg_durchmesser = QWidget(self.tab_kreis)
        self.wg_durchmesser.setObjectName(u"wg_durchmesser")
        self.wg_durchmesser.setMinimumSize(QSize(400, 20))
        self.wg_durchmesser.setMaximumSize(QSize(600, 25))
        self.horizontalLayout_7 = QHBoxLayout(self.wg_durchmesser)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.lb_durchmesser = QLabel(self.wg_durchmesser)
        self.lb_durchmesser.setObjectName(u"lb_durchmesser")
        self.lb_durchmesser.setMinimumSize(QSize(80, 20))
        self.lb_durchmesser.setMaximumSize(QSize(200, 25))
        self.lb_durchmesser.setFont(font1)
        self.lb_durchmesser.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lb_durchmesser)

        self.horizontalSpacer_20 = QSpacerItem(43, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_20)

        self.le_durchmesser = QLineEdit(self.wg_durchmesser)
        self.le_durchmesser.setObjectName(u"le_durchmesser")
        sizePolicy3.setHeightForWidth(self.le_durchmesser.sizePolicy().hasHeightForWidth())
        self.le_durchmesser.setSizePolicy(sizePolicy3)
        self.le_durchmesser.setMinimumSize(QSize(100, 20))
        self.le_durchmesser.setMaximumSize(QSize(150, 20))
        self.le_durchmesser.setFont(font1)

        self.horizontalLayout_7.addWidget(self.le_durchmesser)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_22)


        self.verticalLayout_2.addWidget(self.wg_durchmesser)

        self.wg_z_kreis = QWidget(self.tab_kreis)
        self.wg_z_kreis.setObjectName(u"wg_z_kreis")
        self.wg_z_kreis.setMinimumSize(QSize(400, 20))
        self.wg_z_kreis.setMaximumSize(QSize(600, 25))
        self.horizontalLayout_6 = QHBoxLayout(self.wg_z_kreis)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.lb_kreis_hoehe = QLabel(self.wg_z_kreis)
        self.lb_kreis_hoehe.setObjectName(u"lb_kreis_hoehe")
        self.lb_kreis_hoehe.setMinimumSize(QSize(80, 20))
        self.lb_kreis_hoehe.setMaximumSize(QSize(200, 25))
        self.lb_kreis_hoehe.setFont(font1)
        self.lb_kreis_hoehe.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.lb_kreis_hoehe)

        self.horizontalSpacer_21 = QSpacerItem(43, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_21)

        self.le_z_kreis = QLineEdit(self.wg_z_kreis)
        self.le_z_kreis.setObjectName(u"le_z_kreis")
        sizePolicy3.setHeightForWidth(self.le_z_kreis.sizePolicy().hasHeightForWidth())
        self.le_z_kreis.setSizePolicy(sizePolicy3)
        self.le_z_kreis.setMinimumSize(QSize(100, 20))
        self.le_z_kreis.setMaximumSize(QSize(150, 20))
        self.le_z_kreis.setFont(font1)

        self.horizontalLayout_6.addWidget(self.le_z_kreis)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_23)


        self.verticalLayout_2.addWidget(self.wg_z_kreis)

        self.verticalSpacer = QSpacerItem(20, 22, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.wg_button_kreis = QWidget(self.tab_kreis)
        self.wg_button_kreis.setObjectName(u"wg_button_kreis")
        self.wg_button_kreis.setMinimumSize(QSize(0, 20))
        self.wg_button_kreis.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_5 = QHBoxLayout(self.wg_button_kreis)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_4 = QSpacerItem(119, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.pb_kreis = QPushButton(self.wg_button_kreis)
        self.pb_kreis.setObjectName(u"pb_kreis")
        self.pb_kreis.setMinimumSize(QSize(80, 20))
        self.pb_kreis.setMaximumSize(QSize(100, 25))
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setKerning(True)
        self.pb_kreis.setFont(font2)

        self.horizontalLayout_5.addWidget(self.pb_kreis)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.wg_button_kreis)

        self.tw_rohteil_erstellen.addTab(self.tab_kreis, "")

        self.verticalLayout_8.addWidget(self.tw_rohteil_erstellen)

        self.gb_spannmittel = QGroupBox(self.centralwidget)
        self.gb_spannmittel.setObjectName(u"gb_spannmittel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.gb_spannmittel.sizePolicy().hasHeightForWidth())
        self.gb_spannmittel.setSizePolicy(sizePolicy4)
        self.gb_spannmittel.setMinimumSize(QSize(400, 100))
        self.gb_spannmittel.setMaximumSize(QSize(16777215, 250))
        self.gb_spannmittel.setFont(font1)
        self.gb_spannmittel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_3 = QVBoxLayout(self.gb_spannmittel)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.wg_zielpfad = QWidget(self.gb_spannmittel)
        self.wg_zielpfad.setObjectName(u"wg_zielpfad")
        self.wg_zielpfad.setMinimumSize(QSize(0, 25))
        self.wg_zielpfad.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_10 = QHBoxLayout(self.wg_zielpfad)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 5)
        self.lb_pfad = QLabel(self.wg_zielpfad)
        self.lb_pfad.setObjectName(u"lb_pfad")
        sizePolicy3.setHeightForWidth(self.lb_pfad.sizePolicy().hasHeightForWidth())
        self.lb_pfad.setSizePolicy(sizePolicy3)
        self.lb_pfad.setMinimumSize(QSize(0, 20))
        self.lb_pfad.setMaximumSize(QSize(200, 25))
        self.lb_pfad.setFont(font1)
        self.lb_pfad.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lb_pfad)

        self.horizontalSpacer_8 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.le_pfad = QLineEdit(self.wg_zielpfad)
        self.le_pfad.setObjectName(u"le_pfad")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.le_pfad.sizePolicy().hasHeightForWidth())
        self.le_pfad.setSizePolicy(sizePolicy5)
        self.le_pfad.setMinimumSize(QSize(340, 20))
        self.le_pfad.setMaximumSize(QSize(16777215, 25))
        self.le_pfad.setFont(font1)

        self.horizontalLayout_10.addWidget(self.le_pfad)


        self.verticalLayout_3.addWidget(self.wg_zielpfad)

        self.fr_spannmittelauswahl = QFrame(self.gb_spannmittel)
        self.fr_spannmittelauswahl.setObjectName(u"fr_spannmittelauswahl")
        self.fr_spannmittelauswahl.setMinimumSize(QSize(300, 25))
        self.fr_spannmittelauswahl.setMaximumSize(QSize(550, 30))
        self.fr_spannmittelauswahl.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_spannmittelauswahl.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.fr_spannmittelauswahl)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 3)
        self.cb_spannmittel = QComboBox(self.fr_spannmittelauswahl)
        self.cb_spannmittel.setObjectName(u"cb_spannmittel")
        self.cb_spannmittel.setMinimumSize(QSize(180, 25))
        self.cb_spannmittel.setMaximumSize(QSize(200, 30))
        self.cb_spannmittel.setFont(font1)

        self.horizontalLayout_11.addWidget(self.cb_spannmittel)

        self.horizontalSpacer_10 = QSpacerItem(15, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.cb_bearbeitung_auswahl = QComboBox(self.fr_spannmittelauswahl)
        self.cb_bearbeitung_auswahl.addItem("")
        self.cb_bearbeitung_auswahl.addItem("")
        self.cb_bearbeitung_auswahl.addItem("")
        self.cb_bearbeitung_auswahl.addItem("")
        self.cb_bearbeitung_auswahl.addItem("")
        self.cb_bearbeitung_auswahl.addItem("")
        self.cb_bearbeitung_auswahl.addItem("")
        self.cb_bearbeitung_auswahl.setObjectName(u"cb_bearbeitung_auswahl")
        self.cb_bearbeitung_auswahl.setMinimumSize(QSize(120, 25))
        self.cb_bearbeitung_auswahl.setMaximumSize(QSize(150, 30))
        self.cb_bearbeitung_auswahl.setFont(font1)

        self.horizontalLayout_11.addWidget(self.cb_bearbeitung_auswahl)

        self.horizontalSpacer_39 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_39)


        self.verticalLayout_3.addWidget(self.fr_spannmittelauswahl)

        self.wg_spannmittel_breite = QWidget(self.gb_spannmittel)
        self.wg_spannmittel_breite.setObjectName(u"wg_spannmittel_breite")
        self.wg_spannmittel_breite.setMinimumSize(QSize(0, 25))
        self.wg_spannmittel_breite.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_12 = QHBoxLayout(self.wg_spannmittel_breite)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 4, -1, 3)
        self.lb_spannmittel_wert = QLabel(self.wg_spannmittel_breite)
        self.lb_spannmittel_wert.setObjectName(u"lb_spannmittel_wert")
        sizePolicy3.setHeightForWidth(self.lb_spannmittel_wert.sizePolicy().hasHeightForWidth())
        self.lb_spannmittel_wert.setSizePolicy(sizePolicy3)
        self.lb_spannmittel_wert.setMinimumSize(QSize(0, 20))
        self.lb_spannmittel_wert.setMaximumSize(QSize(200, 25))
        self.lb_spannmittel_wert.setFont(font1)
        self.lb_spannmittel_wert.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.lb_spannmittel_wert)

        self.horizontalSpacer_11 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_11)

        self.le_spannmittel = QLineEdit(self.wg_spannmittel_breite)
        self.le_spannmittel.setObjectName(u"le_spannmittel")
        sizePolicy3.setHeightForWidth(self.le_spannmittel.sizePolicy().hasHeightForWidth())
        self.le_spannmittel.setSizePolicy(sizePolicy3)
        self.le_spannmittel.setMinimumSize(QSize(100, 20))
        self.le_spannmittel.setMaximumSize(QSize(150, 20))
        self.le_spannmittel.setFont(font1)

        self.horizontalLayout_12.addWidget(self.le_spannmittel)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addWidget(self.wg_spannmittel_breite)

        self.wg_spannmittel_erstellen = QWidget(self.gb_spannmittel)
        self.wg_spannmittel_erstellen.setObjectName(u"wg_spannmittel_erstellen")
        self.wg_spannmittel_erstellen.setMinimumSize(QSize(0, 25))
        self.wg_spannmittel_erstellen.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_9 = QHBoxLayout(self.wg_spannmittel_erstellen)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 2, -1, 2)
        self.tb_spannmittel_aufklappen = QToolButton(self.wg_spannmittel_erstellen)
        self.tb_spannmittel_aufklappen.setObjectName(u"tb_spannmittel_aufklappen")
        self.tb_spannmittel_aufklappen.setMinimumSize(QSize(20, 20))
        self.tb_spannmittel_aufklappen.setMaximumSize(QSize(20, 20))
        self.tb_spannmittel_aufklappen.setFont(font1)
        self.tb_spannmittel_aufklappen.setFocusPolicy(Qt.FocusPolicy.NoFocus)
#if QT_CONFIG(shortcut)
        self.tb_spannmittel_aufklappen.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.tb_spannmittel_aufklappen.setCheckable(True)
        self.tb_spannmittel_aufklappen.setChecked(True)
        self.tb_spannmittel_aufklappen.setAutoRaise(True)

        self.horizontalLayout_9.addWidget(self.tb_spannmittel_aufklappen)

        self.horizontalSpacer_12 = QSpacerItem(101, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)

        self.pb_spannmittel = QPushButton(self.wg_spannmittel_erstellen)
        self.pb_spannmittel.setObjectName(u"pb_spannmittel")
        self.pb_spannmittel.setMinimumSize(QSize(120, 20))
        self.pb_spannmittel.setMaximumSize(QSize(150, 25))
        self.pb_spannmittel.setFont(font1)
        self.pb_spannmittel.setAutoDefault(True)

        self.horizontalLayout_9.addWidget(self.pb_spannmittel)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)


        self.verticalLayout_3.addWidget(self.wg_spannmittel_erstellen)

        self.wg_datum_editieren = QWidget(self.gb_spannmittel)
        self.wg_datum_editieren.setObjectName(u"wg_datum_editieren")
        sizePolicy.setHeightForWidth(self.wg_datum_editieren.sizePolicy().hasHeightForWidth())
        self.wg_datum_editieren.setSizePolicy(sizePolicy)
        self.wg_datum_editieren.setMinimumSize(QSize(0, 25))
        self.wg_datum_editieren.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_8 = QHBoxLayout(self.wg_datum_editieren)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 3, -1, 0)
        self.cbx_datum_editieren = QCheckBox(self.wg_datum_editieren)
        self.cbx_datum_editieren.setObjectName(u"cbx_datum_editieren")
        self.cbx_datum_editieren.setMinimumSize(QSize(0, 20))
        self.cbx_datum_editieren.setMaximumSize(QSize(16777215, 25))
        self.cbx_datum_editieren.setFont(font1)

        self.horizontalLayout_8.addWidget(self.cbx_datum_editieren)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.de_datum = QDateEdit(self.wg_datum_editieren)
        self.de_datum.setObjectName(u"de_datum")
        self.de_datum.setMinimumSize(QSize(100, 20))
        self.de_datum.setMaximumSize(QSize(16777215, 25))
        self.de_datum.setFont(font1)
        self.de_datum.setMinimumDate(QDate(2012, 9, 14))
        self.de_datum.setCalendarPopup(True)
        self.de_datum.setCurrentSectionIndex(0)
        self.de_datum.setTimeSpec(Qt.TimeSpec.LocalTime)
        self.de_datum.setDate(QDate(2025, 6, 4))

        self.horizontalLayout_8.addWidget(self.de_datum)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_45)


        self.verticalLayout_3.addWidget(self.wg_datum_editieren)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.verticalLayout_8.addWidget(self.gb_spannmittel)

        self.gb_automatisierung = QGroupBox(self.centralwidget)
        self.gb_automatisierung.setObjectName(u"gb_automatisierung")
        sizePolicy1.setHeightForWidth(self.gb_automatisierung.sizePolicy().hasHeightForWidth())
        self.gb_automatisierung.setSizePolicy(sizePolicy1)
        self.gb_automatisierung.setMinimumSize(QSize(320, 100))
        self.gb_automatisierung.setMaximumSize(QSize(800, 280))
        self.gb_automatisierung.setFont(font1)
        self.gb_automatisierung.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_4 = QVBoxLayout(self.gb_automatisierung)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.wg_zeichnungsnr = QWidget(self.gb_automatisierung)
        self.wg_zeichnungsnr.setObjectName(u"wg_zeichnungsnr")
        sizePolicy4.setHeightForWidth(self.wg_zeichnungsnr.sizePolicy().hasHeightForWidth())
        self.wg_zeichnungsnr.setSizePolicy(sizePolicy4)
        self.wg_zeichnungsnr.setMinimumSize(QSize(0, 20))
        self.wg_zeichnungsnr.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_13 = QHBoxLayout(self.wg_zeichnungsnr)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 3)
        self.lb_zeichnungsnr = QLabel(self.wg_zeichnungsnr)
        self.lb_zeichnungsnr.setObjectName(u"lb_zeichnungsnr")
        sizePolicy3.setHeightForWidth(self.lb_zeichnungsnr.sizePolicy().hasHeightForWidth())
        self.lb_zeichnungsnr.setSizePolicy(sizePolicy3)
        self.lb_zeichnungsnr.setMaximumSize(QSize(200, 200))
        self.lb_zeichnungsnr.setFont(font1)
        self.lb_zeichnungsnr.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lb_zeichnungsnr)

        self.horizontalSpacer_13 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)

        self.le_zeichnungsnr = QLineEdit(self.wg_zeichnungsnr)
        self.le_zeichnungsnr.setObjectName(u"le_zeichnungsnr")
        self.le_zeichnungsnr.setMinimumSize(QSize(335, 25))
        self.le_zeichnungsnr.setMaximumSize(QSize(16777215, 800))
        self.le_zeichnungsnr.setFont(font1)

        self.horizontalLayout_13.addWidget(self.le_zeichnungsnr)


        self.verticalLayout_4.addWidget(self.wg_zeichnungsnr)

        self.wg_wizard_a_buttons = QWidget(self.gb_automatisierung)
        self.wg_wizard_a_buttons.setObjectName(u"wg_wizard_a_buttons")
        sizePolicy4.setHeightForWidth(self.wg_wizard_a_buttons.sizePolicy().hasHeightForWidth())
        self.wg_wizard_a_buttons.setSizePolicy(sizePolicy4)
        self.wg_wizard_a_buttons.setMinimumSize(QSize(0, 25))
        self.wg_wizard_a_buttons.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_22 = QHBoxLayout(self.wg_wizard_a_buttons)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 3, -1, 0)
        self.tb_wizard_a_aufklappen = QToolButton(self.wg_wizard_a_buttons)
        self.tb_wizard_a_aufklappen.setObjectName(u"tb_wizard_a_aufklappen")
        self.tb_wizard_a_aufklappen.setMinimumSize(QSize(20, 20))
        self.tb_wizard_a_aufklappen.setMaximumSize(QSize(20, 20))
        self.tb_wizard_a_aufklappen.setFont(font1)
        self.tb_wizard_a_aufklappen.setFocusPolicy(Qt.FocusPolicy.NoFocus)
#if QT_CONFIG(shortcut)
        self.tb_wizard_a_aufklappen.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.tb_wizard_a_aufklappen.setCheckable(True)
        self.tb_wizard_a_aufklappen.setChecked(True)
        self.tb_wizard_a_aufklappen.setAutoRaise(True)

        self.horizontalLayout_22.addWidget(self.tb_wizard_a_aufklappen)

        self.horizontalSpacer_41 = QSpacerItem(99, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_41)

        self.pb_wizard_a = QPushButton(self.wg_wizard_a_buttons)
        self.pb_wizard_a.setObjectName(u"pb_wizard_a")
        self.pb_wizard_a.setMinimumSize(QSize(70, 20))
        self.pb_wizard_a.setMaximumSize(QSize(100, 25))
        self.pb_wizard_a.setFont(font1)
        self.pb_wizard_a.setAutoDefault(True)

        self.horizontalLayout_22.addWidget(self.pb_wizard_a)

        self.horizontalSpacer_40 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_40)

        self.cb_auto_option_a = QComboBox(self.wg_wizard_a_buttons)
        self.cb_auto_option_a.addItem("")
        self.cb_auto_option_a.addItem("")
        self.cb_auto_option_a.addItem("")
        self.cb_auto_option_a.addItem("")
        self.cb_auto_option_a.setObjectName(u"cb_auto_option_a")
        self.cb_auto_option_a.setMinimumSize(QSize(170, 20))
        self.cb_auto_option_a.setMaximumSize(QSize(205, 25))

        self.horizontalLayout_22.addWidget(self.cb_auto_option_a)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_43)


        self.verticalLayout_4.addWidget(self.wg_wizard_a_buttons)

        self.wg_sleep_timer = QWidget(self.gb_automatisierung)
        self.wg_sleep_timer.setObjectName(u"wg_sleep_timer")
        self.wg_sleep_timer.setMinimumSize(QSize(0, 25))
        self.wg_sleep_timer.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_24 = QHBoxLayout(self.wg_sleep_timer)
        self.horizontalLayout_24.setSpacing(5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 0, -1, 0)
        self.lb_sleep_timer = QLabel(self.wg_sleep_timer)
        self.lb_sleep_timer.setObjectName(u"lb_sleep_timer")
        self.lb_sleep_timer.setMinimumSize(QSize(0, 20))
        self.lb_sleep_timer.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_24.addWidget(self.lb_sleep_timer)

        self.hsl_sleep_timer = QSlider(self.wg_sleep_timer)
        self.hsl_sleep_timer.setObjectName(u"hsl_sleep_timer")
        self.hsl_sleep_timer.setMinimumSize(QSize(0, 20))
        self.hsl_sleep_timer.setMaximumSize(QSize(16777215, 25))
        self.hsl_sleep_timer.setMinimum(1)
        self.hsl_sleep_timer.setMaximum(100)
        self.hsl_sleep_timer.setPageStep(5)
        self.hsl_sleep_timer.setValue(5)
        self.hsl_sleep_timer.setSliderPosition(5)
        self.hsl_sleep_timer.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_24.addWidget(self.hsl_sleep_timer)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_47)


        self.verticalLayout_4.addWidget(self.wg_sleep_timer)

        self.wg_wizard_b_buttons = QWidget(self.gb_automatisierung)
        self.wg_wizard_b_buttons.setObjectName(u"wg_wizard_b_buttons")
        sizePolicy4.setHeightForWidth(self.wg_wizard_b_buttons.sizePolicy().hasHeightForWidth())
        self.wg_wizard_b_buttons.setSizePolicy(sizePolicy4)
        self.wg_wizard_b_buttons.setMinimumSize(QSize(0, 25))
        self.wg_wizard_b_buttons.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_23 = QHBoxLayout(self.wg_wizard_b_buttons)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 0, -1, 0)
        self.tb_wizard_b_aufklappen = QToolButton(self.wg_wizard_b_buttons)
        self.tb_wizard_b_aufklappen.setObjectName(u"tb_wizard_b_aufklappen")
        self.tb_wizard_b_aufklappen.setMinimumSize(QSize(20, 20))
        self.tb_wizard_b_aufklappen.setMaximumSize(QSize(20, 20))
        self.tb_wizard_b_aufklappen.setFont(font1)
        self.tb_wizard_b_aufklappen.setFocusPolicy(Qt.FocusPolicy.NoFocus)
#if QT_CONFIG(shortcut)
        self.tb_wizard_b_aufklappen.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.tb_wizard_b_aufklappen.setCheckable(True)
        self.tb_wizard_b_aufklappen.setChecked(True)
        self.tb_wizard_b_aufklappen.setAutoRaise(True)

        self.horizontalLayout_23.addWidget(self.tb_wizard_b_aufklappen)

        self.horizontalSpacer_42 = QSpacerItem(99, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_42)

        self.pb_wizard_b = QPushButton(self.wg_wizard_b_buttons)
        self.pb_wizard_b.setObjectName(u"pb_wizard_b")
        sizePolicy.setHeightForWidth(self.pb_wizard_b.sizePolicy().hasHeightForWidth())
        self.pb_wizard_b.setSizePolicy(sizePolicy)
        self.pb_wizard_b.setMinimumSize(QSize(70, 20))
        self.pb_wizard_b.setMaximumSize(QSize(100, 25))
        self.pb_wizard_b.setFont(font1)
        self.pb_wizard_b.setAutoDefault(True)

        self.horizontalLayout_23.addWidget(self.pb_wizard_b)

        self.horizontalSpacer_48 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_48)

        self.cb_auto_option_b = QComboBox(self.wg_wizard_b_buttons)
        self.cb_auto_option_b.addItem("")
        self.cb_auto_option_b.addItem("")
        self.cb_auto_option_b.addItem("")
        self.cb_auto_option_b.addItem("")
        self.cb_auto_option_b.setObjectName(u"cb_auto_option_b")
        self.cb_auto_option_b.setMinimumSize(QSize(170, 20))
        self.cb_auto_option_b.setMaximumSize(QSize(205, 25))

        self.horizontalLayout_23.addWidget(self.cb_auto_option_b)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_44)


        self.verticalLayout_4.addWidget(self.wg_wizard_b_buttons)

        self.wg_fertigtielmasse = QWidget(self.gb_automatisierung)
        self.wg_fertigtielmasse.setObjectName(u"wg_fertigtielmasse")
        sizePolicy.setHeightForWidth(self.wg_fertigtielmasse.sizePolicy().hasHeightForWidth())
        self.wg_fertigtielmasse.setSizePolicy(sizePolicy)
        self.wg_fertigtielmasse.setMinimumSize(QSize(300, 95))
        self.wg_fertigtielmasse.setMaximumSize(QSize(550, 180))
        self.formLayout = QFormLayout(self.wg_fertigtielmasse)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(-1, 5, -1, 0)
        self.wg_x_fertig = QWidget(self.wg_fertigtielmasse)
        self.wg_x_fertig.setObjectName(u"wg_x_fertig")
        self.wg_x_fertig.setMinimumSize(QSize(0, 20))
        self.wg_x_fertig.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_15 = QHBoxLayout(self.wg_x_fertig)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 1, -1, 1)
        self.lb_x_fertig = QLabel(self.wg_x_fertig)
        self.lb_x_fertig.setObjectName(u"lb_x_fertig")
        sizePolicy3.setHeightForWidth(self.lb_x_fertig.sizePolicy().hasHeightForWidth())
        self.lb_x_fertig.setSizePolicy(sizePolicy3)
        self.lb_x_fertig.setMinimumSize(QSize(0, 20))
        self.lb_x_fertig.setMaximumSize(QSize(200, 25))
        self.lb_x_fertig.setFont(font1)
        self.lb_x_fertig.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.lb_x_fertig)

        self.horizontalSpacer_28 = QSpacerItem(45, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_28)

        self.le_x_fertig = QLineEdit(self.wg_x_fertig)
        self.le_x_fertig.setObjectName(u"le_x_fertig")
        sizePolicy3.setHeightForWidth(self.le_x_fertig.sizePolicy().hasHeightForWidth())
        self.le_x_fertig.setSizePolicy(sizePolicy3)
        self.le_x_fertig.setMinimumSize(QSize(100, 20))
        self.le_x_fertig.setMaximumSize(QSize(150, 20))
        self.le_x_fertig.setFont(font1)

        self.horizontalLayout_15.addWidget(self.le_x_fertig)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_32)


        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.wg_x_fertig)

        self.wg_y_fertig = QWidget(self.wg_fertigtielmasse)
        self.wg_y_fertig.setObjectName(u"wg_y_fertig")
        self.wg_y_fertig.setMinimumSize(QSize(0, 20))
        self.wg_y_fertig.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_16 = QHBoxLayout(self.wg_y_fertig)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 1, -1, 1)
        self.lb_y_fertig = QLabel(self.wg_y_fertig)
        self.lb_y_fertig.setObjectName(u"lb_y_fertig")
        sizePolicy3.setHeightForWidth(self.lb_y_fertig.sizePolicy().hasHeightForWidth())
        self.lb_y_fertig.setSizePolicy(sizePolicy3)
        self.lb_y_fertig.setMinimumSize(QSize(0, 20))
        self.lb_y_fertig.setMaximumSize(QSize(200, 25))
        self.lb_y_fertig.setFont(font1)
        self.lb_y_fertig.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.lb_y_fertig)

        self.horizontalSpacer_29 = QSpacerItem(45, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_29)

        self.le_y_fertig = QLineEdit(self.wg_y_fertig)
        self.le_y_fertig.setObjectName(u"le_y_fertig")
        sizePolicy3.setHeightForWidth(self.le_y_fertig.sizePolicy().hasHeightForWidth())
        self.le_y_fertig.setSizePolicy(sizePolicy3)
        self.le_y_fertig.setMinimumSize(QSize(100, 20))
        self.le_y_fertig.setMaximumSize(QSize(150, 20))
        self.le_y_fertig.setFont(font1)

        self.horizontalLayout_16.addWidget(self.le_y_fertig)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_33)


        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.wg_y_fertig)

        self.wg_z_fertig = QWidget(self.wg_fertigtielmasse)
        self.wg_z_fertig.setObjectName(u"wg_z_fertig")
        self.wg_z_fertig.setMinimumSize(QSize(0, 20))
        self.wg_z_fertig.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_14 = QHBoxLayout(self.wg_z_fertig)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 1, -1, 1)
        self.lb_z_fertig = QLabel(self.wg_z_fertig)
        self.lb_z_fertig.setObjectName(u"lb_z_fertig")
        sizePolicy3.setHeightForWidth(self.lb_z_fertig.sizePolicy().hasHeightForWidth())
        self.lb_z_fertig.setSizePolicy(sizePolicy3)
        self.lb_z_fertig.setMinimumSize(QSize(0, 20))
        self.lb_z_fertig.setMaximumSize(QSize(200, 25))
        self.lb_z_fertig.setFont(font1)
        self.lb_z_fertig.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.lb_z_fertig)

        self.horizontalSpacer_30 = QSpacerItem(45, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_30)

        self.le_z_fertig = QLineEdit(self.wg_z_fertig)
        self.le_z_fertig.setObjectName(u"le_z_fertig")
        sizePolicy3.setHeightForWidth(self.le_z_fertig.sizePolicy().hasHeightForWidth())
        self.le_z_fertig.setSizePolicy(sizePolicy3)
        self.le_z_fertig.setMinimumSize(QSize(100, 20))
        self.le_z_fertig.setMaximumSize(QSize(150, 20))
        self.le_z_fertig.setFont(font1)

        self.horizontalLayout_14.addWidget(self.le_z_fertig)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_34)


        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.wg_z_fertig)

        self.wg_spanntiefe_b = QWidget(self.wg_fertigtielmasse)
        self.wg_spanntiefe_b.setObjectName(u"wg_spanntiefe_b")
        self.wg_spanntiefe_b.setMinimumSize(QSize(0, 20))
        self.wg_spanntiefe_b.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_17 = QHBoxLayout(self.wg_spanntiefe_b)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 1, -1, 1)
        self.lb_spanntiefe_b = QLabel(self.wg_spanntiefe_b)
        self.lb_spanntiefe_b.setObjectName(u"lb_spanntiefe_b")
        sizePolicy3.setHeightForWidth(self.lb_spanntiefe_b.sizePolicy().hasHeightForWidth())
        self.lb_spanntiefe_b.setSizePolicy(sizePolicy3)
        self.lb_spanntiefe_b.setMinimumSize(QSize(0, 20))
        self.lb_spanntiefe_b.setMaximumSize(QSize(200, 25))
        self.lb_spanntiefe_b.setFont(font1)
        self.lb_spanntiefe_b.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.lb_spanntiefe_b)

        self.horizontalSpacer_31 = QSpacerItem(52, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_31)

        self.le_spanntiefe_b = QLineEdit(self.wg_spanntiefe_b)
        self.le_spanntiefe_b.setObjectName(u"le_spanntiefe_b")
        sizePolicy3.setHeightForWidth(self.le_spanntiefe_b.sizePolicy().hasHeightForWidth())
        self.le_spanntiefe_b.setSizePolicy(sizePolicy3)
        self.le_spanntiefe_b.setMinimumSize(QSize(100, 20))
        self.le_spanntiefe_b.setMaximumSize(QSize(150, 20))
        self.le_spanntiefe_b.setFont(font1)
        self.le_spanntiefe_b.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.horizontalLayout_17.addWidget(self.le_spanntiefe_b)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_35)


        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.wg_spanntiefe_b)


        self.verticalLayout_4.addWidget(self.wg_fertigtielmasse)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.verticalLayout_8.addWidget(self.gb_automatisierung)

        self.gb_python_commander = QGroupBox(self.centralwidget)
        self.gb_python_commander.setObjectName(u"gb_python_commander")
        self.gb_python_commander.setMinimumSize(QSize(400, 120))
        self.gb_python_commander.setMaximumSize(QSize(16777215, 150))
        self.gb_python_commander.setFont(font1)
        self.gb_python_commander.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_5 = QVBoxLayout(self.gb_python_commander)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.wg_at_nummer = QWidget(self.gb_python_commander)
        self.wg_at_nummer.setObjectName(u"wg_at_nummer")
        self.wg_at_nummer.setMinimumSize(QSize(0, 20))
        self.wg_at_nummer.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_19 = QHBoxLayout(self.wg_at_nummer)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(9, 0, -1, 0)
        self.lb_at_nr = QLabel(self.wg_at_nummer)
        self.lb_at_nr.setObjectName(u"lb_at_nr")
        sizePolicy3.setHeightForWidth(self.lb_at_nr.sizePolicy().hasHeightForWidth())
        self.lb_at_nr.setSizePolicy(sizePolicy3)
        self.lb_at_nr.setMinimumSize(QSize(0, 20))
        self.lb_at_nr.setMaximumSize(QSize(200, 25))
        self.lb_at_nr.setFont(font1)
        self.lb_at_nr.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.lb_at_nr)

        self.horizontalSpacer_36 = QSpacerItem(89, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_36)

        self.le_at_nr = QLineEdit(self.wg_at_nummer)
        self.le_at_nr.setObjectName(u"le_at_nr")
        sizePolicy3.setHeightForWidth(self.le_at_nr.sizePolicy().hasHeightForWidth())
        self.le_at_nr.setSizePolicy(sizePolicy3)
        self.le_at_nr.setMinimumSize(QSize(100, 20))
        self.le_at_nr.setMaximumSize(QSize(150, 20))
        self.le_at_nr.setFont(font1)

        self.horizontalLayout_19.addWidget(self.le_at_nr)

        self.horizontalSpacer_24 = QSpacerItem(8, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_24)

        self.cbx_at_nr_editieren = QCheckBox(self.wg_at_nummer)
        self.cbx_at_nr_editieren.setObjectName(u"cbx_at_nr_editieren")
        self.cbx_at_nr_editieren.setMinimumSize(QSize(0, 20))
        self.cbx_at_nr_editieren.setMaximumSize(QSize(16777215, 25))
        self.cbx_at_nr_editieren.setFont(font1)
        self.cbx_at_nr_editieren.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_19.addWidget(self.cbx_at_nr_editieren)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_38)


        self.verticalLayout_5.addWidget(self.wg_at_nummer)

        self.wg_auftrags_nr = QWidget(self.gb_python_commander)
        self.wg_auftrags_nr.setObjectName(u"wg_auftrags_nr")
        self.wg_auftrags_nr.setMinimumSize(QSize(0, 20))
        self.wg_auftrags_nr.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_20 = QHBoxLayout(self.wg_auftrags_nr)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, 5)
        self.lb_auftrags_nr = QLabel(self.wg_auftrags_nr)
        self.lb_auftrags_nr.setObjectName(u"lb_auftrags_nr")
        sizePolicy3.setHeightForWidth(self.lb_auftrags_nr.sizePolicy().hasHeightForWidth())
        self.lb_auftrags_nr.setSizePolicy(sizePolicy3)
        self.lb_auftrags_nr.setMinimumSize(QSize(0, 20))
        self.lb_auftrags_nr.setMaximumSize(QSize(200, 25))
        self.lb_auftrags_nr.setFont(font1)
        self.lb_auftrags_nr.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.lb_auftrags_nr)

        self.horizontalSpacer_25 = QSpacerItem(28, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_25)

        self.le_auftrags_nr = QLineEdit(self.wg_auftrags_nr)
        self.le_auftrags_nr.setObjectName(u"le_auftrags_nr")
        sizePolicy3.setHeightForWidth(self.le_auftrags_nr.sizePolicy().hasHeightForWidth())
        self.le_auftrags_nr.setSizePolicy(sizePolicy3)
        self.le_auftrags_nr.setMinimumSize(QSize(100, 20))
        self.le_auftrags_nr.setMaximumSize(QSize(150, 20))
        self.le_auftrags_nr.setFont(font1)

        self.horizontalLayout_20.addWidget(self.le_auftrags_nr)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_37)


        self.verticalLayout_5.addWidget(self.wg_auftrags_nr)

        self.wg_programme_gefunden = QWidget(self.gb_python_commander)
        self.wg_programme_gefunden.setObjectName(u"wg_programme_gefunden")
        self.wg_programme_gefunden.setMinimumSize(QSize(0, 25))
        self.wg_programme_gefunden.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_21 = QHBoxLayout(self.wg_programme_gefunden)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_9 = QSpacerItem(118, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_9)

        self.pb_rausspielen = QPushButton(self.wg_programme_gefunden)
        self.pb_rausspielen.setObjectName(u"pb_rausspielen")
        self.pb_rausspielen.setMinimumSize(QSize(100, 20))
        self.pb_rausspielen.setMaximumSize(QSize(125, 25))
        self.pb_rausspielen.setFont(font1)
        self.pb_rausspielen.setAutoDefault(True)

        self.horizontalLayout_21.addWidget(self.pb_rausspielen)

        self.horizontalSpacer_26 = QSpacerItem(42, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_26)

        self.lcdn_programme_gefunden = QLCDNumber(self.wg_programme_gefunden)
        self.lcdn_programme_gefunden.setObjectName(u"lcdn_programme_gefunden")
        self.lcdn_programme_gefunden.setMinimumSize(QSize(0, 20))
        self.lcdn_programme_gefunden.setMaximumSize(QSize(30, 25))
        self.lcdn_programme_gefunden.setFont(font1)
        self.lcdn_programme_gefunden.setDigitCount(2)
        self.lcdn_programme_gefunden.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_21.addWidget(self.lcdn_programme_gefunden)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_27)


        self.verticalLayout_5.addWidget(self.wg_programme_gefunden)


        self.verticalLayout_8.addWidget(self.gb_python_commander)

        self.fr_scripts_aufklappen = QFrame(self.centralwidget)
        self.fr_scripts_aufklappen.setObjectName(u"fr_scripts_aufklappen")
        sizePolicy4.setHeightForWidth(self.fr_scripts_aufklappen.sizePolicy().hasHeightForWidth())
        self.fr_scripts_aufklappen.setSizePolicy(sizePolicy4)
        self.fr_scripts_aufklappen.setMinimumSize(QSize(0, 50))
        self.fr_scripts_aufklappen.setMaximumSize(QSize(16777215, 125))
        self.fr_scripts_aufklappen.setFont(font)
        self.fr_scripts_aufklappen.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_scripts_aufklappen.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.fr_scripts_aufklappen)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.wg_scripts_aufklappen = QWidget(self.fr_scripts_aufklappen)
        self.wg_scripts_aufklappen.setObjectName(u"wg_scripts_aufklappen")
        self.wg_scripts_aufklappen.setMinimumSize(QSize(0, 25))
        self.wg_scripts_aufklappen.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_18 = QHBoxLayout(self.wg_scripts_aufklappen)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.tb_scripts_aufklappen = QToolButton(self.wg_scripts_aufklappen)
        self.tb_scripts_aufklappen.setObjectName(u"tb_scripts_aufklappen")
        self.tb_scripts_aufklappen.setMinimumSize(QSize(20, 20))
        self.tb_scripts_aufklappen.setMaximumSize(QSize(20, 20))
        self.tb_scripts_aufklappen.setFocusPolicy(Qt.FocusPolicy.NoFocus)
#if QT_CONFIG(shortcut)
        self.tb_scripts_aufklappen.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.tb_scripts_aufklappen.setCheckable(True)
        self.tb_scripts_aufklappen.setChecked(True)
        self.tb_scripts_aufklappen.setAutoRaise(True)

        self.horizontalLayout_18.addWidget(self.tb_scripts_aufklappen)

        self.lb_scripts = QLabel(self.wg_scripts_aufklappen)
        self.lb_scripts.setObjectName(u"lb_scripts")
        self.lb_scripts.setFont(font)

        self.horizontalLayout_18.addWidget(self.lb_scripts)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_46)


        self.verticalLayout_6.addWidget(self.wg_scripts_aufklappen)

        self.fr_scripts = QFrame(self.fr_scripts_aufklappen)
        self.fr_scripts.setObjectName(u"fr_scripts")
        self.fr_scripts.setMinimumSize(QSize(0, 70))
        self.fr_scripts.setMaximumSize(QSize(16777215, 90))
        self.fr_scripts.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_scripts.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.fr_scripts)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.pb_prozess_oeffnen = QPushButton(self.fr_scripts)
        self.pb_prozess_oeffnen.setObjectName(u"pb_prozess_oeffnen")
        self.pb_prozess_oeffnen.setMinimumSize(QSize(80, 20))
        self.pb_prozess_oeffnen.setMaximumSize(QSize(130, 25))
        self.pb_prozess_oeffnen.setFont(font1)
        self.pb_prozess_oeffnen.setAutoDefault(True)

        self.gridLayout.addWidget(self.pb_prozess_oeffnen, 0, 0, 1, 1)

        self.pb_flet_prozess = QPushButton(self.fr_scripts)
        self.pb_flet_prozess.setObjectName(u"pb_flet_prozess")
        self.pb_flet_prozess.setMinimumSize(QSize(80, 20))
        self.pb_flet_prozess.setMaximumSize(QSize(130, 25))
        self.pb_flet_prozess.setFont(font1)
        self.pb_flet_prozess.setAutoDefault(True)

        self.gridLayout.addWidget(self.pb_flet_prozess, 1, 1, 1, 1)

        self.pb_error_closer = QPushButton(self.fr_scripts)
        self.pb_error_closer.setObjectName(u"pb_error_closer")
        self.pb_error_closer.setMinimumSize(QSize(80, 20))
        self.pb_error_closer.setMaximumSize(QSize(130, 25))
        self.pb_error_closer.setFont(font1)
        self.pb_error_closer.setAutoDefault(True)

        self.gridLayout.addWidget(self.pb_error_closer, 0, 1, 1, 1)

        self.pb_auto_speichern = QPushButton(self.fr_scripts)
        self.pb_auto_speichern.setObjectName(u"pb_auto_speichern")
        self.pb_auto_speichern.setMinimumSize(QSize(80, 20))
        self.pb_auto_speichern.setMaximumSize(QSize(130, 25))
        self.pb_auto_speichern.setFont(font1)
        self.pb_auto_speichern.setAutoDefault(True)

        self.gridLayout.addWidget(self.pb_auto_speichern, 0, 2, 1, 1)

        self.pb_esprit_start_makro = QPushButton(self.fr_scripts)
        self.pb_esprit_start_makro.setObjectName(u"pb_esprit_start_makro")
        self.pb_esprit_start_makro.setMinimumSize(QSize(80, 20))
        self.pb_esprit_start_makro.setMaximumSize(QSize(130, 25))
        self.pb_esprit_start_makro.setFont(font1)
        self.pb_esprit_start_makro.setAutoDefault(True)

        self.gridLayout.addWidget(self.pb_esprit_start_makro, 1, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.fr_scripts)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.verticalLayout_8.addWidget(self.fr_scripts_aufklappen)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        frm_main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 33))
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setObjectName(u"menuDatei")
        frm_main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_main_window)
        self.statusbar.setObjectName(u"statusbar")
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setKerning(True)
        font3.setHintingPreference(QFont.PreferFullHinting)
        self.statusbar.setFont(font3)
        self.statusbar.setStyleSheet(u"QStatusBar {\n"
"    color: green;             /* Textfarbe */\n"
"    font-weight: bold;\n"
"}")
        frm_main_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDatei.menuAction())
        self.menuDatei.addAction(self.actionEinstellungen)
        self.menuDatei.addAction(self.actionAktualisieren)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionBeenden)

        self.retranslateUi(frm_main_window)
        self.tb_spannmittel_aufklappen.clicked["bool"].connect(self.wg_datum_editieren.setHidden)
        self.cbx_datum_editieren.clicked["bool"].connect(self.le_pfad.setEnabled)
        self.actionBeenden.triggered.connect(frm_main_window.close)
        self.tb_scripts_aufklappen.clicked["bool"].connect(self.fr_scripts.setHidden)
        self.tb_wizard_b_aufklappen.clicked["bool"].connect(self.wg_fertigtielmasse.setHidden)
        self.tb_wizard_a_aufklappen.clicked["bool"].connect(self.wg_sleep_timer.setHidden)
        self.actionAktualisieren.triggered.connect(frm_main_window.update)
        self.cbx_at_nr_editieren.clicked["bool"].connect(self.le_at_nr.setEnabled)

        self.tw_rohteil_erstellen.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(frm_main_window)
    # setupUi

    def retranslateUi(self, frm_main_window):
        frm_main_window.setWindowTitle(QCoreApplication.translate("frm_main_window", u"BlankMaker", None))
        self.actionEinstellungen.setText(QCoreApplication.translate("frm_main_window", u"Einstellungen", None))
        self.actionBeenden.setText(QCoreApplication.translate("frm_main_window", u"Beenden", None))
        self.actionAktualisieren.setText(QCoreApplication.translate("frm_main_window", u"Aktualisieren", None))
        self.lb_rechteck_laenge.setText(QCoreApplication.translate("frm_main_window", u"L\u00e4nge X: ", None))
        self.le_rechteck_laenge.setText(QCoreApplication.translate("frm_main_window", u"100", None))
        self.lb_rechteck_breite.setText(QCoreApplication.translate("frm_main_window", u"Breite Y: ", None))
        self.le_rechteck_breite.setText(QCoreApplication.translate("frm_main_window", u"100", None))
        self.lb_rechteck_hoehe.setText(QCoreApplication.translate("frm_main_window", u"H\u00f6he Z:  ", None))
        self.le_rechteck_hoehe.setText(QCoreApplication.translate("frm_main_window", u"100", None))
        self.pb_rechteck.setText(QCoreApplication.translate("frm_main_window", u"Rechteck erstellen", None))
        self.tw_rohteil_erstellen.setTabText(self.tw_rohteil_erstellen.indexOf(self.tab_rechteck), QCoreApplication.translate("frm_main_window", u"Rechteck erstellen", None))
        self.lb_durchmesser.setText(QCoreApplication.translate("frm_main_window", u"Durchmesser:", None))
        self.le_durchmesser.setText(QCoreApplication.translate("frm_main_window", u"100", None))
        self.lb_kreis_hoehe.setText(QCoreApplication.translate("frm_main_window", u"H\u00f6he:             ", None))
        self.le_z_kreis.setText(QCoreApplication.translate("frm_main_window", u"100", None))
        self.pb_kreis.setText(QCoreApplication.translate("frm_main_window", u"Kreis erstellen", None))
        self.tw_rohteil_erstellen.setTabText(self.tw_rohteil_erstellen.indexOf(self.tab_kreis), QCoreApplication.translate("frm_main_window", u"Kreis erstellen", None))
        self.gb_spannmittel.setTitle(QCoreApplication.translate("frm_main_window", u"Spannmittel erstellen", None))
        self.lb_pfad.setText(QCoreApplication.translate("frm_main_window", u"Zielpfad:", None))
        self.le_pfad.setText(QCoreApplication.translate("frm_main_window", u"\"C:\\Users\\FALSCHERPFAD!!!!!!\"", None))
        self.cb_spannmittel.setPlaceholderText(QCoreApplication.translate("frm_main_window", u"Spannmittel ausw\u00e4hlen...", None))
        self.cb_bearbeitung_auswahl.setItemText(0, QCoreApplication.translate("frm_main_window", u"5 Achs 3 Achs", None))
        self.cb_bearbeitung_auswahl.setItemText(1, QCoreApplication.translate("frm_main_window", u"5 Achs 5 Achs", None))
        self.cb_bearbeitung_auswahl.setItemText(2, QCoreApplication.translate("frm_main_window", u"3 Achs 3 Achs", None))
        self.cb_bearbeitung_auswahl.setItemText(3, QCoreApplication.translate("frm_main_window", u"5 Achs", None))
        self.cb_bearbeitung_auswahl.setItemText(4, QCoreApplication.translate("frm_main_window", u"3 Achs", None))
        self.cb_bearbeitung_auswahl.setItemText(5, QCoreApplication.translate("frm_main_window", u"Magnet", None))
        self.cb_bearbeitung_auswahl.setItemText(6, QCoreApplication.translate("frm_main_window", u"Vorrichtung", None))

        self.lb_spannmittel_wert.setText(QCoreApplication.translate("frm_main_window", u"Spannmittelbreite:", None))
        self.le_spannmittel.setText(QCoreApplication.translate("frm_main_window", u"100", None))
        self.tb_spannmittel_aufklappen.setText(QCoreApplication.translate("frm_main_window", u"...", None))
        self.pb_spannmittel.setText(QCoreApplication.translate("frm_main_window", u"Spannmittel erstellen", None))
        self.cbx_datum_editieren.setText(QCoreApplication.translate("frm_main_window", u"Zielpfad editieren", None))
        self.gb_automatisierung.setTitle(QCoreApplication.translate("frm_main_window", u"Automatisierung", None))
        self.lb_zeichnungsnr.setText(QCoreApplication.translate("frm_main_window", u"Zeichnungsnummer:", None))
        self.le_zeichnungsnr.setText(QCoreApplication.translate("frm_main_window", u"24T0004580", None))
        self.tb_wizard_a_aufklappen.setText(QCoreApplication.translate("frm_main_window", u"...", None))
        self.pb_wizard_a.setText(QCoreApplication.translate("frm_main_window", u"Wizard_A", None))
        self.cb_auto_option_a.setItemText(0, QCoreApplication.translate("frm_main_window", u"Gandalf", None))
        self.cb_auto_option_a.setItemText(1, QCoreApplication.translate("frm_main_window", u"Gandalf Fmax", None))
        self.cb_auto_option_a.setItemText(2, QCoreApplication.translate("frm_main_window", u"Ausf\u00fcllhilfe", None))
        self.cb_auto_option_a.setItemText(3, QCoreApplication.translate("frm_main_window", u"Bounding Box auslesen", None))

        self.lb_sleep_timer.setText(QCoreApplication.translate("frm_main_window", u"Sleep Timer", None))
        self.tb_wizard_b_aufklappen.setText(QCoreApplication.translate("frm_main_window", u"...", None))
        self.pb_wizard_b.setText(QCoreApplication.translate("frm_main_window", u"Wizard_B", None))
        self.cb_auto_option_b.setItemText(0, QCoreApplication.translate("frm_main_window", u"Saruman", None))
        self.cb_auto_option_b.setItemText(1, QCoreApplication.translate("frm_main_window", u"Saruman light", None))
        self.cb_auto_option_b.setItemText(2, QCoreApplication.translate("frm_main_window", u"Ausf\u00fcllhilfe B", None))
        self.cb_auto_option_b.setItemText(3, QCoreApplication.translate("frm_main_window", u"Bounding Box auslesen B", None))

        self.lb_x_fertig.setText(QCoreApplication.translate("frm_main_window", u"Fertigma\u00df X:", None))
        self.le_x_fertig.setText(QCoreApplication.translate("frm_main_window", u"100", None))
        self.lb_y_fertig.setText(QCoreApplication.translate("frm_main_window", u"Fertigma\u00df Y:", None))
        self.le_y_fertig.setText(QCoreApplication.translate("frm_main_window", u"100", None))
        self.lb_z_fertig.setText(QCoreApplication.translate("frm_main_window", u"Fertigma\u00df Z:", None))
        self.le_z_fertig.setText(QCoreApplication.translate("frm_main_window", u"100", None))
        self.lb_spanntiefe_b.setText(QCoreApplication.translate("frm_main_window", u"Spanntiefe:", None))
        self.le_spanntiefe_b.setText(QCoreApplication.translate("frm_main_window", u"5", None))
        self.gb_python_commander.setTitle(QCoreApplication.translate("frm_main_window", u"Python Commander", None))
        self.lb_at_nr.setText(QCoreApplication.translate("frm_main_window", u"AT-...", None))
        self.le_at_nr.setText(QCoreApplication.translate("frm_main_window", u"25", None))
        self.cbx_at_nr_editieren.setText(QCoreApplication.translate("frm_main_window", u"editieren", None))
        self.lb_auftrags_nr.setText(QCoreApplication.translate("frm_main_window", u"Auftragsnummer:", None))
        self.le_auftrags_nr.setText(QCoreApplication.translate("frm_main_window", u"0815", None))
        self.pb_rausspielen.setText(QCoreApplication.translate("frm_main_window", u"Starten", None))
        self.tb_scripts_aufklappen.setText(QCoreApplication.translate("frm_main_window", u"...", None))
        self.lb_scripts.setText(QCoreApplication.translate("frm_main_window", u"Externe Programme", None))
        self.pb_prozess_oeffnen.setText(QCoreApplication.translate("frm_main_window", u"Prozess \u00f6ffnen", None))
        self.pb_flet_prozess.setText(QCoreApplication.translate("frm_main_window", u"Flet Prozess", None))
        self.pb_error_closer.setText(QCoreApplication.translate("frm_main_window", u"Fehler Eliminator", None))
        self.pb_auto_speichern.setText(QCoreApplication.translate("frm_main_window", u"Auto Speichern", None))
        self.pb_esprit_start_makro.setText(QCoreApplication.translate("frm_main_window", u"Esprit Start Makro", None))
        self.menuDatei.setTitle(QCoreApplication.translate("frm_main_window", u"Datei", None))
    # retranslateUi

