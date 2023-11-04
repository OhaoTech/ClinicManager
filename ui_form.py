from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtGui import (QAction, QFont, QIcon)
from PySide6.QtWidgets import (QLabel, QLayout, QPushButton, QRadioButton, QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget)

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
        self.verticalLayout = QVBoxLayout(self.centralwidget)  
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
        
        self.themeLayout = QHBoxLayout()
        self.themeLayout.setObjectName(u"themeLayout")
        
        self.theme_label = QLabel(self.centralwidget)
        self.theme_label.setObjectName(u"theme_label")
        self.themeLayout.addWidget(self.theme_label)
        
        self.bottomLayout = QHBoxLayout()
        self.bottomLayout.setObjectName(u"bottomLayout")
        
        self.bottomLayout.addLayout(self.languageLayout)
        self.bottomLayout.addStretch() 
        self.bottomLayout.addLayout(self.themeLayout)
        
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

