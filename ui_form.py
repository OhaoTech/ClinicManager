# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLayout, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout, QHBoxLayout, QComboBox,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(629, 903)
        icon = QIcon(QIcon.fromTheme(u"start-here"))
        MainWindow.setWindowIcon(icon)
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)  # 直接在centralwidget上创建布局
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logo_label = QLabel(self.centralwidget)
        self.logo_label.setObjectName(u"logo_label")

        self.verticalLayout_2.addWidget(self.logo_label)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setObjectName(u"searchButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(32)
        self.searchButton.setFont(font)

        self.verticalLayout.addWidget(self.searchButton)

        self.addNewPatientButton = QPushButton(self.centralwidget)
        self.addNewPatientButton.setObjectName(u"addNewPatientButton")
        sizePolicy.setHeightForWidth(self.addNewPatientButton.sizePolicy().hasHeightForWidth())
        self.addNewPatientButton.setSizePolicy(sizePolicy)
        self.addNewPatientButton.setFont(font)

        self.verticalLayout.addWidget(self.addNewPatientButton)

        self.exportAllPatientsButton = QPushButton(self.centralwidget)
        self.exportAllPatientsButton.setObjectName(u"exportAllPatientsButton")
        sizePolicy.setHeightForWidth(self.exportAllPatientsButton.sizePolicy().hasHeightForWidth())
        self.exportAllPatientsButton.setSizePolicy(sizePolicy)
        self.exportAllPatientsButton.setFont(font)

        self.verticalLayout.addWidget(self.exportAllPatientsButton)

        self.languageLayout = QHBoxLayout()
        self.languageLayout.setObjectName(u"languageLayout")
        self.languageLayout.setSpacing(0)
        
        self.cn_radioButton = QRadioButton(self.centralwidget)
        self.cn_radioButton.setObjectName(u"cn_radioButton")
        self.languageLayout.addWidget(self.cn_radioButton)

        self.en_radioButton = QRadioButton(self.centralwidget)
        self.en_radioButton.setObjectName(u"en_radioButton")
        self.languageLayout.addWidget(self.en_radioButton)
        
        # 创建一个新的水平布局用于存放主题标签和组合框
        self.themeLayout = QHBoxLayout()
        self.themeLayout.setObjectName(u"themeLayout")
        
        self.theme_label = QLabel(self.centralwidget)
        self.theme_label.setObjectName(u"theme_label")
        self.themeLayout.addWidget(self.theme_label)
        
        # 创建一个新的水平布局来组合语言和主题布局
        self.bottomLayout = QHBoxLayout()
        self.bottomLayout.setObjectName(u"bottomLayout")
        
        self.bottomLayout.addLayout(self.languageLayout)
        self.bottomLayout.addStretch()  # 添加弹性空间以确保布局分布
        self.bottomLayout.addLayout(self.themeLayout)
        
        # 在主垂直布局中添加这个新的水平布局
        self.verticalLayout.addLayout(self.bottomLayout)

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
        self.cn_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u6587", None))
        self.en_radioButton.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.theme_label.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
    # retranslateUi

