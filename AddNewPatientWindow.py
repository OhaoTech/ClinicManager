# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QLabel, QTextEdit
from PySide6.QtGui import QPalette, QColor

from ui_addNewPatientWindow import Ui_AddNewPatientWindow

import re


class AddNewPatientWindow(QtWidgets.QMainWindow):
    def __init__(self, parent, database):
        super().__init__(parent)

        self.ui = Ui_AddNewPatientWindow()
        self.ui.setupUi(self)
        self.initStyle()
        
        self.ui.cancel_pushButton.clicked.connect(self.closeWindow)
        self.ui.ok_pushButton.clicked.connect(self.saveInfo)
        self.database = database
        
        self.error_label = QLabel(self)
        self.error_label.setStyleSheet("color:red")
        self.error_label.setGeometry(-100, -100,0,0)
        self.error_label.setText("NULL")
        
        self.ui.name_textEdit.focusOutEvent = self.name_txtEdit_focus_out_event
        self.ui.tel_textEdit.focusOutEvent = self.tel_txtEdit_focus_out_event
        
    def initStyle(self):
        self.ui.allergic_history_textEdit.setPlaceholderText("None")
        self.ui.past_medical_history_textEdit.setPlaceholderText("None")
        self.ui.chief_complaint_textEdit.setPlaceholderText("None")
        self.ui.history_of_the_present_illness_textEdit.setPlaceholderText("None")
        self.ui.examinination_textEdit.setPlaceholderText("None")
        self.ui.diagnosis_textEdit.setPlaceholderText("None")
        self.ui.remedy_textEdit.setPlaceholderText("None")

        
    def closeWindow(self):
        self.close()
        
    def name_txtEdit_focus_out_event(self, event):
        name = self.ui.name_textEdit.toPlainText()
        pattern = r'^[\u4e00-\u9fa5a-zA-Z]+$'
        coord = self.ui.name_textEdit.geometry().bottomLeft()
        if not re.match(pattern, name):
            self.error_label.setGeometry(coord.x(), coord.y(), 300, 11)
            self.error_label.setText("Invalid Name")           
        else:
            self.error_label.setText("")
            QTextEdit.focusOutEvent(self.ui.tel_textEdit, event)
        
    def tel_txtEdit_focus_out_event(self, event):
        tel = self.ui.tel_textEdit.toPlainText()
        pattern = r'^\d{1,11}$'
        coord = self.ui.tel_textEdit.geometry().bottomLeft()
        if not re.match(pattern, tel):
            self.error_label.setGeometry(coord.x(), coord.y(), 300, 11)
            self.error_label.setText("Invalid TEL number")
        else:
            self.error_label.setText("")
            QTextEdit.focusOutEvent(self.ui.name_textEdit, event)
            

    def saveInfo(self):
        name = self.ui.name_textEdit.toPlainText()
        gender = self.ui.gender_comboBox.currentText()
        birthdate = self.ui.birth_dateEdit.date().toString()
        tel = self.ui.tel_textEdit.toPlainText()
        address = self.ui.address_textEdit.toPlainText()
        remark = self.ui.remark_textEdit.toPlainText()
        allergic_history = self.ui.allergic_history_textEdit.toPlainText()
        past_medical_history = self.ui.past_medical_history_textEdit.toPlainText()

        if self.error_label.text() != "":
            pass
        else:
            self.database.insert_patient(name, gender, birthdate, tel, address, remark, allergic_history, past_medical_history)
            self.close()
        
        


        
        
        
    
        








