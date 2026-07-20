'''
Manages database interactions for ticket management.
'''
import sqlite3
from datetime import datetime
from tkinter import messagebox
class Ticket:
    def __init__(self, ticket_id, description, status, category, opening_date, last_modification_date, closing_date):
        self.ticket_id = ticket_id
        self.description = description
        self.status = status
        self.category = category
        self.opening_date = opening_date
        self.last_modification_date = last_modification_date
        self.closing_date = closing_date
class DatabaseManager:
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
                    last_modification_date TEXT NOT NULL,
                    closing_date TEXT
                )
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to create table: {e}")
            raise  # Re-raise the exception to signal the error
    def create_ticket(self, description, category):
        try:
            opening_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute("""
                INSERT INTO tickets (description, status, category, opening_date, last_modification_date)
                VALUES (?, ?, ?, ?, ?)
            """, (description, "open", category, opening_date, opening_date))
            self.conn.commit()
            return self.cursor.lastrowid  # Return the new ticket ID
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to create ticket: {e}")
            raise
    def get_ticket_by_id(self, ticket_id):
        try:
            self.cursor.execute("""
                SELECT ticket_id, description, status, category, opening_date, last_modification_date, closing_date
                FROM tickets
                WHERE ticket_id = ?
            """, (ticket_id,))
            row = self.cursor.fetchone()
            if row:
                return Ticket(*row)
            else:
                return None
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to get ticket: {e}")
            return None
    def get_all_tickets(self):
        try:
            self.cursor.execute("""
                SELECT ticket_id, description, status, category, opening_date, last_modification_date, closing_date
                FROM tickets
            """)
            rows = self.cursor.fetchall()
            return [Ticket(*row) for row in rows]
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to get all tickets: {e}")
            return []
    def get_tickets_for_user(self, user_type):
        try:
            if user_type == "simple":
                self.cursor.execute("""
                    SELECT ticket_id, description, status, category, opening_date, last_modification_date, closing_date
                    FROM tickets
                    WHERE status IN ('open', 'active')
                """)
            else:
                self.cursor.execute("""
                    SELECT ticket_id, description, status, category, opening_date, last_modification_date, closing_date
                    FROM tickets
                """)
            rows = self.cursor.fetchall()
            return [Ticket(*row) for row in rows]
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to get tickets for user: {e}")
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
            messagebox.showerror("Database Error", f"Failed to update ticket: {e}")
    def close_ticket(self, ticket_id):
        try:
            self.cursor.execute("""
                UPDATE tickets
                SET status = 'closed'
                WHERE ticket_id = ?
            """, (ticket_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to close ticket: {e}")