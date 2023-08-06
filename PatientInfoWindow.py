# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import Qt, QRect, QDate
from PySide6 import QtWidgets
from PySide6.QtGui import QResizeEvent
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget,QTreeWidgetItem, QTreeWidget

from ui_PatientInfoWindow import Ui_PatientInfoWIndow
from Database import Database
import numpy as np
class PatientInfoWindow(QtWidgets.QMainWindow):
	def __init__(self, parent, database: Database, patient_id: int):
		super().__init__(parent)
		self.ui = Ui_PatientInfoWIndow()
		self.ui.setupUi(self)
		
		self.database = database
		self.patient_id = patient_id
  
		self.lineEdit_widgets=[self.ui.name_lineEdit, self.ui.gender_comboBox, self.ui.birthdate_dateEdit,
                         self.ui.tel_lineEdit, self.ui.address_lineEdit, self.ui.remark_lineEdit]
		#patient basic info
		self.patient_table = database.get_one_patient_by_id(patient_id)
		self.visit_table = database.get_visits_by_patient(patient_id)
		self.ui.edit_mode_checkBox.stateChanged.connect(self.toggle_edit_mode)
		self.tree_widget = self.ui.treeWidget
		self.init_patient_info()
		for widget in self.lineEdit_widgets:
			widget.setEnabled(False)
   
		#push buttons
		self.ui.new_pushButton.clicked.connect(self.new_medical_record)
		self.ui.save_pushButton.clicked.connect(self.save_medical_record)
		self.ui.delete_pushButton.clicked.connect(self.delete_medical_record)
		#close window
		shortcut = QShortcut(QKeySequence(Qt.CTRL | Qt.Key_W), self)
		shortcut.activated.connect(self.close)
		self.show_visits()
		#todo: tree widget related operation 

	def toggle_edit_mode(self):
		enabled = self.ui.edit_mode_checkBox.isChecked()
		for widget in self.lineEdit_widgets:
			widget.setEnabled(enabled)

		if not enabled:#update the patient info
			name = self.ui.name_lineEdit.text()
			gender = self.ui.gender_comboBox.currentText()
			birthdate = self.ui.birthdate_dateEdit.date().toString('yyyy-MM-dd')
			tel = self.ui.tel_lineEdit.text()
			address = self.ui.address_lineEdit.text()
			remark = self.ui.remark_lineEdit.text()
			allergic_history = self.ui.allergic_history_textEdit.toPlainText()
			past_medical_history = self.ui.past_medical_history_textEdit.toPlainText()
			self.database.update_patient(self.patient_id, name, gender, birthdate, tel, address,remark, allergic_history, past_medical_history)
      
   
	def init_patient_info(self):
		self.ui.name_lineEdit.setText(self.patient_table[1])
		self.ui.gender_comboBox.setCurrentText(self.patient_table[2])
		self.ui.birthdate_dateEdit.setDate(QDate.fromString(self.patient_table[3], "yyyy-MM-dd"))
		self.ui.tel_lineEdit.setText(self.patient_table[4])
		self.ui.address_lineEdit.setText(self.patient_table[5])
		self.ui.remark_lineEdit.setText(self.patient_table[6])
		self.ui.allergic_history_textEdit.setText(self.patient_table[7])
		self.ui.past_medical_history_textEdit.setText(self.patient_table[8])

	def new_medical_record(self):
		self.ui.chief_complaint_textEdit.clear()
		self.ui.history_of_the_present_illness_textEdit.clear()
		self.ui.examinination_textEdit.clear()
		self.ui.diagnosis_textEdit.clear()
		self.ui.remedy_textEdit.clear()

	def save_medical_record(self):
		pass

	def delete_medical_record(self):
		pass

	def show_visits(self):
		date1 = QDate(2023, 8, 2)
		date2 = QDate(2023, 8, 3)
		item1 = QTreeWidgetItem(["Date 1"])
		item1.setText(0, date1.toString("yyyy-MM-dd"))
		self.ui.treeWidget.addTopLevelItems([item1])