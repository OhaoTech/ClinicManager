import math
from Database import Database
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtCore import QCoreApplication
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

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
        
    def print_to_pdf(self, data: list[list[str]], filename: str):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        pdf_filename, _ = QFileDialog.getSaveFileName(None, QCoreApplication.translate("Exportdata", u"Save File", None), "", "PDF" + QCoreApplication.translate("Exportdata", u"Files", None) + "(*.pdf)", options=options)
        if pdf_filename:
            # Register font
            if os.path.isfile("SimSun.ttf"):
                pdfmetrics.registerFont(TTFont("SimSun", "SimSun.ttf"))
            if os.path.isfile("SimSun-Bold.ttf"):
                pdfmetrics.registerFont(TTFont("SimSun-Bold", "SimSun-Bold.ttf"))
            if os.path.isfile("KAITI.ttf"):
                pdfmetrics.registerFont(TTFont("KAITI", "KAITI.ttf"))

            # Define the style for the title of the document
            title_style = ParagraphStyle(
                'TitleStyle',
                parent=getSampleStyleSheet()['Title'],
                fontName='KAITI',   
                fontSize=24,
                leading=30,
                alignment=1,  # Center align
                spaceAfter=30,  # Space after the title
                fontWeight=1,  # Bold
            )
            
            
            # Create the document
            title = Paragraph(data[0][1] + QCoreApplication.translate("Exportdata", u" Report")  , title_style)
            if not pdf_filename.endswith('.pdf'):
                pdf_filename = pdf_filename + ".pdf"
            doc = SimpleDocTemplate(pdf_filename, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)


            # Set colWidths
            left_col_width = doc.width * 0.25
            right_col_width = doc.width - left_col_width
            col_widths = [left_col_width if index == 0 else right_col_width for index in range(len(data[0]))]

            # Wrap the text in cells
            for rowIndex, row in enumerate(data):
                for colIndex, cell_text in enumerate(row):
                    wrapped_text = self.wrap_text_to_fit_width(cell_text, 'SimSun', 12, col_widths[colIndex])
                    data[rowIndex][colIndex] = wrapped_text

            table = Table(data, colWidths=col_widths, splitByRow=True)
            # Set the font for the table to the font that supports Chinese characters
            table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'SimSun-Bold'),  
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12), 
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # 其他单元格使用白色背景
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTNAME', (0, 1), (0, -1), 'SimSun-Bold'),  # 左列使用加粗字体
                ('FONTNAME', (1, 1), (-1, -1), 'SimSun'),  # 其他列使用普通字体
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('LEFTPADDING', (0, 0), (-1, -1), 6),
                ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                ('TOPPADDING', (0, 0), (-1, -1), 6),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                ('WORDWRAP', (0, 0), (-1, -1), True),
                ('FONTNAME', (0, 0), (0, -1), 'SimSun-Bold'),  # 左列标题也使用加粗字体
            ]))
            for rowIndex, row in enumerate(data):
                maxHeight = 20  # Set a minimum row height
                for item in row:
                    # 计算文本行数
                    lines_count = len(item.split('\n'))
                    # 每行的高度可以假设为12（字体大小） + 2（行间距，可根据需要调整）
                    text_height = lines_count * (12 + 2)
                    maxHeight = max(maxHeight, text_height)
                table._argH[rowIndex] = maxHeight

            
            # Build the PDF document
            doc.build([title, table])
            return True
        return False

    def wrap_text_to_fit_width(self, text, font_name, font_size, max_width):
        chars = list(text)
        lines = []
        line = ""
        
        while chars:
            char = chars.pop(0)
            test_line = line + char
            width = pdfmetrics.stringWidth(test_line, font_name, font_size)

            if width <= max_width:
                line = test_line
            else:
                lines.append(line)
                line = char

            # 当chars为空时，确保最后的line也被添加到lines中
            if not chars:
                lines.append(line)

        return "\n".join(lines)
