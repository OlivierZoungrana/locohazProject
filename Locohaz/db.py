import sqlite3

#conn = sqlite3.connect('admin.db')
conn = sqlite3.connect("admin.db")
"""
conn.execute('''CREATE TABLE Admin
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print ("Table created successfully");
"""
"""
conn.execute("INSERT INTO Admin (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO Admin (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO Admin (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO Admin (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print ("Records created successfully");

conn.close()
"""
def selection():
    cursor = conn.execute("SELECT id, name, address, salary from Admin")
    for row in cursor:
        print(
        "ID = ", row[0])
        print(
        "NAME = ", row[1])
        print(
        "ADDRESS = ", row[2])
        print(
        "SALARY = ", row[3], "\n")

    print("Operation done successfully");
    conn.close()

selection()
