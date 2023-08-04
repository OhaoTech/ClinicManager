# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import Qt, QRect
from PySide6 import QtWidgets
from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget

from ui_PatientInfoWindow import Ui_PatientInfoWIndow
from Database import Database
import numpy as np
class PatientInfoWindow(QtWidgets.QMainWindow):
	def __init__(self, parent, database: Database, patient_id: int):
		super().__init__(parent)
		self.ui = Ui_PatientInfoWIndow()
		self.ui.setupUi(self)
		
		self.patient_id = patient_id
  
		self.lineEdit_widgets=[self.ui.name_lineEdit, self.ui.gender_comboBox, self.ui.birthdate_dateEdit,
                         self.ui.tel_lineEdit, self.ui.address_lineEdit, self.ui.remark_lineEdit]

		self.patient_table = database.get_one_patient_by_id(patient_id)
		self.visit_table = database.get_visits_by_patient(patient_id)
		self.tree_widget = self.ui.treeWidget


		self.ui.edit_mode_checkBox.stateChanged.connect(self.toggle_edit_mode)
		self.init_patient_info()

	def toggle_edit_mode(self, state):
		enabled = state == 2
		for widget in self.lineEdit_widgets:
			widget.setEnabled(enabled)
   
	def init_patient_info(self):
		self.ui.name_lineEdit.setText(self.patient_table[1])
		self.ui.gender_comboBox.setCurrentText(self.patient_table[2])
  #todo: set birthdate....
		