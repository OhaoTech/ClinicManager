# This Python file uses the following encoding: utf-8
import sys

from PyQt5 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

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

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Button
        self.ui.searchButton.clicked.connect(self.showSearchWindow)
        self.ui.addNewPatientButton.clicked.connect(self.showAddNewPatientWindow)

        # Menubar Actions
        self.ui.actionExit.triggered.connect(self.quitProgram)

        # Database
        database = Database("clinic.db")

    def showSearchWindow(self):
        search_window = SearchWindow(self)
        search_window.show()

    def showAddNewPatientWindow(self):
        add_new_patient_window = AddNewPatientWindow(self)
        add_new_patient_window.show()

    def quitProgram(self):
        QApplication.quit()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
