import sqlite3

class Database:
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()
        self.create_table()
        self.conn.commit()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                            id INTEGER PRIMARY KEY,
                            full_name TEXT NOT NULL,
                            gender TEXT NOT NULL,
                            birthdate TEXT NOT NULL,
                            telephone TEXT NOT NULL CHECK(telephone GLOB '[0-9]*'),
                            home_address TEXT,
                            remark TEXT,
                            allergic_history TEXT,
                            past_medical_history TEXT)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS visits (
                        id INTEGER PRIMARY KEY,
                        patient_id INTEGER NOT NULL,
                        visit_date TEXT NOT NULL,
                        chief_complaint TEXT,
                        present_illness TEXT,
                        FOREIGN KEY (patient_id) REFERENCES patients(id))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS logs (
                        id INTEGER PRIMARY KEY ,
                        visit_id INTEGER NOT NULL,
                        examination_details TEXT,
                        diagnosis TEXT,
                        remedy TEXT,
                        FOREIGN KEY (visit_id) REFERENCES visits(id))''')


    # Create patient record
    def insert_patient(self, full_name, gender, birthdate, telephone, home_address, remark, allergic_history, past_medical_history):
        self.cursor.execute("INSERT INTO patients (full_name, gender, birthdate, telephone, home_address, remark, allergic_history, past_medical_history) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (full_name, gender, birthdate, telephone, home_address, remark, allergic_history, past_medical_history))
        self.conn.commit()
        return self.cursor.lastrowid #patient id

    def get_patients_schema(self):
        self.cursor.execute("PRAGMA table_info(patients)")
        return self.cursor.fetchall()
    
    def get_one_patient_by_id(self, patient_id):
        self.cursor.execute("SELECT * FROM patients WHERE id=?", (patient_id,))
        return self.cursor.fetchone()    

    # Read patient records
    def get_all_patients(self):
        self.cursor.execute("SELECT * FROM patients")
        return self.cursor.fetchall()
    
    def get_patient_by_condition(self, name, tel, gender):
        query = "SELECT * FROM patients WHERE"
        conditions = []

        if name != "":
            conditions.append("full_name like '" + name + "%'")
        if tel != "":
            conditions.append("telephone = '" + tel + "'")
        if gender != "":
            conditions.append("gender = '" + gender + "'")

        if conditions:
            for i in range(len(conditions)):
                if i == 0:
                    query += " " + conditions[i]
                else:
                    query += " AND " + conditions[i]

        if conditions:
            self.cursor.execute(query)
        else:
            # If no search criteria provided, fetch all patients
            self.cursor.execute("SELECT * FROM patients")

        patients = self.cursor.fetchall()
        
        return patients

    # Update patient record
    def update_patient(self, patient_id, full_name, gender, birthdate, telephone, home_address, remark, allergic_history, past_medical_history):
        try:
            self.cursor.execute("UPDATE patients SET full_name=?, gender=?, birthdate=?, telephone=?, home_address=?, remark=?, allergic_history=?, past_medical_history=? WHERE id=?",
                       (full_name, gender, birthdate, telephone, home_address, remark, allergic_history, past_medical_history, patient_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error updating patient:", e)
            self.conn.rollback()  # Rollback the changes in case of an error
            raise 

    # Delete patient record
    def delete_patient(self, patient_id):
        self.cursor.execute("DELETE FROM patients WHERE id=?", (patient_id,))
        self.conn.commit()

    # Create visit record
    def insert_visit(self, patient_id, visit_date, chief_complaint, present_illness):
        self.cursor.execute("INSERT INTO visits (patient_id, visit_date, chief_complaint, present_illness) VALUES (?, ?, ?, ?)", (patient_id, visit_date, chief_complaint, present_illness))
        self.conn.commit()
        return self.cursor.lastrowid #visit id

    # Read visit records for a patient
    def get_visits_by_patient(self, patient_id):
        self.cursor.execute("SELECT * FROM visits WHERE patient_id=?", (patient_id,))
        return self.cursor.fetchall()
    
    def update_visits_by_visit_id(self, visit_id, chief_complaint, present_illness):
        self.cursor.execute("UPDATE visits SET chief_complaint=?, present_illness=? WHERE id=?",
                       (chief_complaint, present_illness, visit_id))
        self.conn.commit()
    
    def delete_visit_by_patient(self, patient_id):
        self.cursor.execute("DELETE FROM visits WHERE patient_id=?", (patient_id,))
        self.conn.commit()

    def delete_visit_by_date(self, visit_date):
        self.cursor.execute("DELETE FROM visits WHERE visit_date=?", (visit_date,))
        self.conn.commit()
        
    def delete_visit_by_visit_id(self, visit_id):
        self.cursor.execute("DELETE FROM visits WHERE id=?", (visit_id,))
        self.conn.commit()
        
    
    # Create log record
    def insert_log(self, visit_id, examination_details, diagnosis, remedy):
        self.cursor.execute("INSERT INTO logs (visit_id, examination_details, diagnosis, remedy) VALUES (?, ?, ?, ?)",
                       (visit_id, examination_details, diagnosis, remedy))
        self.conn.commit()

    # Read log records for a visit
    def get_logs_by_visit(self, visit_id):
        self.cursor.execute("SELECT * FROM logs WHERE visit_id=?", (visit_id,))
        return self.cursor.fetchall()

    # Update log record
    def update_log(self, log_id, examination_details, diagnosis, remedy):
        self.cursor.execute("UPDATE logs SET examination_details=?, diagnosis=?, remedy=? WHERE id=?",
                       (examination_details, diagnosis, remedy, log_id))
        self.conn.commit()
        
    def update_log_by_visit(self, visit_id, examination_details, diagnosis, remedy):
        self.cursor.execute("UPDATE logs SET examination_details=?, diagnosis=?, remedy=? WHERE visit_id=?",
                       (examination_details, diagnosis, remedy, visit_id))
        self.conn.commit()

    # Delete log record
    def delete_log(self, log_id):
        self.cursor.execute("DELETE FROM logs WHERE id=?", (log_id,))
        self.conn.commit()
        
    def delete_log_by_visit_id(self, visit_id):
        self.cursor.execute("DELETE FROM logs WHERE visit_id = ?", (visit_id,))
        self.conn.commit()
        
    def get_all_patient_info_by_id(self, patient_id):
        # Query to fetch patient information by patient_id
        query = '''SELECT patients.full_name, patients.gender, patients.birthdate, patients.telephone,
                           visits.visit_date, visits.chief_complaint, visits.present_illness,
                           logs.examination_details, logs.diagnosis, logs.remedy
                    FROM patients
                    LEFT JOIN visits ON patients.id = visits.patient_id
                    LEFT JOIN logs ON visits.id = logs.visit_id
                    WHERE patients.id = ?'''

        self.cursor.execute(query, (patient_id,))
        patient_info = self.cursor.fetchone()
        return patient_info
    def get_one_patient_visits_and_logs(self, patient_id):
        self.cursor.execute('''
            SELECT v.visit_date, v.chief_complaint, v.present_illness, 
                   l.examination_details, l.diagnosis, l.remedy
            FROM visits AS v
            INNER JOIN logs AS l ON v.id = l.visit_id
        ''')
        patient_info = self.cursor.fetchall()
        return patient_info
    def __del__(self):
        self.cursor.close()
        self.conn.close()
