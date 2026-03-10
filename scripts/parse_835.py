import pandas as pd
import pyodbc

payments = []

# Read the raw 835 file
with open("../raw_data/payments835.txt", "r") as file:
    lines = file.readlines()

# Parse the file
for line in lines:
    line = line.strip()

    if line.startswith("CLP"):
        parts = line.split("*")

        claim_id = int(parts[1])
        billed_amount = int(parts[3])
        paid_amount = int(parts[4])
        adjustment = int(parts[5].replace("~", ""))

        payments.append({
            "claim_id": claim_id,
            "billed_amount": billed_amount,
            "paid_amount": paid_amount,
            "adjustment": adjustment
        })

# Convert to DataFrame
df = pd.DataFrame(payments)

print(df)

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=HealthcarePipeline;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# Insert into SQL table
for index, row in df.iterrows():
    cursor.execute(
        "INSERT INTO payments VALUES (?, ?, ?, ?)",
        int(row["claim_id"]),
        int(row["billed_amount"]),
        int(row["paid_amount"]),
        int(row["adjustment"])
    )

conn.commit()

print("Payments loaded into SQL Server.")