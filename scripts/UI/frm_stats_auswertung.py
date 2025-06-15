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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QStackedWidget, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_frm_stats_auswertung(object):
    def setupUi(self, frm_stats_auswertung):
        if not frm_stats_auswertung.objectName():
            frm_stats_auswertung.setObjectName(u"frm_stats_auswertung")
        frm_stats_auswertung.resize(800, 600)
        self.centralwidget = QWidget(frm_stats_auswertung)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sw_main = QStackedWidget(self.centralwidget)
        self.sw_main.setObjectName(u"sw_main")
        self.sw_main.setGeometry(QRect(70, 40, 671, 401))
        self.page_zeit = QWidget()
        self.page_zeit.setObjectName(u"page_zeit")
        self.verticalLayout = QVBoxLayout(self.page_zeit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_zeitersparnis = QLabel(self.page_zeit)
        self.lb_zeitersparnis.setObjectName(u"lb_zeitersparnis")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lb_zeitersparnis.setFont(font)
        self.lb_zeitersparnis.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lb_zeitersparnis)

        self.tv_zeit = QTableView(self.page_zeit)
        self.tv_zeit.setObjectName(u"tv_zeit")

        self.verticalLayout.addWidget(self.tv_zeit)

        self.sw_main.addWidget(self.page_zeit)
        self.page_rohteil = QWidget()
        self.page_rohteil.setObjectName(u"page_rohteil")
        self.verticalLayout_2 = QVBoxLayout(self.page_rohteil)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_rohteil = QLabel(self.page_rohteil)
        self.lb_rohteil.setObjectName(u"lb_rohteil")
        self.lb_rohteil.setFont(font)
        self.lb_rohteil.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_rohteil)

        self.tv_rohteil = QTableView(self.page_rohteil)
        self.tv_rohteil.setObjectName(u"tv_rohteil")

        self.verticalLayout_2.addWidget(self.tv_rohteil)

        self.sw_main.addWidget(self.page_rohteil)
        frm_stats_auswertung.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_stats_auswertung)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        frm_stats_auswertung.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_stats_auswertung)
        self.statusbar.setObjectName(u"statusbar")
        frm_stats_auswertung.setStatusBar(self.statusbar)

        self.retranslateUi(frm_stats_auswertung)

        self.sw_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(frm_stats_auswertung)
    # setupUi

    def retranslateUi(self, frm_stats_auswertung):
        frm_stats_auswertung.setWindowTitle(QCoreApplication.translate("frm_stats_auswertung", u"Statistiken auswerten", None))
        self.lb_zeitersparnis.setText(QCoreApplication.translate("frm_stats_auswertung", u"Zeitersparnis", None))
        self.lb_rohteil.setText(QCoreApplication.translate("frm_stats_auswertung", u"Rohmaterial Fehler", None))
    # retranslateUi

