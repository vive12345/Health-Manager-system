import sqlite3

con = sqlite3.connect("employee.db")
print("Database opened successfully")

con.execute(
    "create table employee (id INTEGER PRIMARY KEY AUTOINCREMENT, aname TEXT, time TEXT)")

print("Table created successfully")

con.close()