import pandas as pd

patients = []

file = open("../raw_data/adt.hl7", "r")
lines = file.readlines()

print("Total lines read:", len(lines))

current_patient = {}

for line in lines:
    line = line.strip()

    if line.startswith("PID"):
        fields = line.split("|")

        patient_id = fields[3]
        name = fields[5]
        gender = fields[8]

        last_name, first_name = name.split("^")

        current_patient = {
            "patient_id": patient_id,
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender
        }

    if line.startswith("PV1"):
        patients.append(current_patient)

df = pd.DataFrame(patients)

print(df)

df.to_csv("../patients.csv", index=False)
import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=HealthcarePipeline;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

for index, row in df.iterrows():
    cursor.execute(
        "INSERT INTO patients (patient_id, first_name, last_name, gender) VALUES (?, ?, ?, ?)",
        row["patient_id"],
        row["first_name"],
        row["last_name"],
        row["gender"]
    )

conn.commit()

print("Data inserted into SQL Server successfully.")