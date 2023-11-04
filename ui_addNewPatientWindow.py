
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QRect,QTime, Qt)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QAbstractSpinBox, QComboBox, QDateEdit,
    QDateTimeEdit, QFormLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_AddNewPatientWindow(object):
    def setupUi(self, AddNewPatientWindow):
        if not AddNewPatientWindow.objectName():
            AddNewPatientWindow.setObjectName(u"AddNewPatientWindow")
        AddNewPatientWindow.resize(1029, 952)
        icon = QIcon(QIcon.fromTheme(u"camera-web"))
        AddNewPatientWindow.setWindowIcon(icon)
        self.verticalLayoutWidget_2 = QWidget(AddNewPatientWindow)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 991, 921))
        self.mainVerticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.mainVerticalLayout.setObjectName(u"mainVerticalLayout")
        self.mainVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.name_label_2 = QLabel(self.verticalLayoutWidget_2)
        self.name_label_2.setObjectName(u"name_label_2")
        label_height = self.name_label_2.sizeHint().height()

        self.horizontalLayout_4.addWidget(self.name_label_2)

        self.name_textEdit_2 = QTextEdit(self.verticalLayoutWidget_2)
        self.name_textEdit_2.setObjectName(u"name_textEdit_2")
        self.name_textEdit_2.setStyleSheet(u"")
        self.name_textEdit_2.setFixedHeight(label_height + 20)
        
        self.horizontalLayout_4.addWidget(self.name_textEdit_2)

        self.gender_label_2 = QLabel(self.verticalLayoutWidget_2)
        self.gender_label_2.setObjectName(u"gender_label_2")

        self.horizontalLayout_4.addWidget(self.gender_label_2)

        self.gender_comboBox_2 = QComboBox(self.verticalLayoutWidget_2)
        self.gender_comboBox_2.addItem("")
        self.gender_comboBox_2.addItem("")
        self.gender_comboBox_2.addItem("")
        self.gender_comboBox_2.setObjectName(u"gender_comboBox_2")
        self.gender_comboBox_2.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.gender_comboBox_2)

        self.birthdata_label_2 = QLabel(self.verticalLayoutWidget_2)
        self.birthdata_label_2.setObjectName(u"birthdata_label_2")

        self.horizontalLayout_4.addWidget(self.birthdata_label_2)

        self.birth_dateEdit_2 = QDateEdit(self.verticalLayoutWidget_2)
        self.birth_dateEdit_2.setObjectName(u"birth_dateEdit_2")
        self.birth_dateEdit_2.setStyleSheet(u"")
        self.birth_dateEdit_2.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.birth_dateEdit_2.setCalendarPopup(True)
        self.birth_dateEdit_2.setCurrentSectionIndex(0)
        self.birth_dateEdit_2.setTimeSpec(Qt.LocalTime)
        self.birth_dateEdit_2.setDate(QDate(1999, 1, 1))

        self.horizontalLayout_4.addWidget(self.birth_dateEdit_2)

        self.remark_label_2 = QLabel(self.verticalLayoutWidget_2)
        self.remark_label_2.setObjectName(u"remark_label_2")

        self.horizontalLayout_4.addWidget(self.remark_label_2)

        self.remark_textEdit_2 = QTextEdit(self.verticalLayoutWidget_2)
        self.remark_textEdit_2.setObjectName(u"remark_textEdit_2")
        self.remark_textEdit_2.setStyleSheet(u"")
        self.remark_textEdit_2.setFixedHeight(label_height + 20)

        self.horizontalLayout_4.addWidget(self.remark_textEdit_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.address_label_2 = QLabel(self.verticalLayoutWidget_2)
        self.address_label_2.setObjectName(u"address_label_2")

        self.horizontalLayout_5.addWidget(self.address_label_2)

        self.address_textEdit_2 = QTextEdit(self.verticalLayoutWidget_2)
        self.address_textEdit_2.setObjectName(u"address_textEdit_2")
        self.address_textEdit_2.setStyleSheet(u"")
        self.address_textEdit_2.setFixedHeight(label_height + 20)

        self.horizontalLayout_5.addWidget(self.address_textEdit_2)

        self.tel_label_2 = QLabel(self.verticalLayoutWidget_2)
        self.tel_label_2.setObjectName(u"tel_label_2")

        self.horizontalLayout_5.addWidget(self.tel_label_2)

        self.tel_textEdit_2 = QTextEdit(self.verticalLayoutWidget_2)
        self.tel_textEdit_2.setObjectName(u"tel_textEdit_2")
        self.tel_textEdit_2.setStyleSheet(u"")
        self.tel_textEdit_2.setFixedHeight(label_height + 20)

        self.horizontalLayout_5.addWidget(self.tel_textEdit_2)

        self.add_time_label_2 = QLabel(self.verticalLayoutWidget_2)
        self.add_time_label_2.setObjectName(u"add_time_label_2")

        self.horizontalLayout_5.addWidget(self.add_time_label_2)

        self.add_dateTimeEdit_2 = QDateTimeEdit(self.verticalLayoutWidget_2)
        self.add_dateTimeEdit_2.setObjectName(u"add_dateTimeEdit_2")
        self.add_dateTimeEdit_2.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.add_dateTimeEdit_2.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.add_dateTimeEdit_2.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(8, 0, 0)))
        self.add_dateTimeEdit_2.setCalendarPopup(False)
        self.add_dateTimeEdit_2.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout_5.addWidget(self.add_dateTimeEdit_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.mainVerticalLayout.addLayout(self.verticalLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.medical_history_label = QLabel(self.verticalLayoutWidget_2)
        self.medical_history_label.setObjectName(u"medical_history_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.medical_history_label)

        self.allergic_history_label = QLabel(self.verticalLayoutWidget_2)
        self.allergic_history_label.setObjectName(u"allergic_history_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.allergic_history_label)

        self.allergic_history_textEdit = QTextEdit(self.verticalLayoutWidget_2)
        self.allergic_history_textEdit.setObjectName(u"allergic_history_textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allergic_history_textEdit.sizePolicy().hasHeightForWidth())
        self.allergic_history_textEdit.setSizePolicy(sizePolicy)
        self.allergic_history_textEdit.setStyleSheet(u"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.allergic_history_textEdit)

        self.past_medical_history_label = QLabel(self.verticalLayoutWidget_2)
        self.past_medical_history_label.setObjectName(u"past_medical_history_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.past_medical_history_label)

        self.past_medical_history_textEdit = QTextEdit(self.verticalLayoutWidget_2)
        self.past_medical_history_textEdit.setObjectName(u"past_medical_history_textEdit")
        sizePolicy.setHeightForWidth(self.past_medical_history_textEdit.sizePolicy().hasHeightForWidth())
        self.past_medical_history_textEdit.setSizePolicy(sizePolicy)
        self.past_medical_history_textEdit.setStyleSheet(u"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.past_medical_history_textEdit)

        self.outpatient_records_label = QLabel(self.verticalLayoutWidget_2)
        self.outpatient_records_label.setObjectName(u"outpatient_records_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.outpatient_records_label)

        self.chief_complaint_label = QLabel(self.verticalLayoutWidget_2)
        self.chief_complaint_label.setObjectName(u"chief_complaint_label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.chief_complaint_label)

        self.chief_complaint_textEdit = QTextEdit(self.verticalLayoutWidget_2)
        self.chief_complaint_textEdit.setObjectName(u"chief_complaint_textEdit")
        sizePolicy.setHeightForWidth(self.chief_complaint_textEdit.sizePolicy().hasHeightForWidth())
        self.chief_complaint_textEdit.setSizePolicy(sizePolicy)
        self.chief_complaint_textEdit.setStyleSheet(u"")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.chief_complaint_textEdit)

        self.history_of_the_present_illness_label = QLabel(self.verticalLayoutWidget_2)
        self.history_of_the_present_illness_label.setObjectName(u"history_of_the_present_illness_label")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.history_of_the_present_illness_label)

        self.history_of_the_present_illness_textEdit = QTextEdit(self.verticalLayoutWidget_2)
        self.history_of_the_present_illness_textEdit.setObjectName(u"history_of_the_present_illness_textEdit")
        sizePolicy.setHeightForWidth(self.history_of_the_present_illness_textEdit.sizePolicy().hasHeightForWidth())
        self.history_of_the_present_illness_textEdit.setSizePolicy(sizePolicy)
        self.history_of_the_present_illness_textEdit.setStyleSheet(u"")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.history_of_the_present_illness_textEdit)

        self.examinination_label = QLabel(self.verticalLayoutWidget_2)
        self.examinination_label.setObjectName(u"examinination_label")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.examinination_label)

        self.examinination_textEdit = QTextEdit(self.verticalLayoutWidget_2)
        self.examinination_textEdit.setObjectName(u"examinination_textEdit")
        sizePolicy.setHeightForWidth(self.examinination_textEdit.sizePolicy().hasHeightForWidth())
        self.examinination_textEdit.setSizePolicy(sizePolicy)
        self.examinination_textEdit.setStyleSheet(u"")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.examinination_textEdit)

        self.diagnosis_label = QLabel(self.verticalLayoutWidget_2)
        self.diagnosis_label.setObjectName(u"diagnosis_label")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.diagnosis_label)

        self.diagnosis_textEdit = QTextEdit(self.verticalLayoutWidget_2)
        self.diagnosis_textEdit.setObjectName(u"diagnosis_textEdit")
        sizePolicy.setHeightForWidth(self.diagnosis_textEdit.sizePolicy().hasHeightForWidth())
        self.diagnosis_textEdit.setSizePolicy(sizePolicy)
        self.diagnosis_textEdit.setStyleSheet(u"")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.diagnosis_textEdit)

        self.remedy_label = QLabel(self.verticalLayoutWidget_2)
        self.remedy_label.setObjectName(u"remedy_label")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.remedy_label)

        self.remedy_textEdit = QTextEdit(self.verticalLayoutWidget_2)
        self.remedy_textEdit.setObjectName(u"remedy_textEdit")
        sizePolicy.setHeightForWidth(self.remedy_textEdit.sizePolicy().hasHeightForWidth())
        self.remedy_textEdit.setSizePolicy(sizePolicy)
        self.remedy_textEdit.setStyleSheet(u"")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.remedy_textEdit)


        self.mainVerticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.print_pushButton = QPushButton(self.verticalLayoutWidget_2)
        self.print_pushButton.setObjectName(u"print_pushButton")

        self.horizontalLayout_3.addWidget(self.print_pushButton)

        self.cancel_pushButton = QPushButton(self.verticalLayoutWidget_2)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")

        self.horizontalLayout_3.addWidget(self.cancel_pushButton)

        self.ok_pushButton = QPushButton(self.verticalLayoutWidget_2)
        self.ok_pushButton.setObjectName(u"ok_pushButton")

        self.horizontalLayout_3.addWidget(self.ok_pushButton)


        self.mainVerticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(AddNewPatientWindow)

        QMetaObject.connectSlotsByName(AddNewPatientWindow)
    # setupUi

    def retranslateUi(self, AddNewPatientWindow):
        AddNewPatientWindow.setWindowTitle(QCoreApplication.translate("AddNewPatientWindow", u"AddNewPatientWindow", None))
        self.label_2.setText(QCoreApplication.translate("AddNewPatientWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Patient Info</span></p></body></html>", None))
        self.name_label_2.setText(QCoreApplication.translate("AddNewPatientWindow", u"Name:", None))
        self.gender_label_2.setText(QCoreApplication.translate("AddNewPatientWindow", u"Gender:", None))
        self.gender_comboBox_2.setItemText(0, QCoreApplication.translate("AddNewPatientWindow", u"(Select)", None))
        self.gender_comboBox_2.setItemText(1, QCoreApplication.translate("AddNewPatientWindow", u"Male", None))
        self.gender_comboBox_2.setItemText(2, QCoreApplication.translate("AddNewPatientWindow", u"Female", None))

        self.birthdata_label_2.setText(QCoreApplication.translate("AddNewPatientWindow", u"Birth Date:", None))
        self.birth_dateEdit_2.setDisplayFormat(QCoreApplication.translate("AddNewPatientWindow", u"yyyy/MM/dd", None))
        self.remark_label_2.setText(QCoreApplication.translate("AddNewPatientWindow", u"Remark:", None))
        self.address_label_2.setText(QCoreApplication.translate("AddNewPatientWindow", u"Home Address:", None))
        self.tel_label_2.setText(QCoreApplication.translate("AddNewPatientWindow", u"TEL:", None))
        self.tel_textEdit_2.setHtml(QCoreApplication.translate("AddNewPatientWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Cantarell'; font-size:11pt;\"><br /></p></body></html>", None))
        self.add_time_label_2.setText(QCoreApplication.translate("AddNewPatientWindow", u"Add time:", None))
        self.add_dateTimeEdit_2.setDisplayFormat(QCoreApplication.translate("AddNewPatientWindow", u"yyyy/MM/dd HH:mm:ss\u202f", None))
        self.medical_history_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Medical History</span></p></body></html>", None))
        self.allergic_history_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"Allergic History: ", None))
        self.past_medical_history_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"<html><head/><body><p align=\"center\">Past Medical </p><p align=\"center\">History:</p></body></html>", None))
        self.outpatient_records_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Outpatient Records</span></p></body></html>", None))
        self.chief_complaint_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"Chief Complaint:", None))
        self.history_of_the_present_illness_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"<html><head/><body><p align=\"center\">History of the</p><p align=\"center\"> Present </p><p align=\"center\">Illness:</p></body></html>", None))
        self.examinination_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"<html><head/><body><p align=\"center\">Examination:</p></body></html>", None))
        self.diagnosis_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"<html><head/><body><p align=\"center\">Diagnosis:</p></body></html>", None))
        self.remedy_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"<html><head/><body><p align=\"center\">Remedy</p></body></html>", None))
        self.print_pushButton.setText(QCoreApplication.translate("AddNewPatientWindow", u"Print", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("AddNewPatientWindow", u"Cancel", None))
        self.ok_pushButton.setText(QCoreApplication.translate("AddNewPatientWindow", u"OK", None))
    # retranslateUi

