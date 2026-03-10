\# Healthcare Claims ETL Pipeline



\## Overview



This project demonstrates an end-to-end healthcare data pipeline that processes raw healthcare transaction data and loads it into a structured database for analytics.



\## Data Sources



\* HL7 ADT (Patient Admission Data)

\* EDI 837 (Insurance Claims)

\* EDI 835 (Insurance Payments)



\## ETL Pipeline



Raw Healthcare Files

↓

Python Parsing Scripts

↓

Structured Tables in SQL Server

↓

Analytics Queries



\## Database Tables



patients – patient demographic data

claims – insurance claims submitted

payments – insurance payment responses



\## Technologies Used



Python

SQL Server

Healthcare EDI formats (HL7, 837, 835)



\## Project Structure



raw\_data/ – source healthcare files

scripts/ – Python ETL scripts

sql/ – database table creation scripts



