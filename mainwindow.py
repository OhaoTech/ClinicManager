# This Python file uses the following encoding: utf-8
import sys

from PyQt5 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtCore import Qt 

from SearchWindow import SearchWindow
from AddNewPatientWindow import AddNewPatientWindow

from Database import Database
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ui_searchWindow import Ui_SearchWindow
from ui_addNewPatientWindow import Ui_AddNewPatientWindow

from Exportdatasheet import Exportdatasheet

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Button
        self.ui.searchButton.clicked.connect(self.showSearchWindow)
        self.ui.addNewPatientButton.clicked.connect(self.showAddNewPatientWindow)
        self.ui.exportAllPatientsButton.clicked.connect(self.export_all_patients)

        # Database
        self.database = Database("clinic.db")
        self.exportdatasheet = Exportdatasheet(self.database)
        shortcut = QShortcut(QKeySequence(Qt.CTRL | Qt.Key_W), self)
        shortcut.activated.connect(self.quitProgram)

    def showSearchWindow(self):
        search_window = SearchWindow(self, self.database)
        search_window.show()

    def showAddNewPatientWindow(self):
        add_new_patient_window = AddNewPatientWindow(self, self.database)
        add_new_patient_window.show()

    def quitProgram(self):
        QApplication.quit()

    def export_all_patients(self):
        self.exportdatasheet.export_all_patients_info()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
