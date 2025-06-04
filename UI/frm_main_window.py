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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_frm_main_window(object):
    def setupUi(self, frm_main_window):
        if not frm_main_window.objectName():
            frm_main_window.setObjectName(u"frm_main_window")
        frm_main_window.resize(470, 600)
        frm_main_window.setMinimumSize(QSize(470, 600))
        self.centralwidget = QWidget(frm_main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tw_rohteil_erstellen = QTabWidget(self.centralwidget)
        self.tw_rohteil_erstellen.setObjectName(u"tw_rohteil_erstellen")
        self.tw_rohteil_erstellen.setMinimumSize(QSize(450, 225))
        self.tw_rohteil_erstellen.setMaximumSize(QSize(16777215, 300))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(12)
        font.setBold(False)
        self.tw_rohteil_erstellen.setFont(font)
        self.tw_rohteil_erstellen.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tab_rechteck = QWidget()
        self.tab_rechteck.setObjectName(u"tab_rechteck")
        self.verticalLayout = QVBoxLayout(self.tab_rechteck)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.wg_x_roh = QWidget(self.tab_rechteck)
        self.wg_x_roh.setObjectName(u"wg_x_roh")
        self.horizontalLayout = QHBoxLayout(self.wg_x_roh)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_rechteck_laenge = QLabel(self.wg_x_roh)
        self.lb_rechteck_laenge.setObjectName(u"lb_rechteck_laenge")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_rechteck_laenge.sizePolicy().hasHeightForWidth())
        self.lb_rechteck_laenge.setSizePolicy(sizePolicy)
        self.lb_rechteck_laenge.setMaximumSize(QSize(200, 50))
        self.lb_rechteck_laenge.setFont(font)
        self.lb_rechteck_laenge.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lb_rechteck_laenge)

        self.horizontalSpacer_14 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_14)

        self.le_rechteck_laenge = QLineEdit(self.wg_x_roh)
        self.le_rechteck_laenge.setObjectName(u"le_rechteck_laenge")
        sizePolicy.setHeightForWidth(self.le_rechteck_laenge.sizePolicy().hasHeightForWidth())
        self.le_rechteck_laenge.setSizePolicy(sizePolicy)
        self.le_rechteck_laenge.setMinimumSize(QSize(100, 30))
        self.le_rechteck_laenge.setMaximumSize(QSize(150, 50))
        self.le_rechteck_laenge.setFont(font)

        self.horizontalLayout.addWidget(self.le_rechteck_laenge)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_17)


        self.verticalLayout.addWidget(self.wg_x_roh)

        self.wg_y_roh = QWidget(self.tab_rechteck)
        self.wg_y_roh.setObjectName(u"wg_y_roh")
        self.horizontalLayout_2 = QHBoxLayout(self.wg_y_roh)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_rechteck_breite = QLabel(self.wg_y_roh)
        self.lb_rechteck_breite.setObjectName(u"lb_rechteck_breite")
        sizePolicy.setHeightForWidth(self.lb_rechteck_breite.sizePolicy().hasHeightForWidth())
        self.lb_rechteck_breite.setSizePolicy(sizePolicy)
        self.lb_rechteck_breite.setMaximumSize(QSize(200, 50))
        self.lb_rechteck_breite.setFont(font)
        self.lb_rechteck_breite.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lb_rechteck_breite)

        self.horizontalSpacer_15 = QSpacerItem(76, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_15)

        self.le_rechteck_breite = QLineEdit(self.wg_y_roh)
        self.le_rechteck_breite.setObjectName(u"le_rechteck_breite")
        sizePolicy.setHeightForWidth(self.le_rechteck_breite.sizePolicy().hasHeightForWidth())
        self.le_rechteck_breite.setSizePolicy(sizePolicy)
        self.le_rechteck_breite.setMinimumSize(QSize(100, 30))
        self.le_rechteck_breite.setMaximumSize(QSize(150, 50))
        self.le_rechteck_breite.setFont(font)

        self.horizontalLayout_2.addWidget(self.le_rechteck_breite)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_18)


        self.verticalLayout.addWidget(self.wg_y_roh)

        self.wg_z_roh = QWidget(self.tab_rechteck)
        self.wg_z_roh.setObjectName(u"wg_z_roh")
        self.horizontalLayout_3 = QHBoxLayout(self.wg_z_roh)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_rechteck_hoehe = QLabel(self.wg_z_roh)
        self.lb_rechteck_hoehe.setObjectName(u"lb_rechteck_hoehe")
        sizePolicy.setHeightForWidth(self.lb_rechteck_hoehe.sizePolicy().hasHeightForWidth())
        self.lb_rechteck_hoehe.setSizePolicy(sizePolicy)
        self.lb_rechteck_hoehe.setMaximumSize(QSize(200, 50))
        self.lb_rechteck_hoehe.setFont(font)
        self.lb_rechteck_hoehe.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lb_rechteck_hoehe)

        self.horizontalSpacer_16 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_16)

        self.le_rechteck_hoehe = QLineEdit(self.wg_z_roh)
        self.le_rechteck_hoehe.setObjectName(u"le_rechteck_hoehe")
        sizePolicy.setHeightForWidth(self.le_rechteck_hoehe.sizePolicy().hasHeightForWidth())
        self.le_rechteck_hoehe.setSizePolicy(sizePolicy)
        self.le_rechteck_hoehe.setMinimumSize(QSize(100, 30))
        self.le_rechteck_hoehe.setMaximumSize(QSize(150, 50))
        self.le_rechteck_hoehe.setFont(font)

        self.horizontalLayout_3.addWidget(self.le_rechteck_hoehe)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_19)


        self.verticalLayout.addWidget(self.wg_z_roh)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.wg_button_roh = QWidget(self.tab_rechteck)
        self.wg_button_roh.setObjectName(u"wg_button_roh")
        self.horizontalLayout_4 = QHBoxLayout(self.wg_button_roh)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(151, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pb_rechteck = QPushButton(self.wg_button_roh)
        self.pb_rechteck.setObjectName(u"pb_rechteck")
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.pb_rechteck.setFont(font1)
        self.pb_rechteck.setAutoDefault(True)

        self.horizontalLayout_4.addWidget(self.pb_rechteck)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.wg_button_roh)

        self.tw_rohteil_erstellen.addTab(self.tab_rechteck, "")
        self.tab_kreis = QWidget()
        self.tab_kreis.setObjectName(u"tab_kreis")
        self.verticalLayout_2 = QVBoxLayout(self.tab_kreis)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.wg_durchmesser = QWidget(self.tab_kreis)
        self.wg_durchmesser.setObjectName(u"wg_durchmesser")
        self.horizontalLayout_7 = QHBoxLayout(self.wg_durchmesser)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_durchmesser = QLabel(self.wg_durchmesser)
        self.lb_durchmesser.setObjectName(u"lb_durchmesser")
        self.lb_durchmesser.setMaximumSize(QSize(200, 50))
        self.lb_durchmesser.setFont(font)
        self.lb_durchmesser.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lb_durchmesser)

        self.horizontalSpacer_20 = QSpacerItem(48, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_20)

        self.le_durchmesser = QLineEdit(self.wg_durchmesser)
        self.le_durchmesser.setObjectName(u"le_durchmesser")
        sizePolicy.setHeightForWidth(self.le_durchmesser.sizePolicy().hasHeightForWidth())
        self.le_durchmesser.setSizePolicy(sizePolicy)
        self.le_durchmesser.setMinimumSize(QSize(100, 30))
        self.le_durchmesser.setMaximumSize(QSize(150, 50))
        self.le_durchmesser.setFont(font)

        self.horizontalLayout_7.addWidget(self.le_durchmesser)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_22)


        self.verticalLayout_2.addWidget(self.wg_durchmesser)

        self.wg_z_kreis = QWidget(self.tab_kreis)
        self.wg_z_kreis.setObjectName(u"wg_z_kreis")
        self.horizontalLayout_6 = QHBoxLayout(self.wg_z_kreis)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_kreis_hoehe = QLabel(self.wg_z_kreis)
        self.lb_kreis_hoehe.setObjectName(u"lb_kreis_hoehe")
        self.lb_kreis_hoehe.setMaximumSize(QSize(200, 50))
        self.lb_kreis_hoehe.setFont(font)
        self.lb_kreis_hoehe.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.lb_kreis_hoehe)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_21)

        self.le_z_kreis = QLineEdit(self.wg_z_kreis)
        self.le_z_kreis.setObjectName(u"le_z_kreis")
        sizePolicy.setHeightForWidth(self.le_z_kreis.sizePolicy().hasHeightForWidth())
        self.le_z_kreis.setSizePolicy(sizePolicy)
        self.le_z_kreis.setMinimumSize(QSize(100, 30))
        self.le_z_kreis.setMaximumSize(QSize(150, 50))
        self.le_z_kreis.setFont(font)

        self.horizontalLayout_6.addWidget(self.le_z_kreis)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_23)


        self.verticalLayout_2.addWidget(self.wg_z_kreis)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.wg_button_kreis = QWidget(self.tab_kreis)
        self.wg_button_kreis.setObjectName(u"wg_button_kreis")
        self.horizontalLayout_5 = QHBoxLayout(self.wg_button_kreis)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(158, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.pb_kreis = QPushButton(self.wg_button_kreis)
        self.pb_kreis.setObjectName(u"pb_kreis")
        self.pb_kreis.setFont(font1)

        self.horizontalLayout_5.addWidget(self.pb_kreis)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.wg_button_kreis)

        self.tw_rohteil_erstellen.addTab(self.tab_kreis, "")

        self.verticalLayout_4.addWidget(self.tw_rohteil_erstellen)

        self.gb_spannmittel = QGroupBox(self.centralwidget)
        self.gb_spannmittel.setObjectName(u"gb_spannmittel")
        self.gb_spannmittel.setMinimumSize(QSize(450, 120))
        self.gb_spannmittel.setMaximumSize(QSize(16777215, 300))
        self.gb_spannmittel.setFont(font)
        self.gb_spannmittel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_3 = QVBoxLayout(self.gb_spannmittel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.wg_zielpfad = QWidget(self.gb_spannmittel)
        self.wg_zielpfad.setObjectName(u"wg_zielpfad")
        self.horizontalLayout_10 = QHBoxLayout(self.wg_zielpfad)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lb_pfad = QLabel(self.wg_zielpfad)
        self.lb_pfad.setObjectName(u"lb_pfad")
        sizePolicy.setHeightForWidth(self.lb_pfad.sizePolicy().hasHeightForWidth())
        self.lb_pfad.setSizePolicy(sizePolicy)
        self.lb_pfad.setMaximumSize(QSize(200, 200))
        self.lb_pfad.setFont(font)
        self.lb_pfad.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lb_pfad)

        self.horizontalSpacer_8 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.le_pfad = QLineEdit(self.wg_zielpfad)
        self.le_pfad.setObjectName(u"le_pfad")
        self.le_pfad.setMinimumSize(QSize(400, 0))
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.le_pfad.setFont(font2)

        self.horizontalLayout_10.addWidget(self.le_pfad)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_24)


        self.verticalLayout_3.addWidget(self.wg_zielpfad)

        self.wg_spannmittel_erstellen = QWidget(self.gb_spannmittel)
        self.wg_spannmittel_erstellen.setObjectName(u"wg_spannmittel_erstellen")
        self.horizontalLayout_9 = QHBoxLayout(self.wg_spannmittel_erstellen)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.tb_spannmittel_aufklappen = QToolButton(self.wg_spannmittel_erstellen)
        self.tb_spannmittel_aufklappen.setObjectName(u"tb_spannmittel_aufklappen")
        self.tb_spannmittel_aufklappen.setFocusPolicy(Qt.FocusPolicy.NoFocus)
