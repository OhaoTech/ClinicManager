# This Python file uses the following encoding: utf-8
import sys
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox,  QSizePolicy, QSlider, QLabel, QWidget
from PySide6.QtGui import QShortcut, QKeySequence, QFontDatabase, QFont
from PySide6.QtCore import Qt, QCoreApplication, QTranslator

from SearchWindow import SearchWindow
from AddNewPatientWindow import AddNewPatientWindow

from Database import Database

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
        shortcut = QShortcut(QKeySequence(Qt.CTRL | Qt.Key_W), self)
        shortcut.activated.connect(self.quitProgram)
        
        # theme
        self.theme_comboBox = QComboBox(self)
        self.theme_comboBox.addItems([QCoreApplication.translate("MainWindow", u"Auto", None), 
                                      QCoreApplication.translate("MainWindow", u"Light", None), 
                                      QCoreApplication.translate("MainWindow", u"Dark", None)])
        self.theme_comboBox.currentIndexChanged.connect(self.themeSelect)
        self.ui.themeLayout.addWidget(self.theme_comboBox)  # 将组合框添加到主题布局中
        
        # language
        self.translator = QTranslator()
        self.ui.cn_radioButton.click()
        self.ui.cn_radioButton.clicked.connect(self.languageSelect)
        self.ui.en_radioButton.clicked.connect(self.languageSelect)
        
        
        self.fontSizeLabel = QLabel(QCoreApplication.translate("MainWindow", u"Aa", None), self)
        self.fontSizeSlider = QSlider(Qt.Horizontal, self)
        self.fontSizeSlider.setMinimum(12)  # Minimum font size
        self.fontSizeSlider.setMaximum(36)  # Maximum font size
        self.fontSizeSlider.setValue(16)  # Default font size
        self.fontSizeSlider.valueChanged.connect(self.adjustFontSize)
        self.ui.themeLayout.addWidget(self.fontSizeLabel)
        self.ui.themeLayout.addWidget(self.fontSizeSlider)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.fontSizeSlider.setSizePolicy(sizePolicy)
        self.fontSizeSlider.setFixedWidth(200)

        

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
        
    def updateWidgetFonts(self, widget, font):
        """Recursively update the font of the widget and its children."""
        if isinstance(widget, QWidget):  # Check if it's a widget
            widget.setFont(font)
        for child in widget.children():
            self.updateWidgetFonts(child, font)


    def adjustFontSize(self):
        """Slot to adjust the font size based on the slider value."""
        value = self.fontSizeSlider.value()
        font = QApplication.font()
        button_font = QApplication.font()
        font.setPointSize(value)
        button_font_size = value + 16
        button_font.setPointSize(button_font_size)
        self.ui.searchButton.setFont(button_font)
        self.ui.addNewPatientButton.setFont(button_font)
        self.ui.exportAllPatientsButton.setFont(button_font)
        
        QApplication.setFont(font)
        self.ui.themeLayout.update()
        self.updateWidgetFonts(self, font)          

    def updateWidgetFonts(self, parent, font):
        for child in parent.children():
            if isinstance(child, QWidget) and child not in [self.ui.searchButton, self.ui.addNewPatientButton, self.ui.exportAllPatientsButton, self.ui.logo_label]:
                child.setFont(font)
                self.updateWidgetFonts(child, font)  
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("auto")

    fontId = QFontDatabase.addApplicationFont("Simsun-Bold.ttf")
    if fontId != -1:  # 确认字体已经被加载
        fontFamilies = QFontDatabase.applicationFontFamilies(fontId)
        if fontFamilies:  # 设置字体给整个应用程序
            simsunFont = QFont(fontFamilies[0])
            app.setFont(simsunFont)

    widget = MainWindow()
    widget.languageSelect()
    widget.show()
    sys.exit(app.exec())
