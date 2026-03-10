CREATE TABLE patients (
    patient_id VARCHAR(10),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(1)
);

CREATE TABLE claims (
    claim_id INT,
    patient_id VARCHAR(10),
    procedure_code VARCHAR(10),
    diagnosis_code VARCHAR(10),
    billed_amount INT
);

CREATE TABLE payments (
    claim_id INT,
    billed_amount INT,
    paid_amount INT,
    adjustment INT
);