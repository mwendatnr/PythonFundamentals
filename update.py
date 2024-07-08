import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("UPDATE EMPLOYEE set SALARY=60000.00 where ID = 1")
conn.commit()

data = conn.execute("SELECT * FROM EMPLOYEE")

for row in data:
    print("ID: ", row[0])
    print("FIRSTNAME: ", row[1])
    print("LASTNAME: ", row[2])
    print("AGE: ", row[3])
    print("SALARY: ", row[4])

print("Successfully updated a record")