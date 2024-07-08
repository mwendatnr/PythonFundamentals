import sqlite3

conn = sqlite3.connect('example.dp')
print("Opened database successfully")

conn.execute("DELETE FROM EMPLOYEE where ID = 6")
conn.commit()

data = conn.execute("SELECT * FROM EMPLOYEE")

for row in data:
    print("ID: ", row[0])
    print("FIRSTNAME: ", row[1])
    print("LASTNAME: ", row[2])
    print("AGE: ", row[3])
    print("SALARY: ", row[4])

print("Successfully deleted a record")