#if QT_CONFIG(shortcut)
        self.tb_spannmittel_aufklappen.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.tb_spannmittel_aufklappen.setCheckable(True)
        self.tb_spannmittel_aufklappen.setChecked(True)
        self.tb_spannmittel_aufklappen.setAutoRaise(True)

        self.horizontalLayout_9.addWidget(self.tb_spannmittel_aufklappen)

        self.horizontalSpacer_6 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.pb_spannmittel = QPushButton(self.wg_spannmittel_erstellen)
        self.pb_spannmittel.setObjectName(u"pb_spannmittel")
        self.pb_spannmittel.setFont(font1)
        self.pb_spannmittel.setAutoDefault(True)

        self.horizontalLayout_9.addWidget(self.pb_spannmittel)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)


        self.verticalLayout_3.addWidget(self.wg_spannmittel_erstellen)

        self.line = QFrame(self.gb_spannmittel)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.wg_datum_editieren = QWidget(self.gb_spannmittel)
        self.wg_datum_editieren.setObjectName(u"wg_datum_editieren")
        self.horizontalLayout_8 = QHBoxLayout(self.wg_datum_editieren)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cb_datum_editieren = QCheckBox(self.wg_datum_editieren)
        self.cb_datum_editieren.setObjectName(u"cb_datum_editieren")
        self.cb_datum_editieren.setFont(font)

        self.horizontalLayout_8.addWidget(self.cb_datum_editieren)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.de_datum = QDateEdit(self.wg_datum_editieren)
        self.de_datum.setObjectName(u"de_datum")
        self.de_datum.setMinimumDate(QDate(2012, 9, 14))
        self.de_datum.setCalendarPopup(True)
        self.de_datum.setCurrentSectionIndex(0)
        self.de_datum.setTimeSpec(Qt.TimeSpec.LocalTime)
        self.de_datum.setDate(QDate(2025, 6, 4))

        self.horizontalLayout_8.addWidget(self.de_datum)


        self.verticalLayout_3.addWidget(self.wg_datum_editieren)


        self.verticalLayout_4.addWidget(self.gb_spannmittel)

        frm_main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 470, 22))
        frm_main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_main_window)
        self.statusbar.setObjectName(u"statusbar")
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setHintingPreference(QFont.PreferFullHinting)
        self.statusbar.setFont(font3)
        self.statusbar.setStyleSheet(u"QStatusBar {\n"
"    color: green;             /* Textfarbe */\n"
"    font-weight: bold;\n"
"}")
        frm_main_window.setStatusBar(self.statusbar)

        self.retranslateUi(frm_main_window)
        self.tb_spannmittel_aufklappen.clicked["bool"].connect(self.wg_datum_editieren.setHidden)
        self.cb_datum_editieren.clicked["bool"].connect(self.le_pfad.setEnabled)

        self.tw_rohteil_erstellen.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(frm_main_window)
    # setupUi

    def retranslateUi(self, frm_main_window):
        frm_main_window.setWindowTitle(QCoreApplication.translate("frm_main_window", u"MainWindow", None))
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
        self.le_pfad.setText(QCoreApplication.translate("frm_main_window", u"\"C:\\Users\\Ismail\\Pictures\\\"", None))
        self.tb_spannmittel_aufklappen.setText(QCoreApplication.translate("frm_main_window", u"...", None))
        self.pb_spannmittel.setText(QCoreApplication.translate("frm_main_window", u"Spannmittel erstellen", None))
        self.cb_datum_editieren.setText(QCoreApplication.translate("frm_main_window", u"Zielpfad editieren", None))
    # retranslateUi

