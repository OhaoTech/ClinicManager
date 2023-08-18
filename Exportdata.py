from Database import Database
from PySide2.QtWidgets import QFileDialog, QMessageBox
from PySide2.QtCore import QCoreApplication
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
class Exportdata():
    def __init__(self, database: Database):
        self.database = database
    def choose_file_directory(self,df:pd.DataFrame):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename_without_extension, _ = QFileDialog.getSaveFileName(None, QCoreApplication.translate("Exportdata", u"Save File", None), "","Excel" + QCoreApplication.translate("Exportdata", u"Files", None) + "(*.xlsx)", options=options)
        if filename_without_extension:
            df.to_excel(filename_without_extension+".xlsx", index=False)
            QMessageBox.information(None, QCoreApplication.translate("Exportdata", u"Good!", None), filename_without_extension + ".xlsx"+QCoreApplication.translate("Exportdata", u"exported successful!", None))
    def export_datasheet_all_patients_info(self):
        data = self.database.get_all_patients()
        if len(data) == 0:
            QMessageBox.information(None, QCoreApplication.translate("Exportdata", u"Error!", None), QCoreApplication.translate("Exportdata", u"No data to export!", None))
            return
        labels = [QCoreApplication.translate("Exportdata", u"No.", None),
                  QCoreApplication.translate("Exportdata", u"Name", None),
                  QCoreApplication.translate("Exportdata", u"Gender", None),
                  QCoreApplication.translate("Exportdata", u"Birthdate", None),
                  QCoreApplication.translate("Exportdata", u"TEL", None),
                  QCoreApplication.translate("Exportdata", u"Home Address", None),
                  QCoreApplication.translate("Exportdata", u"Remark", None),
                  QCoreApplication.translate("Exportdata", u"Allergic History", None),
                  QCoreApplication.translate("Exportdata", u"Past Medical History", None)
                ]
        df = pd.DataFrame(data,columns=labels)
        df = df.iloc[1:]
        self.choose_file_directory(df)
        
    def export_datasheet_one_patient_log_visit(self,patient_id:int):
        data = self.database.get_one_patient_visits_and_logs(patient_id)
        labels = [QCoreApplication.translate("Exportdata", u"Visit Date", None),
                  QCoreApplication.translate("Exportdata", u"Chief Complaint", None),
                  QCoreApplication.translate("Exportdata", u"Present Illness", None),
                  QCoreApplication.translate("Exportdata", u"Examination Details", None),
                  QCoreApplication.translate("Exportdata", u"Diagnosis", None),
                  QCoreApplication.translate("Exportdata", u"Remedy", None),
                  ]
        df = pd.DataFrame(data,columns=labels)
        self.choose_file_directory(df)
        
    def print_to_pdf(self,data , filename: str):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        pdf_filename, _= QFileDialog.getSaveFileName(None, QCoreApplication.translate("Exportdata", u"Save File", None), "","PDF" + QCoreApplication.translate("Exportdata", u"Files", None) + "(*.pdf)", options=options)
        if(pdf_filename):
            pdf_filename = pdf_filename + ".pdf"
            doc = SimpleDocTemplate(pdf_filename, pagesize=A4)
            if os.path.isfile("SimSun.ttf"):
                pdfmetrics.registerFont(TTFont("SimSun", "SimSun.ttf"))
            elif os.path.isfile("SimSun.ttc"):
                pdfmetrics.registerFont(TTFont("SimSun", "SimSun.ttc"))

            table = Table(data)
            # Set the font for the table to the font that supports Chinese characters
            table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                      ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                      ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                      ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                      ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                      ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                      ('GRID', (0, 0), (-1, -1), 1, colors.black),
                                      ('FONTNAME', (0, 0), (-1, -1), 'SimSun')
                                      ]))

            # Build the PDF document
            doc.build([table])
            return True
        return False


