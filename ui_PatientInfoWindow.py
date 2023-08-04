# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PatientInfoWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QSizePolicy, QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_PatientInfoWIndow(object):
    def setupUi(self, PatientInfoWIndow):
        if not PatientInfoWIndow.objectName():
            PatientInfoWIndow.setObjectName(u"PatientInfoWIndow")
        PatientInfoWIndow.resize(860, 825)
        self.treeWidget = QTreeWidget(PatientInfoWIndow)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(0, 120, 151, 701))
        self.groupBox = QGroupBox(PatientInfoWIndow)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 881, 111))
        self.name_label = QLabel(self.groupBox)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(10, 20, 66, 18))
        self.name_lineEdit = QLineEdit(self.groupBox)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setGeometry(QRect(60, 10, 113, 36))
        self.gender_label = QLabel(self.groupBox)
        self.gender_label.setObjectName(u"gender_label")
        self.gender_label.setGeometry(QRect(190, 20, 66, 18))
        self.tel_lineEdit = QLineEdit(self.groupBox)
        self.tel_lineEdit.setObjectName(u"tel_lineEdit")
        self.tel_lineEdit.setGeometry(QRect(420, 10, 151, 36))
        self.gender_comboBox = QComboBox(self.groupBox)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")
        self.gender_comboBox.setGeometry(QRect(250, 10, 125, 36))
        self.tel_label = QLabel(self.groupBox)
        self.tel_label.setObjectName(u"tel_label")
        self.tel_label.setGeometry(QRect(380, 20, 66, 18))
        self.remark_lineEdit = QLineEdit(self.groupBox)
        self.remark_lineEdit.setObjectName(u"remark_lineEdit")
        self.remark_lineEdit.setGeometry(QRect(540, 60, 201, 36))
        self.remark_label = QLabel(self.groupBox)
        self.remark_label.setObjectName(u"remark_label")
        self.remark_label.setGeometry(QRect(480, 70, 66, 18))
        self.address_lineEdit = QLineEdit(self.groupBox)
        self.address_lineEdit.setObjectName(u"address_lineEdit")
        self.address_lineEdit.setGeometry(QRect(120, 60, 351, 36))
        self.address_label = QLabel(self.groupBox)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setGeometry(QRect(10, 70, 111, 18))
        self.edit_mode_checkBox = QCheckBox(self.groupBox)
        self.edit_mode_checkBox.setObjectName(u"edit_mode_checkBox")
        self.edit_mode_checkBox.setGeometry(QRect(750, 70, 97, 24))
        self.birthdate_dateEdit = QDateEdit(self.groupBox)
        self.birthdate_dateEdit.setObjectName(u"birthdate_dateEdit")
        self.birthdate_dateEdit.setGeometry(QRect(650, 10, 201, 42))
        self.tel_label_2 = QLabel(self.groupBox)
        self.tel_label_2.setObjectName(u"tel_label_2")
        self.tel_label_2.setGeometry(QRect(580, 20, 66, 18))

        self.retranslateUi(PatientInfoWIndow)

        QMetaObject.connectSlotsByName(PatientInfoWIndow)
    # setupUi

    def retranslateUi(self, PatientInfoWIndow):
        PatientInfoWIndow.setWindowTitle(QCoreApplication.translate("PatientInfoWIndow", u"PatientInfoWindow", None))
        self.groupBox.setTitle("")
        self.name_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"Name:", None))
        self.gender_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"Gender:", None))
        self.tel_lineEdit.setText("")
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("PatientInfoWIndow", u"Male", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("PatientInfoWIndow", u"Female", None))

        self.tel_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"TEL:", None))
        self.remark_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"Remark:", None))
        self.address_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"Home Address:", None))
        self.edit_mode_checkBox.setText(QCoreApplication.translate("PatientInfoWIndow", u"Edit Mode", None))
        self.birthdate_dateEdit.setDisplayFormat(QCoreApplication.translate("PatientInfoWIndow", u"yyyy/MM/dd", None))
        self.tel_label_2.setText(QCoreApplication.translate("PatientInfoWIndow", u"<html><head/><body><p>Birthdate:</p></body></html>", None))
    # retranslateUi

