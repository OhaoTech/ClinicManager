# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import Qt, QRect, QCoreApplication
from PySide6 import QtWidgets
from PySide6.QtGui import QResizeEvent, QShortcut, QKeySequence, QMouseEvent
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox

from ui_searchWindow import Ui_SearchWindow
from PatientInfoWindow import PatientInfoWindow
from Database import Database
from Exportdatasheet import Exportdatasheet
import numpy as np
class SearchWindow(QtWidgets.QMainWindow):
    def __init__(self, parent, database: Database, exportdatasheet: Exportdatasheet):
        super().__init__(parent)
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)
        self.database = database
        self.exportdatasheet = exportdatasheet
        

        self.table = self.ui.patient_tableWidget

        # set header labels
        labels = [
            QCoreApplication.translate("SearchWindow", "ID"),
            QCoreApplication.translate("SearchWindow", "Full Name"),
            QCoreApplication.translate("SearchWindow", "Gender"),
            QCoreApplication.translate("SearchWindow", "Birthdate"),
            QCoreApplication.translate("SearchWindow", "Telephone"),
            QCoreApplication.translate("SearchWindow", "Home Address"),
            QCoreApplication.translate("SearchWindow", "Remark"),
            QCoreApplication.translate("SearchWindow", "Allergic History"),
            QCoreApplication.translate("SearchWindow", "Past Medical History")
        ]
        # labels = self.database.get_patients_schema()
        self.table.setColumnCount(np.shape(labels)[0])
        for i in range(len(labels)):
            self.table.setHorizontalHeaderItem(i , QTableWidgetItem(labels[i]))
        # Allow manual resizing of the header sections
        horizontal_header = self.table.horizontalHeader()
        horizontal_header.setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        horizontal_header.setSectionsMovable(True)
        horizontal_header.setDragEnabled(True)
        
        vertical_header = self.table.verticalHeader()
        vertical_header.setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        vertical_header.setSectionsMovable(True)
        vertical_header.setDragEnabled(True)
        
        
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setShowGrid(False)
        self.table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        self.table.horizontalHeader().setSortIndicatorShown(True)
        self.table.setColumnHidden(0, True)


        self.ui.search_pushButton.clicked.connect(self.search_patients)
        self.ui.delete_selected_pushButton.clicked.connect(self.delete_selected_patient)
        self.table.itemDoubleClicked.connect(self.on_item_doule_clicked)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.ui.personal_info_label)
        layout.addWidget(self.ui.gender_label)
        layout.addWidget(self.ui.gender_comboBox)
        layout.addWidget(self.ui.tel_label)
        layout.addWidget(self.ui.tel_plainTextEdit)
        layout.addWidget(self.ui.search_pushButton)
        layout.addWidget(self.ui.groupBox)
        layout.addWidget(self.table)
        
        self.setLayout(layout)
    
        shortcut = QShortcut(QKeySequence(Qt.CTRL | Qt.Key_W), self)
        shortcut.activated.connect(self.close)
        
        self.search_patients()

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        #resize the table widget as the cursor dragging the window
        XY = self.table.geometry().topLeft()
        
        
        width = self.geometry().width()
        height = self.geometry().height() 
        self.table.setGeometry(QRect(XY.x(), XY.y(), width, height))
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.ui.groupBox.setGeometry(0, 0, width , height)

    def mousePressEvent(self, event: QMouseEvent):
        self.search_patients()        


    def search_patients(self):
        name = self.ui.name_plainTextEdit.toPlainText()
        tel = self.ui.tel_plainTextEdit.toPlainText()
        gender = self.ui.gender_comboBox.currentText()
        if gender == QCoreApplication.translate("SearchWindow", u"(Select)", None):
            gender = ""
        elif gender == QCoreApplication.translate("SearchWindow", u"Male", None):
            gender = "Male"
        elif gender == QCoreApplication.translate("SearchWindow", u"Female", None):
            gender = "Female"
        patients_list = self.database.get_patient_by_condition(name, tel, gender)
        # Clear the table before populating with new data
        self.table.clearContents()
        self.table.setRowCount(0)

        # Populating the table with the fetched patient data
        for row, data in enumerate(patients_list):
            self.table.insertRow(row)
            for col, value in enumerate(data):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        
    def delete_selected_patient(self):
        if not self.show_confirmation_dialog():
            return
        selected_row = self.table.currentRow()
        patient_id_item = self.table.item(selected_row, 0)
        patient_id = int(patient_id_item.text())
        self.database.delete_patient(patient_id)
        self.search_patients()
        
    def show_confirmation_dialog(self) -> bool:
        confirm_dialog = QMessageBox(self)
        confirm_dialog.setIcon(QMessageBox.Warning)
        confirm_dialog.setWindowTitle(QCoreApplication.translate("SearchWindow", u"Confirmation", None))
        confirm_dialog.setText(QCoreApplication.translate("SearchWindow", u"Are you sure you want to delete this patient?", None))
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        confirm_dialog.setDefaultButton(QMessageBox.Cancel)

        response = confirm_dialog.exec_()
        if response == QMessageBox.Yes:
            return True            
        else:
            return False

    def on_item_doule_clicked(self, item):
        row = item.row()
        patient_id_item = self.table.item(row, 0)
        patient_id = int(patient_id_item.text())
        self.showPatientInfoWindow(patient_id)
        
    def showPatientInfoWindow(self, patient_id):
        patient_info_window = PatientInfoWindow(self, self.database, patient_id, self.exportdatasheet )
        patient_info_window.show()
            
