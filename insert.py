import sqlite3

conn = sqlite3.connect('example.dp')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEE VALUES (1,'Mary','Kamau',45,34000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (2,'James','Wekesa',28,134000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (3,'Ann','Nduta',52,57000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (4,'Joe','Were',67,120000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (5,'Jane','Kadzo',25,24000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (6,'Paul','Salim',56,574000.00)")

conn.commit()

print("Successfully added records")

conn.close()