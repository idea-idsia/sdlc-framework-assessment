'''
This module defines the database interaction for the ticket management application.
'''
import sqlite3
class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            return True
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            return False
    def create_table(self):
        if not self.conn:
            return False
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tickets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    status TEXT,
                    description TEXT,
                    category TEXT
                )
            """)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Table creation error: {e}")
            return False
    def get_tickets(self):
        if not self.conn:
            return []
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id, status, description, category FROM tickets")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching tickets: {e}")
            return []
    def insert_ticket(self, description, category):
        if not self.conn:
            return False
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO tickets (status, description, category) VALUES (?, ?, ?)",
                           ('Open', description, category))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error inserting ticket: {e}")
            return False
    def delete_ticket(self, ticket_id):
        if not self.conn:
            return False
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error deleting ticket: {e}")
            return False
    def close(self):
        if self.conn:
            self.conn.close()