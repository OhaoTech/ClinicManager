# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QDateTime, QRect
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt, QTimer, QCoreApplication
from PySide6.QtWidgets import  QLabel, QTextEdit, QMessageBox
from PySide6.QtGui import  QKeySequence, QShortcut


from ui_addNewPatientWindow import Ui_AddNewPatientWindow

import re

from Database import Database
from Exportdata import Exportdata

class AddNewPatientWindow(QtWidgets.QMainWindow):
    def __init__(self, parent, database = Database | None):
        super().__init__(parent)

        self.ui = Ui_AddNewPatientWindow()
        self.ui.setupUi(self)
        self.initStyle()
        
        #push button
        self.ui.cancel_pushButton.clicked.connect(self.closeWindow)
        self.ui.ok_pushButton.clicked.connect(self.saveInfo)
        
        self.database = database
        self.exportdata = Exportdata(database)
        
        #error label
        self.error_label = QLabel(self)
        self.error_label.setStyleSheet("color:red")
        
        #focus out event
        self.ui.name_textEdit_2.focusOutEvent = self.name_txtEdit_focus_out_event
        self.ui.tel_textEdit_2.focusOutEvent = self.tel_txtEdit_focus_out_event
        self.ui.gender_comboBox_2.focusOutEvent = self.gender_comboBox_2_focus_out_event
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)
        
        shortcut = QShortcut(QKeySequence(Qt.CTRL | Qt.Key_W), self)
        shortcut.activated.connect(self.close)
        
        # print to pdf
        self.ui.print_pushButton.clicked.connect(self.print_to_pdf)
        
    def initStyle(self):
        cn_none = QCoreApplication.translate("AddNewPatientWindow", u"None", None)
        self.ui.remark_textEdit_2.setPlaceholderText(cn_none)
        self.ui.allergic_history_textEdit.setPlaceholderText(cn_none)
        self.ui.past_medical_history_textEdit.setPlaceholderText(cn_none)
        self.ui.chief_complaint_textEdit.setPlaceholderText(cn_none)
        self.ui.history_of_the_present_illness_textEdit.setPlaceholderText(cn_none)
        self.ui.examinination_textEdit.setPlaceholderText(cn_none)
        self.ui.diagnosis_textEdit.setPlaceholderText(cn_none)
        self.ui.remedy_textEdit.setPlaceholderText(cn_none)

        
    def closeWindow(self):
        self.close()
        
    def resizeEvent(self, event):
        
        current_width = self.width()
        current_height = self.height()        
        width_ratio = current_width / 1029.0
        height_ratio = current_height / 952.0

        new_width = int(991 * width_ratio)
        new_height = int(921 * height_ratio)
        self.ui.verticalLayoutWidget_2.setGeometry(QRect(10, 10, new_width, new_height))

        super(AddNewPatientWindow, self).resizeEvent(event)
        
    def name_txtEdit_focus_out_event(self, event):
        name = self.ui.name_textEdit_2.toPlainText()
        pattern = r'^[\u4e00-\u9fa5a-zA-Z]+$'
        coord = self.ui.name_textEdit_2.geometry().bottomLeft()
        if not re.match(pattern, name):
            self.error_label.setGeometry(coord.x(), coord.y(), 300, 11)
            self.error_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"Invalid Name", None))           
        else:
            self.error_label.setText("")
            QTextEdit.focusOutEvent(self.ui.tel_textEdit_2, event)
        
    def tel_txtEdit_focus_out_event(self, event):
        tel = self.ui.tel_textEdit_2.toPlainText()
        pattern = r'^\d{1,11}$'
        coord = self.ui.tel_textEdit_2.geometry().bottomLeft()
        if not re.match(pattern, tel):
            self.error_label.setGeometry(coord.x(), coord.y(), 300, 11)
            self.error_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"Invalid TEL number", None))
        else:
            self.error_label.setText("")
            QTextEdit.focusOutEvent(self.ui.name_textEdit_2, event)

    def gender_comboBox_2_focus_out_event(self, event):
        self.error_label.setText("")
        QTextEdit.focusOutEvent(self.ui.name_textEdit_2, event)
        
    def update_date_time(self):
        self.ui.add_dateTimeEdit_2.setDateTime(QDateTime.currentDateTime())
        


    def show_confirmation_dialog(self) -> bool:
        formatted_date_time = self.ui.add_dateTimeEdit_2.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        confirm_dialog = QMessageBox(self)
        confirm_dialog.setIcon(QMessageBox.Warning)
        confirm_dialog.setWindowTitle(QCoreApplication.translate("AddNewPatientWindow", u"Confirmation", None))#'Confirmation'
        confirm_dialog.setText(QCoreApplication.translate("AddNewPatientWindow", u"Proceed with date and time: ", None) + f'{formatted_date_time}?')
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        confirm_dialog.setDefaultButton(QMessageBox.Cancel)

        response = confirm_dialog.exec_()
        if response == QMessageBox.Yes:
            return True            
        else:
            return False


    def saveInfo(self):
        if not self.show_confirmation_dialog():
            return
        #patient table
        name = self.ui.name_textEdit_2.toPlainText()
        gender = self.ui.gender_comboBox_2.currentText()
        birthdate = self.ui.birth_dateEdit_2.date().toString('yyyy-MM-dd')
        tel = self.ui.tel_textEdit_2.toPlainText()
        address = self.ui.address_textEdit_2.toPlainText()
        remark = self.ui.remark_textEdit_2.toPlainText()
        allergic_history = self.ui.allergic_history_textEdit.toPlainText()
        past_medical_history = self.ui.past_medical_history_textEdit.toPlainText()

        if self.error_label.text() != "":
            pass
        elif self.ui.gender_comboBox_2.currentText() == "(Select)":
            coord = self.ui.gender_comboBox_2.geometry().bottomLeft()
            self.error_label.setGeometry(coord.x(), coord.y(), 300, 11)
            self.error_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"Please select number", None))
        elif self.ui.name_textEdit_2.toPlainText() == "":
            coord = self.ui.name_textEdit_2.geometry().bottomLeft()
            self.error_label.setGeometry(coord.x(), coord.y(), 300, 11)
            self.error_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"Invalid Name", None))   
        elif self.ui.tel_textEdit_2.toPlainText() == "":
            coord = self.ui.tel_textEdit_2.geometry().bottomLeft()
            self.error_label.setGeometry(coord.x(), coord.y(), 300, 11)
            self.error_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"Invalid TEL number", None), name)   
        else:
            patient_id = self.database.insert_patient(name, gender, birthdate, tel, address, remark, allergic_history, past_medical_history)
                    
        #visit table
        visit_date = self.ui.add_dateTimeEdit_2.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        cheif_complaint = self.ui.chief_complaint_textEdit.toPlainText()
        present_illness = self.ui.history_of_the_present_illness_textEdit.toPlainText()
        visit_id = self.database.insert_visit(patient_id, visit_date, cheif_complaint, present_illness)
        
        #logs table
        examination = self.ui.examinination_textEdit.toPlainText()
        diagnosis = self.ui.diagnosis_textEdit.toPlainText()
        remedy = self.ui.remedy_textEdit.toPlainText()
        self.database.insert_log(visit_id, examination, diagnosis, remedy)
        
        self.close()
        
    @QtCore.Slot()
    def reTranslate(self):
        self.ui.retranslateUi(self)
        self.initStyle()


        
    @QtCore.Slot()
    def print_to_pdf(self):
        name = self.ui.name_textEdit_2.toPlainText()
        gender = self.ui.gender_comboBox_2.currentText()
        birthdate = self.ui.birth_dateEdit_2.date().toString('yyyy-MM-dd')
        tel = self.ui.tel_textEdit_2.toPlainText()
        address = self.ui.address_textEdit_2.toPlainText()
        remark = self.ui.remark_textEdit_2.toPlainText()
        allergic_history = self.ui.allergic_history_textEdit.toPlainText()
        past_medical_history = self.ui.past_medical_history_textEdit.toPlainText()
        visit_date = self.ui.add_dateTimeEdit_2.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        chief_complaint = self.ui.chief_complaint_textEdit.toPlainText()
        present_illness = self.ui.history_of_the_present_illness_textEdit.toPlainText()
        examination = self.ui.examinination_textEdit.toPlainText()
        diagnosis = self.ui.diagnosis_textEdit.toPlainText()
        remedy = self.ui.remedy_textEdit.toPlainText()
        
        # Create a table with the data
        data = [[QCoreApplication.translate("AddNewPatientWindow", u"Name", None), name],
                [QCoreApplication.translate("AddNewPatientWindow", u"Gender", None), gender],
                [QCoreApplication.translate("AddNewPatientWindow", u"Birthdate", None), birthdate],
                [QCoreApplication.translate("AddNewPatientWindow", u"Telephone", None), tel],
                [QCoreApplication.translate("AddNewPatientWindow", u"Address", None), address],
                [QCoreApplication.translate("AddNewPatientWindow", u"Remark", None), remark],
                [QCoreApplication.translate("AddNewPatientWindow", u"Allergic History", None), allergic_history],
                [QCoreApplication.translate("AddNewPatientWindow", u"Past Medical History", None), past_medical_history],
                [QCoreApplication.translate("AddNewPatientWindow", u"Visit Date", None), visit_date],
                [QCoreApplication.translate("AddNewPatientWindow", u"Chief Complaint", None), chief_complaint],
                [QCoreApplication.translate("AddNewPatientWindow", u"Present Illness", None), present_illness],
                [QCoreApplication.translate("AddNewPatientWindow", u"Examination", None), examination],
                [QCoreApplication.translate("AddNewPatientWindow", u"Diagnosis", None), diagnosis],
                [QCoreApplication.translate("AddNewPatientWindow", u"Remedy", None), remedy]]

        self.exportdata.print_to_pdf(data, filename=name)
        QMessageBox.information(self, QCoreApplication.translate("AddNewPatientWindow", u"Success!", None), name + QCoreApplication.translate("AddNewPatientWindow", u" printed as PDF file", None))
        






