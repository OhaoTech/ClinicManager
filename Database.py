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
                            full_name TEXT,
                            gender TEXT,
                            birthdate TEXT,
                            telephone TEXT,
                            home_address TEXT,
                            remark TEXT,
                            allergic_history TEXT,
                            past_medical_history TEXT
                            )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS visits (
                        id INTEGER PRIMARY KEY,
                        patient_id INTEGER,
                        visit_date TEXT,
                        chief_complaint TEXT,
                        FOREIGN KEY (patient_id) REFERENCES patients(id))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS examinations (
                        id INTEGER PRIMARY KEY,
                        visit_id INTEGER,
                        examination_details TEXT,
                        FOREIGN KEY (visit_id) REFERENCES visits(id))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS prescriptions (
                        id INTEGER PRIMARY KEY,
                        visit_id INTEGER,
                        prescription_details TEXT,
                        FOREIGN KEY (visit_id) REFERENCES visits(id))''')


    # Create patient record
    def insert_patient(self, full_name, gender, birthdate, telephone, home_address, remark, allergic_history, past_medical_history):
        self.cursor.execute("INSERT INTO patients (full_name, gender, birthdate, telephone, home_address, remark, allergic_history, past_medical_history) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (full_name, gender, birthdate, telephone, home_address, remark, allergic_history, past_medical_history))
        self.conn.commit()

    # Read patient records
    def get_all_patients(self):
        self.cursor.execute("SELECT * FROM patients")
        return self.cursor.fetchall()

    # Update patient record
    def update_patient(self, patient_id, full_name, gender, birthdate, telephone, home_address, remark, allergic_history, past_medical_history):
        self.cursor.execute("UPDATE patients SET full_name=?, gender=?, birthdate=?, telephone=?, home_address=?, remark=?, allergic_history=?, past_medical_history=?, WHERE id=?",
                   (full_name, gender, birthdate, telephone, home_address, remark, allergic_history, past_medical_history, patient_id))
        self.conn.commit()

    # Delete patient record
    def delete_patient(self, patient_id):
        self.cursor.execute("DELETE FROM patients WHERE id=?", (patient_id,))
        self.conn.commit()

    # Create visit record
    def insert_visit(self, patient_id, visit_date, chief_complaint):
        self.cursor.execute("INSERT INTO visits (patient_id, visit_date, chief_complaint) VALUES (?, ?, ?)", (patient_id, visit_date, chief_complaint))
        self.conn.commit()

    # Read visit records for a patient
    def get_visits_by_patient(self, patient_id):
        self.cursor.execute("SELECT * FROM visits WHERE patient_id=?", (patient_id,))
        return self.cursor.fetchall()

    # Create examination record
    def insert_examination(self, visit_id, examination_details):
        self.cursor.execute("INSERT INTO examinations (visit_id, examination_details) VALUES (?, ?)", (visit_id, examination_details))
        self.conn.commit()

    # Read examination records for a visit
    def get_examinations_by_visit(self, visit_id):
        self.cursor.execute("SELECT * FROM examinations WHERE visit_id=?", (visit_id,))
        return self.cursor.fetchall()

    # Create prescription record
    def insert__prescription(self, visit_id, prescription_details):
        self.cursor.execute("INSERT INTO prescriptions (visit_id, prescription_details) VALUES (?, ?)", (visit_id, prescription_details))
        self.conn.commit()

    # Read prescription records for a visit
    def get_prescriptions_by_visit(self, visit_id):
        self.cursor.execute("SELECT * FROM prescriptions WHERE visit_id=?", (visit_id,))
        return self.cursor.fetchall()



    def __del__(self):
        self.cursor.close()
        self.conn.close()
