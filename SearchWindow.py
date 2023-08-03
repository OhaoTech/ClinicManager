# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

from ui_searchWindow import Ui_SearchWindow

class SearchWindow(QtWidgets.QMainWindow):
    def __init__(self, parent, database):
        super().__init__(parent)
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)
        self.database = database

