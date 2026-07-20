'''
Database module for managing tickets.
Provides functions to create, read, update, and delete tickets.
'''
import sqlite3
from ticket import Ticket
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    def create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS tickets (
                    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    status TEXT NOT NULL,
                    category TEXT NOT NULL,
                    opening_date TEXT NOT NULL,
                    last_modification_date TEXT
                )
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Failed to create table: {e}")
            raise
    def create_ticket(self, description, category, opening_date):
        try:
            self.cursor.execute("""
                INSERT INTO tickets (description, status, category, opening_date, last_modification_date)
                VALUES (?, ?, ?, ?, ?)
            """, (description, "open", category, opening_date, opening_date))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Failed to create ticket: {e}")
            raise
    def get_ticket_by_id(self, ticket_id):
        try:
            self.cursor.execute("""
                SELECT ticket_id, description, status, category, opening_date, last_modification_date
                FROM tickets
                WHERE ticket_id = ?
            """, (ticket_id,))
            row = self.cursor.fetchone()
            if row:
                return Ticket(*row)
            else:
                return None
        except sqlite3.Error as e:
            print(f"Failed to get ticket: {e}")
            return None
    def get_all_tickets(self):
        try:
            self.cursor.execute("""
                SELECT ticket_id, description, status, category, opening_date, last_modification_date
                FROM tickets
            """)
            rows = self.cursor.fetchall()
            return [Ticket(*row) for row in rows]
        except sqlite3.Error as e:
            print(f"Failed to get all tickets: {e}")
            return []
    def update_ticket(self, ticket_id, description, status, category):
        try:
            self.cursor.execute("""
                UPDATE tickets
                SET description = ?, status = ?, category = ?
                WHERE ticket_id = ?
            """, (description, status, category, ticket_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Failed to update ticket: {e}")
            raise
    def close_ticket(self, ticket_id):
        try:
            self.cursor.execute("""
                UPDATE tickets
                SET status = 'closed'
                WHERE ticket_id = ?
            """, (ticket_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Failed to close ticket: {e}")
            raise