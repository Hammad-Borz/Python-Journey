import sqlite3
connection = sqlite3.connect("students.db")
print("Database Created Successfully")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")
connection.commit()
print("Table Created Successfully")
cursor.execute(
    "INSERT INTO students (name, age) VALUES (?, ?)",
    ("BORZ", 18)
)
connection.commit()
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print(rows)
connection.close()