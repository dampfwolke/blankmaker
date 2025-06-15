# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_stats_auswertung.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_frm_stats_auswertung(object):
    def setupUi(self, frm_stats_auswertung):
        if not frm_stats_auswertung.objectName():
            frm_stats_auswertung.setObjectName(u"frm_stats_auswertung")
        frm_stats_auswertung.resize(1380, 883)
        self.centralwidget = QWidget(frm_stats_auswertung)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tw_main = QTabWidget(self.centralwidget)
        self.tw_main.setObjectName(u"tw_main")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.tw_main.setFont(font)
        self.tab_zeit = QWidget()
        self.tab_zeit.setObjectName(u"tab_zeit")
        self.verticalLayout = QVBoxLayout(self.tab_zeit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_zeitersparnis = QLabel(self.tab_zeit)
        self.lb_zeitersparnis.setObjectName(u"lb_zeitersparnis")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_zeitersparnis.sizePolicy().hasHeightForWidth())
        self.lb_zeitersparnis.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.lb_zeitersparnis.setFont(font1)
        self.lb_zeitersparnis.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lb_zeitersparnis)

        self.tv_zeit = QTableView(self.tab_zeit)
        self.tv_zeit.setObjectName(u"tv_zeit")
        self.tv_zeit.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tv_zeit.setTabKeyNavigation(True)
        self.tv_zeit.setDragEnabled(True)
        self.tv_zeit.setDragDropOverwriteMode(False)

        self.verticalLayout.addWidget(self.tv_zeit)

        self.wg_buttons_zeit = QWidget(self.tab_zeit)
        self.wg_buttons_zeit.setObjectName(u"wg_buttons_zeit")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.wg_buttons_zeit.setFont(font2)
        self.horizontalLayout = QHBoxLayout(self.wg_buttons_zeit)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_aktualisieren_zeit = QPushButton(self.wg_buttons_zeit)
        self.pb_aktualisieren_zeit.setObjectName(u"pb_aktualisieren_zeit")

        self.horizontalLayout.addWidget(self.pb_aktualisieren_zeit)

        self.pb_auswerten_zeit = QPushButton(self.wg_buttons_zeit)
        self.pb_auswerten_zeit.setObjectName(u"pb_auswerten_zeit")

        self.horizontalLayout.addWidget(self.pb_auswerten_zeit)


        self.verticalLayout.addWidget(self.wg_buttons_zeit)

        self.lb_zeit_ausgabe = QLabel(self.tab_zeit)
        self.lb_zeit_ausgabe.setObjectName(u"lb_zeit_ausgabe")
        self.lb_zeit_ausgabe.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.lb_zeit_ausgabe)

        self.tw_main.addTab(self.tab_zeit, "")
        self.tab_rohmaterial = QWidget()
        self.tab_rohmaterial.setObjectName(u"tab_rohmaterial")
        self.verticalLayout_3 = QVBoxLayout(self.tab_rohmaterial)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lb_rohteil = QLabel(self.tab_rohmaterial)
        self.lb_rohteil.setObjectName(u"lb_rohteil")
        self.lb_rohteil.setFont(font1)
        self.lb_rohteil.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lb_rohteil)

        self.tv_rohteil = QTableView(self.tab_rohmaterial)
        self.tv_rohteil.setObjectName(u"tv_rohteil")

        self.verticalLayout_3.addWidget(self.tv_rohteil)

        self.wg_buttons_roh = QWidget(self.tab_rohmaterial)
        self.wg_buttons_roh.setObjectName(u"wg_buttons_roh")
        self.wg_buttons_roh.setFont(font2)
        self.horizontalLayout_2 = QHBoxLayout(self.wg_buttons_roh)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_aktualisieren_roh = QPushButton(self.wg_buttons_roh)
        self.pb_aktualisieren_roh.setObjectName(u"pb_aktualisieren_roh")

        self.horizontalLayout_2.addWidget(self.pb_aktualisieren_roh)

        self.pb_auswerten_roh = QPushButton(self.wg_buttons_roh)
        self.pb_auswerten_roh.setObjectName(u"pb_auswerten_roh")

        self.horizontalLayout_2.addWidget(self.pb_auswerten_roh)


        self.verticalLayout_3.addWidget(self.wg_buttons_roh)

        self.lb_roh_ausgabe = QLabel(self.tab_rohmaterial)
        self.lb_roh_ausgabe.setObjectName(u"lb_roh_ausgabe")

        self.verticalLayout_3.addWidget(self.lb_roh_ausgabe)

        self.tw_main.addTab(self.tab_rohmaterial, "")

        self.verticalLayout_2.addWidget(self.tw_main)

        frm_stats_auswertung.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_stats_auswertung)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1380, 33))
        frm_stats_auswertung.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_stats_auswertung)
        self.statusbar.setObjectName(u"statusbar")
        frm_stats_auswertung.setStatusBar(self.statusbar)

        self.retranslateUi(frm_stats_auswertung)

        self.tw_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(frm_stats_auswertung)
    # setupUi

    def retranslateUi(self, frm_stats_auswertung):
        frm_stats_auswertung.setWindowTitle(QCoreApplication.translate("frm_stats_auswertung", u"Statistiken auswerten", None))
        self.lb_zeitersparnis.setText(QCoreApplication.translate("frm_stats_auswertung", u"Zeitersparnis", None))
        self.pb_aktualisieren_zeit.setText(QCoreApplication.translate("frm_stats_auswertung", u"Aktualisieren", None))
        self.pb_auswerten_zeit.setText(QCoreApplication.translate("frm_stats_auswertung", u"Auswerten", None))
        self.lb_zeit_ausgabe.setText(QCoreApplication.translate("frm_stats_auswertung", u"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", None))
        self.tw_main.setTabText(self.tw_main.indexOf(self.tab_zeit), QCoreApplication.translate("frm_stats_auswertung", u"Zeitersparnis", None))
        self.lb_rohteil.setText(QCoreApplication.translate("frm_stats_auswertung", u"Rohmaterial Fehler", None))
        self.pb_aktualisieren_roh.setText(QCoreApplication.translate("frm_stats_auswertung", u"Aktualisieren", None))
        self.pb_auswerten_roh.setText(QCoreApplication.translate("frm_stats_auswertung", u"Auswerten", None))
        self.lb_roh_ausgabe.setText(QCoreApplication.translate("frm_stats_auswertung", u"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", None))
        self.tw_main.setTabText(self.tw_main.indexOf(self.tab_rohmaterial), QCoreApplication.translate("frm_stats_auswertung", u"Rohmaterial", None))
    # retranslateUi

