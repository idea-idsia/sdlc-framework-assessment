'''
The Database class that handles database connections and operations.
'''
import sqlite3
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()
    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY,
                description TEXT,
                category TEXT,
                status TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT
            )
        """)
        self.conn.commit()
    def insert_data(self, table_name, data):
        if table_name == "tickets":
            self.cursor.execute("INSERT INTO tickets (description, category, status) VALUES (?, ?, ?)", data)
        elif table_name == "users":
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", data)
        self.conn.commit()