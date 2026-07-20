# Import necessary libraries
import sqlite3
'''
Database manager class.
It creates a connection to the database, 
and provides methods for executing queries and creating tables.
'''
class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect("tickets.db")
        self.cursor = self.conn.cursor()
    def create_tables(self):
        # Create tickets table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY,
                status TEXT,
                description TEXT,
                category TEXT,
                opening_date DATE,
                last_modification_date DATE,
                closing_date DATE
            );
        """)
        # Create users table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                role TEXT
            );
        """)
        self.conn.commit()
    def execute_query(self, query, params):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
    def insert_ticket(self, ticket):
        query = "INSERT INTO tickets (status, description, category, opening_date, last_modification_date, closing_date) VALUES (?, ?, ?, ?, ?, ?)"
        params = (ticket.status, ticket.description, ticket.category, ticket.opening_date, ticket.last_modification_date, ticket.closing_date)
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting ticket: {e}")
    def update_ticket(self, ticket):
        query = "UPDATE tickets SET status = ?, description = ?, category = ?, opening_date = ?, last_modification_date = ?, closing_date = ? WHERE id = ?"
        params = (ticket.status, ticket.description, ticket.category, ticket.opening_date, ticket.last_modification_date, ticket.closing_date, ticket.id)
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating ticket: {e}")
    def delete_ticket(self, ticket_id):
        query = "DELETE FROM tickets WHERE id = ?"
        params = (ticket_id,)
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error deleting ticket: {e}")