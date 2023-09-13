# This Python file uses the following encoding: utf-8
import sys
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QComboBox
from PySide2.QtGui import  QKeySequence, QShortcutEvent, QKeyEvent
from PySide2.QtCore import Qt, QCoreApplication, QTranslator, Signal
from PyQt5.QtCore import pyqtSignal

from SearchWindow import SearchWindow
from AddNewPatientWindow import AddNewPatientWindow

from Database import Database
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

from Exportdata import Exportdata
import qdarktheme

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
        self.export_data = Exportdata(self.database)
        
        #theme
        self.theme_comboBox = QComboBox(self)
        self.theme_comboBox.addItems([QCoreApplication.translate("MainWindow", u"Auto", None), QCoreApplication.translate("MainWindow", u"Light", None), QCoreApplication.translate("MainWindow", u"Dark", None)])
        self.theme_comboBox.setGeometry(500, 760, 101, 36)
        self.theme_comboBox.currentIndexChanged.connect(self.themeSelect)
        
        # language
        self.translator = QTranslator()
        self.ui.cn_radioButton.click()
        self.ui.cn_radioButton.clicked.connect(self.languageSelect)
        self.ui.en_radioButton.clicked.connect(self.languageSelect)

        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if isinstance(event, QShortcutEvent) and event.key() == QKeySequence(Qt.CTRL | Qt.Key_W):
            self.close()
        super().keyPressEvent(event)

        

    def showSearchWindow(self):
        search_window = SearchWindow(self, self.database, self.export_data)
        search_window.show()
        self.ui.cn_radioButton.clicked.connect(search_window.reTranslate)
        self.ui.en_radioButton.clicked.connect(search_window.reTranslate)

    def showAddNewPatientWindow(self):
        add_new_patient_window = AddNewPatientWindow(self, self.database)
        add_new_patient_window.show()
        self.ui.cn_radioButton.clicked.connect(add_new_patient_window.reTranslate)
        self.ui.en_radioButton.clicked.connect(add_new_patient_window.reTranslate)

    def quitProgram(self):
        QApplication.quit()

    def export_all_patients(self):
        self.export_data.export_datasheet_all_patients_info()
        
    def themeSelect(self):
        if self.theme_comboBox.currentText() == QCoreApplication.translate("MainWindow", u"Auto", None):
            theme = "auto"
        elif self.theme_comboBox.currentText() == QCoreApplication.translate("MainWindow", u"Light", None):
            theme = "light"
        elif self.theme_comboBox.currentText() == QCoreApplication.translate("MainWindow", u"Dark", None):
            theme = "dark"
        qdarktheme.setup_theme(theme)
        
        
    def themeRetranslate(self):
        self.theme_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Auto", None))
        self.theme_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Light", None))
        self.theme_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Dark", None))

    def languageSelect(self):
        if self.ui.cn_radioButton.isChecked():
            self.translator.load("language.qm")
            QCoreApplication.installTranslator(self.translator)
            self.ui.retranslateUi(self)
            self.themeRetranslate()
            self.update()
            
        elif self.ui.en_radioButton.isChecked():
            QCoreApplication.removeTranslator(self.translator)
            self.ui.retranslateUi(self)
            self.themeRetranslate()
            self.update()
            
    def languageRadioButtonConnect(self, target):
        self.ui.cn_radioButton.clicked.connect(target)
        self.ui.en_radioButton.clicked.connect(target)
            
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("auto")
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)  # Enable high-DPI scaling
    font = QApplication.font()  # Get the default font
    font.setPointSizeF(font.pointSizeF() * app.devicePixelRatio())  # Adjust font size based on DPI
    app.setFont(font)  # Set the adjusted font
    widget = MainWindow()
    widget.languageSelect()
    widget.show()
    sys.exit(app.exec_())
