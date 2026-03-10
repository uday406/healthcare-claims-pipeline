import pandas as pd
import pyodbc

claims = []

with open("../raw_data/claims837.txt", "r") as file:
    lines = file.readlines()

current_claim = {}

for line in lines:
    line = line.strip()

    if line.startswith("CLM"):
        parts = line.split("*")
        current_claim["claim_id"] = int(parts[1])
        current_claim["billed_amount"] = int(parts[2].replace("~",""))

    if line.startswith("PAT"):
        parts = line.split("*")
        current_claim["patient_id"] = parts[1].replace("~","")

    if line.startswith("SV1"):
        parts = line.split("*")
        proc = parts[1]
        current_claim["procedure_code"] = proc.split(":")[1]

    if line.startswith("HI"):
        parts = line.split("*")
        diag = parts[1]
        current_claim["diagnosis_code"] = diag.split(":")[1].replace("~","")

        claims.append(current_claim.copy())

df = pd.DataFrame(claims)

print(df)

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=HealthcarePipeline;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

for index, row in df.iterrows():
    cursor.execute(
        "INSERT INTO claims VALUES (?, ?, ?, ?, ?)",
        row["claim_id"],
        row["patient_id"],
        row["procedure_code"],
        row["diagnosis_code"],
        row["billed_amount"]
    )

conn.commit()

print("Claims loaded into SQL Server.")