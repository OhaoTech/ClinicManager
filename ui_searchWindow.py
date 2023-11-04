from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import ( QComboBox, QHBoxLayout, 
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QTableWidget, QVBoxLayout, QWidget)

class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        if not SearchWindow.objectName():
            SearchWindow.setObjectName(u"SearchWindow")
        SearchWindow.resize(946, 833)
        icon = QIcon(QIcon.fromTheme(u"phone"))
        SearchWindow.setWindowIcon(icon)

        self.centralwidget = QWidget(SearchWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.personal_info_label = QLabel(self.centralwidget)
        self.personal_info_label.setObjectName(u"personal_info_label")
        self.verticalLayout_2.addWidget(self.personal_info_label)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.name_label_3 = QLabel(self.centralwidget)
        self.name_label_3.setObjectName(u"name_label_3")
        self.horizontalLayout_3.addWidget(self.name_label_3)

        self.name_plainTextEdit_3 = QPlainTextEdit(self.centralwidget)
        self.name_plainTextEdit_3.setObjectName(u"name_plainTextEdit_3")
        self.name_plainTextEdit_3.setStyleSheet(u"")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_plainTextEdit_3.sizePolicy().hasHeightForWidth())
        self.name_plainTextEdit_3.setSizePolicy(sizePolicy)
        self.name_plainTextEdit_3.setMaximumHeight(self.name_label_3.height() + 2)
        self.horizontalLayout_3.addWidget(self.name_plainTextEdit_3)
        
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_plainTextEdit_3.sizePolicy().hasHeightForWidth())
        self.name_plainTextEdit_3.setSizePolicy(sizePolicy)
        self.name_plainTextEdit_3.setMaximumHeight(self.name_label_3.height() + 2)


        self.gender_label_3 = QLabel(self.centralwidget)
        self.gender_label_3.setObjectName(u"gender_label_3")
        self.horizontalLayout_3.addWidget(self.gender_label_3)

        self.gender_comboBox_3 = QComboBox(self.centralwidget)
        self.gender_comboBox_3.addItem("")
        self.gender_comboBox_3.addItem("")
        self.gender_comboBox_3.addItem("")
        self.gender_comboBox_3.setObjectName(u"gender_comboBox_3")
        self.horizontalLayout_3.addWidget(self.gender_comboBox_3)

        self.tel_label_3 = QLabel(self.centralwidget)
        self.tel_label_3.setObjectName(u"tel_label_3")
        self.horizontalLayout_3.addWidget(self.tel_label_3)

        self.tel_plainTextEdit_3 = QPlainTextEdit(self.centralwidget)
        self.tel_plainTextEdit_3.setObjectName(u"tel_plainTextEdit_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tel_plainTextEdit_3.sizePolicy().hasHeightForWidth())
        self.tel_plainTextEdit_3.setSizePolicy(sizePolicy)
        self.tel_plainTextEdit_3.setMaximumHeight(self.tel_label_3.height() + 2)
        self.horizontalLayout_3.addWidget(self.tel_plainTextEdit_3)

        self.search_pushButton_3 = QPushButton(self.centralwidget)
        self.search_pushButton_3.setObjectName(u"search_pushButton_3")
        self.horizontalLayout_3.addWidget(self.search_pushButton_3)

        self.delete_selected_pushButton_3 = QPushButton(self.centralwidget)
        self.delete_selected_pushButton_3.setObjectName(u"delete_selected_pushButton_3")
        self.horizontalLayout_3.addWidget(self.delete_selected_pushButton_3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.patient_tableWidget = QTableWidget(self.centralwidget)
        self.patient_tableWidget.setObjectName(u"patient_tableWidget")
        self.verticalLayout_3.addWidget(self.patient_tableWidget)

        SearchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchWindow)
        QMetaObject.connectSlotsByName(SearchWindow)

    # setupUi

    def retranslateUi(self, SearchWindow):
        SearchWindow.setWindowTitle(QCoreApplication.translate("SearchWindow", u"SearchWindow", None))
        self.personal_info_label.setText(QCoreApplication.translate("SearchWindow", u"Personal Info", None))
        self.personal_info_label.setStyleSheet("font-size: 48pt; font-weight: bold; qproperty-alignment: 'AlignCenter';");
        self.name_label_3.setText(QCoreApplication.translate("SearchWindow", u"Name:", None))
        self.gender_label_3.setText(QCoreApplication.translate("SearchWindow", u"Gender:", None))
        self.gender_comboBox_3.setItemText(0, QCoreApplication.translate("SearchWindow", u"(Select)", None))
        self.gender_comboBox_3.setItemText(1, QCoreApplication.translate("SearchWindow", u"Male", None))
        self.gender_comboBox_3.setItemText(2, QCoreApplication.translate("SearchWindow", u"Female", None))

        self.tel_label_3.setText(QCoreApplication.translate("SearchWindow", u"TEL:", None))
        self.search_pushButton_3.setText(QCoreApplication.translate("SearchWindow", u"Search", None))
        self.delete_selected_pushButton_3.setText(QCoreApplication.translate("SearchWindow", u"Delete Selected", None))
    # retranslateUi

