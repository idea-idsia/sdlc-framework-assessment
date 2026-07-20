Python
'''
This file contains the Database class, which is responsible for interacting with the SQLite database.
It provides methods for inserting, retrieving, and updating tickets in the database.
'''
import sqlite3
class Database:
    def __init__(self):
        self.conn = sqlite3.connect("tickets.db")
        self.cursor = self.conn.cursor()
        # Create table if it does not exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY,
                description TEXT,
                status TEXT DEFAULT 'open',
                opening_date DATE,
                last_modification_date DATE,
                closing_date DATE,
                category TEXT
            )
        """)
        self.conn.commit()
    def insert_ticket(self, ticket):
        '''
        Insert a new ticket into the database.
        '''
        try:
            self.cursor.execute("""
                INSERT INTO tickets (description, status, opening_date, last_modification_date, closing_date, category)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                ticket.description,
                ticket.status,
                ticket.opening_date,
                ticket.last_modification_date,
                ticket.closing_date,
                ticket.category
            ))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting ticket: {e}")
    def get_tickets(self):
        '''
        Retrieve all tickets from the database.
        '''
        try:
            self.cursor.execute("SELECT * FROM tickets")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving tickets: {e}")
            return []
    def update_ticket(self, ticket_id, new_status):
        '''
        Update the status of a ticket in the database.
        '''
        try:
            self.cursor.execute("UPDATE tickets SET status = ? WHERE id = ?", (new_status, ticket_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating ticket: {e}")