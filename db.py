import sqlite3
import os

db_path = os.path.join("db", "users.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Tworzymy tabelę users
c.execute("DROP TABLE IF EXISTS users")
c.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# Dodajemy przykładowe konto
c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "admin123"))
c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user", "user123"))

conn.commit()
conn.close()
print("Baza danych zainicjalizowana.")
