-- Total Revenue
SELECT SUM(paid_amount) AS total_revenue
FROM payments;

-- Total Claims
SELECT COUNT(*) AS total_claims
FROM claims;

-- Revenue by Procedure
SELECT 
procedure_code,
SUM(paid_amount) AS revenue
FROM claims c
JOIN payments p
ON c.claim_id = p.claim_id
GROUP BY procedure_code
ORDER BY revenue DESC;

-- Revenue by Patient
SELECT 
p.first_name,
p.last_name,
SUM(pay.paid_amount) AS revenue
FROM patients p
JOIN claims c
ON p.patient_id = c.patient_id
JOIN payments pay
ON c.claim_id = pay.claim_id
GROUP BY p.first_name, p.last_name
ORDER BY revenue DESC;