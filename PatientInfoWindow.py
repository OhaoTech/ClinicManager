# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import Qt, QRect, QDate, QTimer, QDateTime
from PySide6 import QtWidgets
from PySide6.QtGui import QResizeEvent
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QTreeWidgetItem, QTreeWidget, QMessageBox 

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
                         self.ui.tel_lineEdit, self.ui.address_lineEdit, self.ui.remark_lineEdit,
                         self.ui.allergic_history_textEdit, self.ui.past_medical_history_textEdit]
		#patient basic info
		self.patient_table = database.get_one_patient_by_id(patient_id)
		self.visit_table = database.get_visits_by_patient(patient_id)
  
		self.ui.edit_mode_checkBox.stateChanged.connect(self.toggle_edit_mode)
		self.tree_widget = self.ui.treeWidget
		self.init_patient_info()
		for widget in self.lineEdit_widgets:
			widget.setEnabled(False)
   
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.update_date_time)
		self.timer.start(1000)
   
		#push buttons
		self.ui.new_pushButton.clicked.connect(self.new_medical_record)
		self.ui.add_record_pushButton.clicked.connect(self.add_medical_record)
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
	
	def update_date_time(self):
		self.ui.realtime_dateTimeEdit.setDateTime(QDateTime.currentDateTime())
      
   
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

	def add_medical_record(self):
		if not self.show_confirmation_dialog():
			return

		chief_complaint = self.ui.chief_complaint_textEdit.toPlainText()
		present_illness = self.ui.history_of_the_present_illness_textEdit.toPlainText()

		examination = self.ui.examinination_textEdit.toPlainText()
		diagnosis = self.ui.diagnosis_textEdit.toPlainText()
		remedy = self.ui.remedy_textEdit.toPlainText()
  
		current_real_time = self.ui.realtime_dateTimeEdit.dateTime().toString('yyyy-MM-dd HH:mm:ss')

		visit_id = self.database.insert_visit(self.patient_id, current_real_time, chief_complaint, present_illness)
  
		self.database.insert_log(visit_id, examination, diagnosis, remedy)
		self.show_visits() 
  




	def show_confirmation_dialog(self) -> bool:
		formatted_date_time = self.ui.realtime_dateTimeEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
		confirm_dialog = QMessageBox(self)
		confirm_dialog.setIcon(QMessageBox.Warning)
		confirm_dialog.setWindowTitle('Confirmation')
		confirm_dialog.setText(f'Proceed with date and time: {formatted_date_time}?')
		confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
		confirm_dialog.setDefaultButton(QMessageBox.Cancel)

		response = confirm_dialog.exec_()
		if response == QMessageBox.Yes:
			return True            
		else:
			return False

	def delete_medical_record(self):
		pass

	def show_visits(self):
		visits_data = self.database.get_visits_by_patient(self.patient_id)
		date_items = []
		for data in visits_data:
			item = QTreeWidgetItem()
			item.setText(0, data[2])
			date_items.append(item)
		self.tree_widget.addTopLevelItems(date_items)