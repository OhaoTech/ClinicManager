# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QTableView,
    QWidget)

class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        if not SearchWindow.objectName():
            SearchWindow.setObjectName(u"SearchWindow")
        SearchWindow.resize(724, 558)
        icon = QIcon(QIcon.fromTheme(u"phone"))
        SearchWindow.setWindowIcon(icon)
        self.pushButton = QPushButton(SearchWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(430, 60, 91, 51))
        self.plainTextEdit = QPlainTextEdit(SearchWindow)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(90, 60, 131, 41))
        self.label = QLabel(SearchWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 141, 31))
        self.label_2 = QLabel(SearchWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 60, 66, 18))
        self.label_3 = QLabel(SearchWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 60, 66, 18))
        self.comboBox = QComboBox(SearchWindow)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(300, 60, 111, 36))
        self.label_4 = QLabel(SearchWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 110, 66, 18))
        self.plainTextEdit_2 = QPlainTextEdit(SearchWindow)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(90, 110, 251, 41))
        self.tableView = QTableView(SearchWindow)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(40, 160, 651, 391))

        self.retranslateUi(SearchWindow)

        QMetaObject.connectSlotsByName(SearchWindow)
    # setupUi

    def retranslateUi(self, SearchWindow):
        SearchWindow.setWindowTitle(QCoreApplication.translate("SearchWindow", u"SearchWindow", None))
        self.pushButton.setText(QCoreApplication.translate("SearchWindow", u"Search", None))
        self.label.setText(QCoreApplication.translate("SearchWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Personal Info</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("SearchWindow", u"Name:", None))
        self.label_3.setText(QCoreApplication.translate("SearchWindow", u"Gender:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("SearchWindow", u"(Select)", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("SearchWindow", u"Male", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("SearchWindow", u"Female", None))

        self.label_4.setText(QCoreApplication.translate("SearchWindow", u"TEL:", None))
    # retranslateUi

