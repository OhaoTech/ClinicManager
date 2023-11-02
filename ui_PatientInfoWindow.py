# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PatientInfoWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QDateTimeEdit, QFormLayout, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextBrowser, QTextEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_PatientInfoWindow(object):
    def setupUi(self, PatientInfoWindow):
        if not PatientInfoWindow.objectName():
            PatientInfoWindow.setObjectName(u"PatientInfoWindow")
        PatientInfoWindow.resize(1072, 1100)
        self.verticalLayoutWidget_5 = QWidget(PatientInfoWindow)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 10, 1051, 1081))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name_label = QLabel(self.verticalLayoutWidget_5)
        self.name_label.setObjectName(u"name_label")

        self.horizontalLayout.addWidget(self.name_label)

        self.name_lineEdit = QLineEdit(self.verticalLayoutWidget_5)
        self.name_lineEdit.setObjectName(u"name_lineEdit")

        self.horizontalLayout.addWidget(self.name_lineEdit)

        self.birthdate_label = QLabel(self.verticalLayoutWidget_5)
        self.birthdate_label.setObjectName(u"birthdate_label")

        self.horizontalLayout.addWidget(self.birthdate_label)

        self.birthdate_dateEdit = QDateEdit(self.verticalLayoutWidget_5)
        self.birthdate_dateEdit.setObjectName(u"birthdate_dateEdit")

        self.horizontalLayout.addWidget(self.birthdate_dateEdit)

        self.gender_label = QLabel(self.verticalLayoutWidget_5)
        self.gender_label.setObjectName(u"gender_label")

        self.horizontalLayout.addWidget(self.gender_label)

        self.gender_comboBox = QComboBox(self.verticalLayoutWidget_5)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")

        self.horizontalLayout.addWidget(self.gender_comboBox)

        self.tel_label = QLabel(self.verticalLayoutWidget_5)
        self.tel_label.setObjectName(u"tel_label")

        self.horizontalLayout.addWidget(self.tel_label)

        self.tel_lineEdit = QLineEdit(self.verticalLayoutWidget_5)
        self.tel_lineEdit.setObjectName(u"tel_lineEdit")

        self.horizontalLayout.addWidget(self.tel_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.address_label = QLabel(self.verticalLayoutWidget_5)
        self.address_label.setObjectName(u"address_label")

        self.horizontalLayout_2.addWidget(self.address_label)

        self.address_lineEdit = QLineEdit(self.verticalLayoutWidget_5)
        self.address_lineEdit.setObjectName(u"address_lineEdit")

        self.horizontalLayout_2.addWidget(self.address_lineEdit)

        self.remark_label = QLabel(self.verticalLayoutWidget_5)
        self.remark_label.setObjectName(u"remark_label")

        self.horizontalLayout_2.addWidget(self.remark_label)

        self.remark_lineEdit = QLineEdit(self.verticalLayoutWidget_5)
        self.remark_lineEdit.setObjectName(u"remark_lineEdit")

        self.horizontalLayout_2.addWidget(self.remark_lineEdit)

        self.edit_mode_checkBox = QCheckBox(self.verticalLayoutWidget_5)
        self.edit_mode_checkBox.setObjectName(u"edit_mode_checkBox")

        self.horizontalLayout_2.addWidget(self.edit_mode_checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.treeWidget = QTreeWidget(self.verticalLayoutWidget_5)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Visit Date Time");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_2.addWidget(self.treeWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.delete_all_records_pushButton = QPushButton(self.verticalLayoutWidget_5)
        self.delete_all_records_pushButton.setObjectName(u"delete_all_records_pushButton")

        self.horizontalLayout_3.addWidget(self.delete_all_records_pushButton)

        self.export_to_excel_pushButton = QPushButton(self.verticalLayoutWidget_5)
        self.export_to_excel_pushButton.setObjectName(u"export_to_excel_pushButton")

        self.horizontalLayout_3.addWidget(self.export_to_excel_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.allergic_history_label = QLabel(self.verticalLayoutWidget_5)
        self.allergic_history_label.setObjectName(u"allergic_history_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.allergic_history_label)

        self.allergic_history_textEdit = QTextEdit(self.verticalLayoutWidget_5)
        self.allergic_history_textEdit.setObjectName(u"allergic_history_textEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.allergic_history_textEdit)

        self.past_medical_history_label = QLabel(self.verticalLayoutWidget_5)
        self.past_medical_history_label.setObjectName(u"past_medical_history_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.past_medical_history_label)

        self.past_medical_history_textEdit = QTextEdit(self.verticalLayoutWidget_5)
        self.past_medical_history_textEdit.setObjectName(u"past_medical_history_textEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.past_medical_history_textEdit)

        self.line = QFrame(self.verticalLayoutWidget_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.line)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.textBrowser = QTextBrowser(self.verticalLayoutWidget_5)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"font: 700 11pt \"Liberation Serif\";")

        self.horizontalLayout_6.addWidget(self.textBrowser)

        self.realtime_label = QLabel(self.verticalLayoutWidget_5)
        self.realtime_label.setObjectName(u"realtime_label")

        self.horizontalLayout_6.addWidget(self.realtime_label)

        self.realtime_dateTimeEdit = QDateTimeEdit(self.verticalLayoutWidget_5)
        self.realtime_dateTimeEdit.setObjectName(u"realtime_dateTimeEdit")
        self.realtime_dateTimeEdit.setLocale(QLocale(QLocale.Chinese, QLocale.China))

        self.horizontalLayout_6.addWidget(self.realtime_dateTimeEdit)

        self.edit_record_checkBox = QCheckBox(self.verticalLayoutWidget_5)
        self.edit_record_checkBox.setObjectName(u"edit_record_checkBox")

        self.horizontalLayout_6.addWidget(self.edit_record_checkBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.chief_complaint_label = QLabel(self.verticalLayoutWidget_5)
        self.chief_complaint_label.setObjectName(u"chief_complaint_label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.chief_complaint_label)

        self.chief_complaint_textEdit = QTextEdit(self.verticalLayoutWidget_5)
        self.chief_complaint_textEdit.setObjectName(u"chief_complaint_textEdit")
        self.chief_complaint_textEdit.setStyleSheet(u"")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.chief_complaint_textEdit)

        self.history_of_the_present_illness_label = QLabel(self.verticalLayoutWidget_5)
        self.history_of_the_present_illness_label.setObjectName(u"history_of_the_present_illness_label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.history_of_the_present_illness_label)

        self.history_of_the_present_illness_textEdit = QTextEdit(self.verticalLayoutWidget_5)
        self.history_of_the_present_illness_textEdit.setObjectName(u"history_of_the_present_illness_textEdit")
        self.history_of_the_present_illness_textEdit.setStyleSheet(u"")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.history_of_the_present_illness_textEdit)

        self.examinination_label = QLabel(self.verticalLayoutWidget_5)
        self.examinination_label.setObjectName(u"examinination_label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.examinination_label)

        self.examinination_textEdit = QTextEdit(self.verticalLayoutWidget_5)
        self.examinination_textEdit.setObjectName(u"examinination_textEdit")
        self.examinination_textEdit.setStyleSheet(u"")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.examinination_textEdit)

        self.diagnosis_label = QLabel(self.verticalLayoutWidget_5)
        self.diagnosis_label.setObjectName(u"diagnosis_label")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.diagnosis_label)

        self.remedy_label = QLabel(self.verticalLayoutWidget_5)
        self.remedy_label.setObjectName(u"remedy_label")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.remedy_label)

        self.remedy_textEdit = QTextEdit(self.verticalLayoutWidget_5)
        self.remedy_textEdit.setObjectName(u"remedy_textEdit")
        self.remedy_textEdit.setStyleSheet(u"")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.remedy_textEdit)

        self.diagnosis_textEdit = QTextEdit(self.verticalLayoutWidget_5)
        self.diagnosis_textEdit.setObjectName(u"diagnosis_textEdit")
        self.diagnosis_textEdit.setStyleSheet(u"")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.diagnosis_textEdit)


        self.verticalLayout_3.addLayout(self.formLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.delete_record_pushButton = QPushButton(self.verticalLayoutWidget_5)
        self.delete_record_pushButton.setObjectName(u"delete_record_pushButton")

        self.horizontalLayout_5.addWidget(self.delete_record_pushButton)

        self.expor_to_pdf_pushButton = QPushButton(self.verticalLayoutWidget_5)
        self.expor_to_pdf_pushButton.setObjectName(u"expor_to_pdf_pushButton")

        self.horizontalLayout_5.addWidget(self.expor_to_pdf_pushButton)

        self.new_pushButton = QPushButton(self.verticalLayoutWidget_5)
        self.new_pushButton.setObjectName(u"new_pushButton")

        self.horizontalLayout_5.addWidget(self.new_pushButton)

        self.add_record_pushButton = QPushButton(self.verticalLayoutWidget_5)
        self.add_record_pushButton.setObjectName(u"add_record_pushButton")

        self.horizontalLayout_5.addWidget(self.add_record_pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)

        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)


        self.retranslateUi(PatientInfoWindow)

        QMetaObject.connectSlotsByName(PatientInfoWindow)
    # setupUi

    def retranslateUi(self, PatientInfoWindow):
        PatientInfoWindow.setWindowTitle(QCoreApplication.translate("PatientInfoWindow", u"PatientInfoWindow", None))
        self.name_label.setText(QCoreApplication.translate("PatientInfoWindow", u"Name:", None))
        self.birthdate_label.setText(QCoreApplication.translate("PatientInfoWindow", u"<html><head/><body><p>Birthdate:</p></body></html>", None))
        self.birthdate_dateEdit.setDisplayFormat(QCoreApplication.translate("PatientInfoWindow", u"yyyy/MM/dd", None))
        self.gender_label.setText(QCoreApplication.translate("PatientInfoWindow", u"Gender:", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("PatientInfoWindow", u"Male", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("PatientInfoWindow", u"Female", None))

        self.tel_label.setText(QCoreApplication.translate("PatientInfoWindow", u"TEL:", None))
        self.tel_lineEdit.setText("")
        self.address_label.setText(QCoreApplication.translate("PatientInfoWindow", u"Home Address:", None))
        self.remark_label.setText(QCoreApplication.translate("PatientInfoWindow", u"Remark:", None))
        self.edit_mode_checkBox.setText(QCoreApplication.translate("PatientInfoWindow", u"Edit/Save Info", None))
        self.delete_all_records_pushButton.setText(QCoreApplication.translate("PatientInfoWindow", u"Delete All Records", None))
        self.export_to_excel_pushButton.setText(QCoreApplication.translate("PatientInfoWindow", u"Export to Excel", None))
        self.allergic_history_label.setText(QCoreApplication.translate("PatientInfoWindow", u"Allergic History:", None))
        self.past_medical_history_label.setText(QCoreApplication.translate("PatientInfoWindow", u"<html><head/><body><p>Past Medical </p><p>History:</p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("PatientInfoWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Liberation Serif'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Cantarell'; font-size:22pt;\">Medical Records</span></p></body></html>", None))
        self.realtime_label.setText(QCoreApplication.translate("PatientInfoWindow", u"Realtime:", None))
        self.realtime_dateTimeEdit.setDisplayFormat(QCoreApplication.translate("PatientInfoWindow", u"yyyy-MM-dd HH:mm:ss", None))
        self.edit_record_checkBox.setText(QCoreApplication.translate("PatientInfoWindow", u"Edit/Save Record", None))
        self.chief_complaint_label.setText(QCoreApplication.translate("PatientInfoWindow", u"<html><head/><body><p align=\"center\">Chief Complaint:</p></body></html>", None))
        self.history_of_the_present_illness_label.setText(QCoreApplication.translate("PatientInfoWindow", u"<html><head/><body><p>Present Illness History: </p></body></html>", None))
        self.examinination_label.setText(QCoreApplication.translate("PatientInfoWindow", u"<html><head/><body><p align=\"center\">Examination:</p></body></html>", None))
        self.diagnosis_label.setText(QCoreApplication.translate("PatientInfoWindow", u"<html><head/><body><p align=\"center\">Diagnosis:</p></body></html>", None))
        self.remedy_label.setText(QCoreApplication.translate("PatientInfoWindow", u"<html><head/><body><p align=\"center\">Remedy:</p></body></html>", None))
        self.delete_record_pushButton.setText(QCoreApplication.translate("PatientInfoWindow", u"Delete Record", None))
        self.expor_to_pdf_pushButton.setText(QCoreApplication.translate("PatientInfoWindow", u"Export to PDF", None))
        self.new_pushButton.setText(QCoreApplication.translate("PatientInfoWindow", u"Clear ", None))
        self.add_record_pushButton.setText(QCoreApplication.translate("PatientInfoWindow", u"Add Record", None))
    # retranslateUi

