# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt, QDate, QTimer, QDateTime, QCoreApplication, QModelIndex, QRect
from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QTreeWidgetItem, QMessageBox

from ui_PatientInfoWindow import Ui_PatientInfoWindow
from Database import Database
from Exportdata import Exportdata
import numpy as np
class PatientInfoWindow(QtWidgets.QMainWindow):
    
	def __init__(self, parent, database: Database, patient_id: int, export_data: Exportdata):
		super().__init__(parent)
		self.ui = Ui_PatientInfoWindow()
		self.ui.setupUi(self)
		self.parent = parent
		self.database = database
		self.patient_id = patient_id
		self.export_data = export_data

  
		self.info_widgets=[self.ui.name_lineEdit, self.ui.gender_comboBox, self.ui.birthdate_dateEdit,
                         self.ui.tel_lineEdit, self.ui.address_lineEdit, self.ui.remark_lineEdit,
                         self.ui.allergic_history_textEdit, self.ui.past_medical_history_textEdit]
  
		self.records_widgets=[self.ui.chief_complaint_textEdit, self.ui.history_of_the_present_illness_textEdit,
                        self.ui.examinination_textEdit, self.ui.diagnosis_textEdit, self.ui.remedy_textEdit]
		#patient basic info
		self.patient_table = database.get_one_patient_by_id(patient_id)
		self.visit_table = database.get_visits_by_patient(patient_id)
		self.visit_date = ""
  
		self.ui.edit_mode_checkBox.stateChanged.connect(self.toggle_edit_info)
		self.ui.edit_record_checkBox.stateChanged.connect(self.toggle_edit_record)
		self.tree_widget = self.ui.treeWidget
		self.init_patient_info()
		for widget in self.info_widgets:
			widget.setEnabled(False)
		for widget in self.records_widgets:
			widget.setEnabled(False)
   
		#realtime DateTimeEdit timer
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.update_date_time)
		self.timer.start(1000)
		self.ui.realtime_dateTimeEdit.setDisabled(True)
   
		#push buttons
		self.ui.new_pushButton.clicked.connect(self.new_medical_record)
		self.ui.add_record_pushButton.clicked.connect(self.add_medical_record)
		self.ui.delete_record_pushButton.clicked.connect(self.delete_medical_record)
		self.ui.delete_all_records_pushButton.clicked.connect(self.delete_all_medical_record)
		self.ui.export_to_excel_pushButton.clicked.connect(self.export_data.export_datasheet_one_patient_log_visit)
		self.ui.expor_to_pdf_pushButton.clicked.connect(self.print_to_pdf)
		#close window
		shortcut = QShortcut(QKeySequence(Qt.CTRL | Qt.Key_W), self)
		shortcut.activated.connect(self.close)

		#tree widget configurations
		self.tree_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)		
		self.tree_widget.setColumnCount(4)
		self.tree_widget.setColumnHidden(0, True)
		self.tree_widget.setColumnHidden(2, True)
		self.tree_widget.setColumnHidden(3, True)
		self.tree_widget.itemClicked.connect(self.on_item_clicked)
		self.tree_widget.doubleClicked.connect(self.on_item_doule_clicked)
		self.tree_widget.setHeaderLabels(["", QCoreApplication.translate("PatientInfoWindow", u"Visit Date", None), "", ""])
		self.show_visits() 
	
	def resizeEvent(self, event):
		# 获取当前窗口的大小
		current_width = self.width()
		current_height = self.height()

		# 计算宽度和高度的比例
		width_ratio = current_width / 1072.0
		height_ratio = current_height / 1100.0

		# 设置self.verticalLayoutWidget_2的新大小和位置
		new_width = int(1051 * width_ratio)
		new_height = int(1081 * height_ratio)
		self.ui.verticalLayoutWidget_5.setGeometry(QRect(10 * width_ratio, 10 * height_ratio, new_width, new_height))

		super(PatientInfoWindow, self).resizeEvent(event)



	def toggle_edit_info(self):
		enabled = self.ui.edit_mode_checkBox.isChecked()
		for widget in self.info_widgets:
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
			
	
	def toggle_edit_record(self):
		enabled = self.ui.edit_record_checkBox.isChecked()
		for widget in self.records_widgets:
			widget.setEnabled(enabled)
   
		if not enabled:
			chief_complaint = self.ui.chief_complaint_textEdit.toPlainText()
			present_illness = self.ui.history_of_the_present_illness_textEdit.toPlainText()
			examination = self.ui.examinination_textEdit.toPlainText()
			diagnosis = self.ui.diagnosis_textEdit.toPlainText()
			remedy = self.ui.remedy_textEdit.toPlainText()
			self.database.update_visits_by_visit_id(self.visit_id, chief_complaint, present_illness)
			self.database.update_log_by_visit(self.visit_id, examination, diagnosis, remedy)
			self.show_visits()
   
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
		confirm_dialog.setWindowTitle(QCoreApplication.translate("PatientInfoWindow", u"Confirmation", None))
		confirm_dialog.setText(QCoreApplication.translate("PatientInfoWindow", f"Proceed with date and time: {formatted_date_time}?", None))
		confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
		confirm_dialog.setDefaultButton(QMessageBox.Cancel)

		response = confirm_dialog.exec_()
		if response == QMessageBox.Yes:
			return True            
		else:
			return False

	def delete_medical_record(self):
		if not self.show_confirmation_dialog():
			return
		self.database.delete_log_by_visit_id(self.visit_id)
		self.database.delete_visit_by_visit_id(self.visit_id)
		self.show_visits()
  
	def delete_all_medical_record(self):
		if not self.show_confirmation_dialog():
			return
		self.database.delete_visit_by_patient(self.patient_id)
		self.show_visits()


	def on_item_doule_clicked(self, index: QModelIndex):
		item = self.tree_widget.itemFromIndex(index)
		self.visit_id = item.text(0)
		self.visit_date = item.text(1)
		chief_complaint = item.text(2)
		present_illness = item.text(3)
  
		self.ui.chief_complaint_textEdit.setText(chief_complaint)
		self.ui.history_of_the_present_illness_textEdit.setText(present_illness)
  
		log_data = self.database.get_logs_by_visit(self.visit_id)
	
		self.ui.examinination_textEdit.setText(log_data[0][2])
		self.ui.diagnosis_textEdit.setText(log_data[0][3])
		self.ui.remedy_textEdit.setText(log_data[0][4])
  
	def on_item_clicked(self, item: QTreeWidgetItem, column: int):
		self.visit_id = item.text(0)
		self.visit_date = item.text(1)
		chief_complaint = item.text(2)
		present_illness = item.text(3)
  
		self.ui.chief_complaint_textEdit.setText(chief_complaint)
		self.ui.history_of_the_present_illness_textEdit.setText(present_illness)
  
		log_data = self.database.get_logs_by_visit(self.visit_id)
	
		self.ui.examinination_textEdit.setText(log_data[0][2])
		self.ui.diagnosis_textEdit.setText(log_data[0][3])
		self.ui.remedy_textEdit.setText(log_data[0][4])	

	def show_visits(self):
		self.tree_widget.clear()
		visits_data = self.database.get_visits_by_patient(self.patient_id)
		date_items = []
		for data in visits_data:
			item = QTreeWidgetItem()
			item.setText(0, str(data[0]))# visit_id
			item.setText(1, data[2])# visit date
			item.setText(2, data[3])# chief complaint
			item.setText(3, data[4])# past medical history

			date_items.append(item)
		self.tree_widget.addTopLevelItems(date_items)

	@QtCore.Slot()
	def reTranslate(self):
		self.ui.retranslateUi(self)
		self.tree_widget.setHeaderLabels(["", QCoreApplication.translate("PatientInfoWindow", u"Visit Date", None), "", ""])
		self.update()
     
	@QtCore.Slot()
	def print_to_pdf(self):
		if self.visit_date.strip() == "":
			QMessageBox.information(self, QCoreApplication.translate("PatientInfoWindow", u"Error!", None), QCoreApplication.translate("PatientInfoWindow", u"Please select a visit record", None))
			return
		name = self.ui.name_lineEdit.text()
		gender = self.ui.gender_comboBox.currentText()
		birthdate = self.ui.birthdate_dateEdit.date().toString('yyyy-MM-dd')
		tel = self.ui.tel_lineEdit.text()
		address = self.ui.address_lineEdit.text()
		remark = self.ui.remark_lineEdit.text()
		allergic_history = self.ui.allergic_history_textEdit.toPlainText()
		past_medical_history = self.ui.past_medical_history_textEdit.toPlainText()
		visit_date = self.visit_date
		chief_complaint = self.ui.chief_complaint_textEdit.toPlainText()
		present_illness = self.ui.history_of_the_present_illness_textEdit.toPlainText()
		examination = self.ui.examinination_textEdit.toPlainText()
		diagnosis = self.ui.diagnosis_textEdit.toPlainText()
		remedy = self.ui.remedy_textEdit.toPlainText()
		
		data = [[QCoreApplication.translate("PatientInfoWindow", u"Name", None), name],
				[QCoreApplication.translate("PatientInfoWindow", u"Gender", None), gender],
				[QCoreApplication.translate("PatientInfoWindow", u"Birthdate", None), birthdate],
				[QCoreApplication.translate("PatientInfoWindow", u"TEL", None), tel],
				[QCoreApplication.translate("PatientInfoWindow", u"Address", None), address],
				[QCoreApplication.translate("PatientInfoWindow", u"Remark", None), remark],	
				[QCoreApplication.translate("PatientInfoWindow", u"Allergic History", None), allergic_history],
				[QCoreApplication.translate("PatientInfoWindow", u"Past Medical History", None), past_medical_history],
				[QCoreApplication.translate("PatientInfoWindow", u"Visit Date", None), visit_date],
				[QCoreApplication.translate("PatientInfoWindow", u"Chief Complaint", None), chief_complaint],
				[QCoreApplication.translate("PatientInfoWindow", u"History of the Present Illness", None), present_illness],
				[QCoreApplication.translate("PatientInfoWindow", u"Examination", None), examination],
				[QCoreApplication.translate("PatientInfoWindow", u"Diagnosis", None), diagnosis],
				[QCoreApplication.translate("PatientInfoWindow", u"Remedy", None), remedy]]
		if	self.export_data.print_to_pdf(data, filename=name):
			QMessageBox.information(self, QCoreApplication.translate("PatientInfoWindow", u"Success!", None), name + QCoreApplication.translate("PatientInfoWindow", u" printed as PDF file", None))
  