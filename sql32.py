import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    age INTEGER
)
""")
cursor.execute("INSERT INTO students VALUES ('Ali', 22)")
cursor.execute("INSERT INTO students VALUES ('Ahmed', 25)")
cursor.execute("INSERT INTO students VALUES ('Sara', 21)")

connection.commit()
cursor.execute("SELECT * FROM students WHERE age > 21")

students = cursor.fetchall()

print(students)