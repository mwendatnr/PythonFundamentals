import sqlite3

conn = sqlite3.connect('example.dp')
print("Opened database successfully")

conn.execute('''CREATE TABLE EMPLOYEE(
ID INT PRIMARY KEY NOT NULL,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT,
AGE INT,
SALARY REAL)
''')

print("Successfully created employee table")
conn.close()