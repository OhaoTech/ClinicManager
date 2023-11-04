from PySide6 import QtCore
from PySide6.QtCore import Qt, QRect, QCoreApplication
from PySide6 import QtWidgets
from PySide6.QtGui import QResizeEvent, QShortcut, QKeySequence, QMouseEvent
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox

from ui_searchWindow import Ui_SearchWindow
from PatientInfoWindow import PatientInfoWindow
from Database import Database
from Exportdata import Exportdata
import numpy as np
class SearchWindow(QtWidgets.QMainWindow):
    def __init__(self, parent, database: Database, export_data: Exportdata):
        super().__init__(parent)
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)
        self.database = database
        self.parent = parent
        self.export_data = export_data
        

        self.table = self.ui.patient_tableWidget


        self.reTranslate_headers()
        # Allow manual resizing of the header sections
        horizontal_header = self.table.horizontalHeader()
        horizontal_header.setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        horizontal_header.setSectionResizeMode(self.table.columnCount()-1, QtWidgets.QHeaderView.Stretch)

        
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



        self.ui.search_pushButton_3.clicked.connect(self.search_patients)
        self.ui.delete_selected_pushButton_3.clicked.connect(self.delete_selected_patient)
        self.table.itemDoubleClicked.connect(self.on_item_doule_clicked)


    
        shortcut = QShortcut(QKeySequence(Qt.CTRL | Qt.Key_W), self)
        shortcut.activated.connect(self.close)
        
        self.search_patients()
        
    def reTranslate_headers(self):
        # set header labels
        self.labels = [
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
        self.table.setColumnCount(np.shape(self.labels)[0])
        for i in range(np.shape(self.labels)[0]):
            self.table.setHorizontalHeaderItem(i, QTableWidgetItem(self.labels[i]))
            

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        #resize the table widget as the cursor dragging the window
        XY = self.table.geometry().topLeft()
        
        
        width = self.geometry().width()
        height = self.geometry().height() 
        self.table.setGeometry(QRect(XY.x(), XY.y(), width, height))
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def mousePressEvent(self, event: QMouseEvent):
        self.search_patients()        


    def search_patients(self):
        
        name = self.ui.name_plainTextEdit_3.toPlainText() 
        tel = self.ui.tel_plainTextEdit_3.toPlainText()  
        gender = self.ui.gender_comboBox_3.currentText() 
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
        
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        self.table.horizontalHeader().setSectionResizeMode(self.table.columnCount()-1, QtWidgets.QHeaderView.Stretch)
        
        
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
        patient_info_window = PatientInfoWindow(self, self.database, patient_id, self.export_data )
        patient_info_window.show()
        self.parent.languageRadioButtonConnect(patient_info_window.reTranslate)
        
    @QtCore.Slot()
    def reTranslate(self):
        self.reTranslate_headers()
        self.ui.retranslateUi(self)
        self.update()
            
