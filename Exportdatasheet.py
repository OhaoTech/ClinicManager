from Database import Database
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtCore import QCoreApplication
import pandas as pd
class Exportdatasheet():
    def __init__(self, database: Database):
        self.database = database
    def choose_file_directory(self,df:pd.DataFrame):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename_without_extension, _ = QFileDialog.getSaveFileName(None, QCoreApplication.translate("Exportdatasheet", u"Save File", None), "","Excel" + QCoreApplication.translate("Exportdatasheet", u"Files", None) + "(*.xlsx)", options=options)
        if filename_without_extension:
            df.to_excel(filename_without_extension+".xlsx", index=False)
            QMessageBox.information(None, QCoreApplication.translate("Exportdatasheet", u"Good!", None), filename_without_extension + ".xlsx"+QCoreApplication.translate("Exportdatasheet", u"exported successful!", None))
    def export_all_patients_info(self):
        data = self.database.get_all_patients()
        columns = [col[0] for col in self.database.cursor.description]
        df = pd.DataFrame(data,columns=columns)
        self.choose_file_directory(df)
    def export_one_patient_log_visit(self,patient_id:int):
        data = self.database.get_one_patient_visits_and_logs(patient_id)
        columns = [col[0] for col in self.database.cursor.description]
        df = pd.DataFrame(data,columns=columns)
        self.choose_file_directory(df)
