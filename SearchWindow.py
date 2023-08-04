# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import Qt, QRect
from PySide6 import QtWidgets
from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget

from ui_searchWindow import Ui_SearchWindow
from Database import Database
import numpy as np
class SearchWindow(QtWidgets.QMainWindow):
    def __init__(self, parent, database: Database):
        super().__init__(parent)
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)
        self.database = database

        self.ui.search_pushButton.clicked.connect(self.search_patients)
        self.table = self.ui.patient_tableWidget

        # set header labels
        labels = self.database.get_patients_schema()
        self.table.setColumnCount(np.shape(labels)[0])
        for i in range(len(labels)):
            self.table.setHorizontalHeaderItem(i, QTableWidgetItem(labels[i][1]))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.ui.personal_info_label)
        layout.addWidget(self.ui.gender_label)
        layout.addWidget(self.ui.gender_comboBox)
        layout.addWidget(self.ui.tel_label)
        layout.addWidget(self.ui.tel_plainTextEdit)
        layout.addWidget(self.ui.search_pushButton)
        layout.addWidget(self.table)
        
        self.setLayout(layout)
        

        

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        #resize the table widget as the cursor dragging the window
        XY = self.table.geometry().topLeft()
        
        width = self.geometry().width() - 30
        height = self.geometry().height() - 80
        self.table.setGeometry(QRect(XY.x(), XY.y(), width, height))
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        
        

    def search_patients(self):
        name = self.ui.name_plainTextEdit.toPlainText()
        tel = self.ui.tel_plainTextEdit.toPlainText()
        gender = self.ui.gender_comboBox.currentText()
        if gender == "(Select)":
            gender = ""
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
        

        
     
            
            
