# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_frm_settings(object):
    def setupUi(self, frm_settings):
        if not frm_settings.objectName():
            frm_settings.setObjectName(u"frm_settings")
        frm_settings.setWindowModality(Qt.WindowModality.ApplicationModal)
        frm_settings.resize(650, 803)
        frm_settings.setMinimumSize(QSize(650, 680))
        frm_settings.setMaximumSize(QSize(650, 1200))
        icon = QIcon()
        icon.addFile(u":/Buttons/download.png", QSize(), QIcon.Normal, QIcon.Off)
        frm_settings.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(frm_settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.wg_title = QWidget(frm_settings)
        self.wg_title.setObjectName(u"wg_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wg_title.sizePolicy().hasHeightForWidth())
        self.wg_title.setSizePolicy(sizePolicy)
        self.wg_title.setMinimumSize(QSize(500, 60))
        self.wg_title.setMaximumSize(QSize(500, 60))
        self.horizontalLayout = QHBoxLayout(self.wg_title)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_title_text = QLabel(self.wg_title)
        self.lb_title_text.setObjectName(u"lb_title_text")
        self.lb_title_text.setMinimumSize(QSize(200, 50))
        self.lb_title_text.setMaximumSize(QSize(400, 60))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(16)
        font.setBold(True)
        self.lb_title_text.setFont(font)
        self.lb_title_text.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lb_title_text)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.wg_title)

        self.wg_formular = QWidget(frm_settings)
        self.wg_formular.setObjectName(u"wg_formular")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wg_formular.sizePolicy().hasHeightForWidth())
        self.wg_formular.setSizePolicy(sizePolicy1)
        self.wg_formular.setMinimumSize(QSize(500, 300))
        self.wg_formular.setMaximumSize(QSize(800, 1000))
        font1 = QFont()
        font1.setPointSize(10)
        self.wg_formular.setFont(font1)
        self.formLayout = QFormLayout(self.wg_formular)
        self.formLayout.setObjectName(u"formLayout")
        self.lb_nc_base_path = QLabel(self.wg_formular)
        self.lb_nc_base_path.setObjectName(u"lb_nc_base_path")
        self.lb_nc_base_path.setMinimumSize(QSize(130, 35))
        self.lb_nc_base_path.setMaximumSize(QSize(250, 50))
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.lb_nc_base_path.setFont(font2)
        self.lb_nc_base_path.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lb_nc_base_path)

        self.le_nc_base_path = QLineEdit(self.wg_formular)
        self.le_nc_base_path.setObjectName(u"le_nc_base_path")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_nc_base_path.sizePolicy().hasHeightForWidth())
        self.le_nc_base_path.setSizePolicy(sizePolicy2)
        self.le_nc_base_path.setMinimumSize(QSize(330, 35))
        self.le_nc_base_path.setMaximumSize(QSize(900, 50))
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(12)
        self.le_nc_base_path.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_nc_base_path)

        self.lb_spannmittel_basis_pfad = QLabel(self.wg_formular)
        self.lb_spannmittel_basis_pfad.setObjectName(u"lb_spannmittel_basis_pfad")
        self.lb_spannmittel_basis_pfad.setMinimumSize(QSize(135, 35))
        self.lb_spannmittel_basis_pfad.setMaximumSize(QSize(250, 50))
        self.lb_spannmittel_basis_pfad.setFont(font2)
        self.lb_spannmittel_basis_pfad.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lb_spannmittel_basis_pfad)

        self.le_spannmittel_basis_pfad = QLineEdit(self.wg_formular)
        self.le_spannmittel_basis_pfad.setObjectName(u"le_spannmittel_basis_pfad")
        sizePolicy2.setHeightForWidth(self.le_spannmittel_basis_pfad.sizePolicy().hasHeightForWidth())
        self.le_spannmittel_basis_pfad.setSizePolicy(sizePolicy2)
        self.le_spannmittel_basis_pfad.setMinimumSize(QSize(330, 35))
        self.le_spannmittel_basis_pfad.setMaximumSize(QSize(900, 50))
        self.le_spannmittel_basis_pfad.setFont(font3)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_spannmittel_basis_pfad)

        self.lb_wks = QLabel(self.wg_formular)
        self.lb_wks.setObjectName(u"lb_wks")
        self.lb_wks.setMinimumSize(QSize(130, 35))
        self.lb_wks.setMaximumSize(QSize(250, 50))
        self.lb_wks.setFont(font2)
        self.lb_wks.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lb_wks)

        self.le_wks = QLineEdit(self.wg_formular)
        self.le_wks.setObjectName(u"le_wks")
        sizePolicy2.setHeightForWidth(self.le_wks.sizePolicy().hasHeightForWidth())
        self.le_wks.setSizePolicy(sizePolicy2)
        self.le_wks.setMinimumSize(QSize(330, 35))
        self.le_wks.setMaximumSize(QSize(900, 50))
        self.le_wks.setFont(font3)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_wks)

        self.lb_projekt_prefix = QLabel(self.wg_formular)
        self.lb_projekt_prefix.setObjectName(u"lb_projekt_prefix")
        self.lb_projekt_prefix.setMinimumSize(QSize(130, 35))
        self.lb_projekt_prefix.setMaximumSize(QSize(250, 50))
        self.lb_projekt_prefix.setFont(font2)
        self.lb_projekt_prefix.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lb_projekt_prefix)

        self.le_projekt_prefix = QLineEdit(self.wg_formular)
        self.le_projekt_prefix.setObjectName(u"le_projekt_prefix")
        sizePolicy2.setHeightForWidth(self.le_projekt_prefix.sizePolicy().hasHeightForWidth())
        self.le_projekt_prefix.setSizePolicy(sizePolicy2)
        self.le_projekt_prefix.setMinimumSize(QSize(330, 35))
        self.le_projekt_prefix.setMaximumSize(QSize(900, 50))
        self.le_projekt_prefix.setFont(font3)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.le_projekt_prefix)

        self.lb_pfad_backup = QLabel(self.wg_formular)
        self.lb_pfad_backup.setObjectName(u"lb_pfad_backup")
        self.lb_pfad_backup.setMinimumSize(QSize(130, 35))
        self.lb_pfad_backup.setMaximumSize(QSize(250, 50))
        self.lb_pfad_backup.setFont(font2)
        self.lb_pfad_backup.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lb_pfad_backup)

        self.le_pfad_backup = QLineEdit(self.wg_formular)
        self.le_pfad_backup.setObjectName(u"le_pfad_backup")
        sizePolicy2.setHeightForWidth(self.le_pfad_backup.sizePolicy().hasHeightForWidth())
        self.le_pfad_backup.setSizePolicy(sizePolicy2)
        self.le_pfad_backup.setMinimumSize(QSize(330, 35))
        self.le_pfad_backup.setMaximumSize(QSize(900, 50))
        self.le_pfad_backup.setFont(font3)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.le_pfad_backup)

        self.lb_pfad_template = QLabel(self.wg_formular)
        self.lb_pfad_template.setObjectName(u"lb_pfad_template")
        self.lb_pfad_template.setMinimumSize(QSize(130, 35))
        self.lb_pfad_template.setMaximumSize(QSize(250, 50))
        self.lb_pfad_template.setFont(font2)
        self.lb_pfad_template.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lb_pfad_template)

        self.le_pfad_template = QLineEdit(self.wg_formular)
        self.le_pfad_template.setObjectName(u"le_pfad_template")
        sizePolicy2.setHeightForWidth(self.le_pfad_template.sizePolicy().hasHeightForWidth())
        self.le_pfad_template.setSizePolicy(sizePolicy2)
        self.le_pfad_template.setMinimumSize(QSize(330, 35))
        self.le_pfad_template.setMaximumSize(QSize(900, 50))
        self.le_pfad_template.setFont(font3)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.le_pfad_template)

        self.lb_platzhalter_1 = QLabel(self.wg_formular)
        self.lb_platzhalter_1.setObjectName(u"lb_platzhalter_1")
        self.lb_platzhalter_1.setMinimumSize(QSize(120, 35))
        self.lb_platzhalter_1.setMaximumSize(QSize(250, 50))
        self.lb_platzhalter_1.setFont(font2)
        self.lb_platzhalter_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lb_platzhalter_1)

        self.le_platzhalter_1 = QLineEdit(self.wg_formular)
        self.le_platzhalter_1.setObjectName(u"le_platzhalter_1")
        self.le_platzhalter_1.setMinimumSize(QSize(330, 35))
        self.le_platzhalter_1.setMaximumSize(QSize(900, 50))
        self.le_platzhalter_1.setFont(font3)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.le_platzhalter_1)

        self.lb_nutzername = QLabel(self.wg_formular)
        self.lb_nutzername.setObjectName(u"lb_nutzername")
        self.lb_nutzername.setMinimumSize(QSize(130, 35))
        self.lb_nutzername.setMaximumSize(QSize(250, 50))
        self.lb_nutzername.setFont(font2)
        self.lb_nutzername.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_nutzername)

        self.le_nutzername = QLineEdit(self.wg_formular)
        self.le_nutzername.setObjectName(u"le_nutzername")
        sizePolicy2.setHeightForWidth(self.le_nutzername.sizePolicy().hasHeightForWidth())
        self.le_nutzername.setSizePolicy(sizePolicy2)
        self.le_nutzername.setMinimumSize(QSize(330, 35))
        self.le_nutzername.setMaximumSize(QSize(900, 50))
        self.le_nutzername.setFont(font3)
        self.le_nutzername.setStyleSheet(u"background-color: rgb(0, 85, 0)\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_nutzername)


        self.verticalLayout.addWidget(self.wg_formular)

        self.wg_styles = QWidget(frm_settings)
        self.wg_styles.setObjectName(u"wg_styles")
        self.wg_styles.setMinimumSize(QSize(500, 60))
        self.horizontalLayout_3 = QHBoxLayout(self.wg_styles)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_styles = QLabel(self.wg_styles)
        self.lb_styles.setObjectName(u"lb_styles")
        self.lb_styles.setMinimumSize(QSize(120, 35))
        self.lb_styles.setMaximumSize(QSize(250, 50))
        self.lb_styles.setFont(font2)
        self.lb_styles.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lb_styles)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.cb_styles = QComboBox(self.wg_styles)
        self.cb_styles.setObjectName(u"cb_styles")
        self.cb_styles.setMinimumSize(QSize(330, 35))
        self.cb_styles.setFont(font3)

        self.horizontalLayout_3.addWidget(self.cb_styles)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addWidget(self.wg_styles)

        self.lb_ausgabe = QLabel(frm_settings)
        self.lb_ausgabe.setObjectName(u"lb_ausgabe")
        sizePolicy1.setHeightForWidth(self.lb_ausgabe.sizePolicy().hasHeightForWidth())
        self.lb_ausgabe.setSizePolicy(sizePolicy1)
        self.lb_ausgabe.setMinimumSize(QSize(500, 100))
        self.lb_ausgabe.setMaximumSize(QSize(700, 200))
        font4 = QFont()
        font4.setFamilies([u"Comic Sans MS"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.lb_ausgabe.setFont(font4)
        self.lb_ausgabe.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lb_ausgabe)

        self.fr_buttons = QFrame(frm_settings)
        self.fr_buttons.setObjectName(u"fr_buttons")
        self.fr_buttons.setMinimumSize(QSize(500, 70))
        self.fr_buttons.setMaximumSize(QSize(800, 100))
        self.fr_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_buttons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_abbrechen = QPushButton(self.fr_buttons)
        self.pb_abbrechen.setObjectName(u"pb_abbrechen")
        self.pb_abbrechen.setMinimumSize(QSize(120, 50))
        self.pb_abbrechen.setFont(font2)
        self.pb_abbrechen.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.pb_abbrechen)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pb_laden = QPushButton(self.fr_buttons)
        self.pb_laden.setObjectName(u"pb_laden")
        self.pb_laden.setMinimumSize(QSize(120, 50))
        self.pb_laden.setFont(font2)
        self.pb_laden.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.pb_laden)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.pb_speichern = QPushButton(self.fr_buttons)
        self.pb_speichern.setObjectName(u"pb_speichern")
        self.pb_speichern.setMinimumSize(QSize(120, 50))
        self.pb_speichern.setFont(font2)
        self.pb_speichern.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.pb_speichern)


        self.verticalLayout.addWidget(self.fr_buttons)


        self.retranslateUi(frm_settings)
        self.pb_abbrechen.clicked.connect(frm_settings.close)

        QMetaObject.connectSlotsByName(frm_settings)
    # setupUi

    def retranslateUi(self, frm_settings):
        frm_settings.setWindowTitle(QCoreApplication.translate("frm_settings", u"Einstellungen", None))
        self.lb_title_text.setText(QCoreApplication.translate("frm_settings", u"Einstellungen", None))
        self.lb_nc_base_path.setText(QCoreApplication.translate("frm_settings", u"Pfad NC-Files:", None))
        self.le_nc_base_path.setText("")
        self.lb_spannmittel_basis_pfad.setText(QCoreApplication.translate("frm_settings", u"Pfad Spannmittel: ", None))
        self.lb_wks.setText(QCoreApplication.translate("frm_settings", u"WKS:", None))
        self.lb_projekt_prefix.setText(QCoreApplication.translate("frm_settings", u"AT-Nummer:", None))
        self.lb_pfad_backup.setText(QCoreApplication.translate("frm_settings", u"Pfad Backup:", None))
        self.lb_pfad_template.setText(QCoreApplication.translate("frm_settings", u"Pfad KW:", None))
        self.lb_platzhalter_1.setText(QCoreApplication.translate("frm_settings", u"platzhalter_1", None))
        self.le_platzhalter_1.setText(QCoreApplication.translate("frm_settings", u"platzhalter_1", None))
        self.lb_nutzername.setText(QCoreApplication.translate("frm_settings", u"Name:", None))
        self.lb_styles.setText(QCoreApplication.translate("frm_settings", u"Theme:", None))
        self.lb_ausgabe.setText("")
        self.pb_abbrechen.setText(QCoreApplication.translate("frm_settings", u"Beenden", None))
        self.pb_laden.setText(QCoreApplication.translate("frm_settings", u"Laden", None))
        self.pb_speichern.setText(QCoreApplication.translate("frm_settings", u"Speichern", None))
#if QT_CONFIG(shortcut)
        self.pb_speichern.setShortcut(QCoreApplication.translate("frm_settings", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

