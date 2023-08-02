# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

from ui_addNewPatientWindow import Ui_AddNewPatientWindow

class AddNewPatientWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddNewPatientWindow()
        self.ui.setupUi(self)




    def initStyle(self):
        pass



