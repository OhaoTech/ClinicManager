# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHeaderView,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        if not SearchWindow.objectName():
            SearchWindow.setObjectName(u"SearchWindow")
        SearchWindow.resize(1023, 928)
        icon = QIcon()
        iconThemeName = u"phone"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        SearchWindow.setWindowIcon(icon)
        self.groupBox = QGroupBox(SearchWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 971, 161))
        self.search_pushButton = QPushButton(self.groupBox)
        self.search_pushButton.setObjectName(u"search_pushButton")
        self.search_pushButton.setGeometry(QRect(710, 100, 91, 36))
        self.tel_plainTextEdit = QPlainTextEdit(self.groupBox)
        self.tel_plainTextEdit.setObjectName(u"tel_plainTextEdit")
        self.tel_plainTextEdit.setGeometry(QRect(440, 100, 251, 41))
        self.tel_plainTextEdit.setStyleSheet(u"")
        self.personal_info_label = QLabel(self.groupBox)
        self.personal_info_label.setObjectName(u"personal_info_label")
        self.personal_info_label.setGeometry(QRect(300, 10, 431, 71))
        self.name_plainTextEdit = QPlainTextEdit(self.groupBox)
        self.name_plainTextEdit.setObjectName(u"name_plainTextEdit")
        self.name_plainTextEdit.setGeometry(QRect(70, 100, 131, 31))
        self.name_plainTextEdit.setStyleSheet(u"")
        self.name_label = QLabel(self.groupBox)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(20, 100, 66, 18))
        self.tel_label = QLabel(self.groupBox)
        self.tel_label.setObjectName(u"tel_label")
        self.tel_label.setGeometry(QRect(400, 100, 66, 18))
        self.gender_label = QLabel(self.groupBox)
        self.gender_label.setObjectName(u"gender_label")
        self.gender_label.setGeometry(QRect(220, 100, 66, 18))
        self.gender_comboBox = QComboBox(self.groupBox)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")
        self.gender_comboBox.setGeometry(QRect(280, 100, 111, 36))
        self.delete_selected_pushButton = QPushButton(self.groupBox)
        self.delete_selected_pushButton.setObjectName(u"delete_selected_pushButton")
        self.delete_selected_pushButton.setGeometry(QRect(820, 100, 131, 36))
        self.tel_label.raise_()
        self.gender_label.raise_()
        self.name_label.raise_()
        self.search_pushButton.raise_()
        self.tel_plainTextEdit.raise_()
        self.personal_info_label.raise_()
        self.name_plainTextEdit.raise_()
        self.gender_comboBox.raise_()
        self.delete_selected_pushButton.raise_()
        self.patient_tableWidget = QTableWidget(SearchWindow)
        self.patient_tableWidget.setObjectName(u"patient_tableWidget")
        self.patient_tableWidget.setGeometry(QRect(10, 180, 991, 731))

        self.retranslateUi(SearchWindow)

        QMetaObject.connectSlotsByName(SearchWindow)
    # setupUi

    def retranslateUi(self, SearchWindow):
        SearchWindow.setWindowTitle(QCoreApplication.translate("SearchWindow", u"SearchWindow", None))
        self.groupBox.setTitle("")
        self.search_pushButton.setText(QCoreApplication.translate("SearchWindow", u"Search", None))
        self.personal_info_label.setText(QCoreApplication.translate("SearchWindow", u"<html><head/><body><p><span style=\" font-size:48pt; font-weight:700;\">Personal Info</span></p></body></html>", None))
        self.name_label.setText(QCoreApplication.translate("SearchWindow", u"Name:", None))
        self.tel_label.setText(QCoreApplication.translate("SearchWindow", u"TEL:", None))
        self.gender_label.setText(QCoreApplication.translate("SearchWindow", u"Gender:", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("SearchWindow", u"(Select)", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("SearchWindow", u"Male", None))
        self.gender_comboBox.setItemText(2, QCoreApplication.translate("SearchWindow", u"Female", None))

        self.delete_selected_pushButton.setText(QCoreApplication.translate("SearchWindow", u"Delete Selected", None))
    # retranslateUi

