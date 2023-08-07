# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(614, 903)
        icon = QIcon()
        iconThemeName = u"start-here"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        MainWindow.setWindowIcon(icon)
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo_label = QLabel(self.centralwidget)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setGeometry(QRect(170, 30, 261, 71))
        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(60, 110, 471, 201))
        font = QFont()
        font.setPointSize(32)
        self.searchButton.setFont(font)
        self.addNewPatientButton = QPushButton(self.centralwidget)
        self.addNewPatientButton.setObjectName(u"addNewPatientButton")
        self.addNewPatientButton.setGeometry(QRect(60, 320, 471, 201))
        self.addNewPatientButton.setFont(font)
        self.exportAllPatientsButton = QPushButton(self.centralwidget)
        self.exportAllPatientsButton.setObjectName(u"exportAllPatientsButton")
        self.exportAllPatientsButton.setGeometry(QRect(60, 530, 471, 201))
        self.exportAllPatientsButton.setFont(font)
        self.theme_label = QLabel(self.centralwidget)
        self.theme_label.setObjectName(u"theme_label")
        self.theme_label.setGeometry(QRect(450, 870, 66, 18))
        self.en_radioButton = QRadioButton(self.centralwidget)
        self.en_radioButton.setObjectName(u"en_radioButton")
        self.en_radioButton.setGeometry(QRect(10, 870, 114, 24))
        self.cn_radioButton = QRadioButton(self.centralwidget)
        self.cn_radioButton.setObjectName(u"cn_radioButton")
        self.cn_radioButton.setGeometry(QRect(10, 840, 114, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Clinic Manager", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import...", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export...", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.logo_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Clinic Manager</span></p></body></html>", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.addNewPatientButton.setText(QCoreApplication.translate("MainWindow", u"Add New Patient", None))
        self.exportAllPatientsButton.setText(QCoreApplication.translate("MainWindow", u"Export All Patients", None))
        self.theme_label.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.en_radioButton.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.cn_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u6587", None))
    # retranslateUi

