from Database import Database
from tkinter import Tk, filedialog
import pandas as pd
class Exportdatasheet():
    def __init__(self, database: Database):
        self.database = database
    def choose_file_directory(self,df:pd.DataFrame):
        Tk().withdraw()
        output_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        df.to_excel(output_path, index=False)
    def export_all_patients_info(self):
        data = self.database.get_all_patients()
        columns = [col[0] for col in self.database.cursor.description]
        df = pd.DataFrame(data,columns=columns)
        self.choose_file_directory(df)
