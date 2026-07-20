'''
Module to manage database operations.
Includes classes and methods to interact with SQLite database for managing tickets.
'''
import sqlite3
from datetime import datetime
class DatabaseManager:
    def __init__(self, db_name="tickets.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.setup_tables()
    def setup_tables(self):
        # Create table if it doesn't exist
        query = """
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY,
                status TEXT DEFAULT 'open',
                description TEXT,
                category TEXT,
                opening_date DATE DEFAULT CURRENT_DATE,
                last_modification_date DATE,
                closing_date DATE
            )
        """
        self.cursor.execute(query)
        self.connection.commit()
    def add_ticket(self, ticket):
        query = "INSERT INTO tickets (status, description, category) VALUES (?, ?, ?)"
        values = (ticket['status'], ticket['description'], ticket['category'])
        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor.lastrowid
    def update_ticket_status(self, ticket_id, status):
        query = "UPDATE tickets SET status=? WHERE id=?"
        self.cursor.execute(query, (status, ticket_id))
        self.connection.commit()
    def close_ticket(self, ticket_id, closing_date=None):
        if not closing_date:
            closing_date = datetime.now().strftime("%Y-%m-%d")
        # Update closing date and status to 'closed'
        query = "UPDATE tickets SET status='closed', closing_date=? WHERE id=?"
        self.cursor.execute(query, (closing_date, ticket_id))
        self.connection.commit()
    def query_all(self):
        """Fetch all tickets from the database."""
        query = "SELECT * FROM tickets"
        self.cursor.execute(query)
        return [{'id': row[0], 'status': row[1], 'description': row[2],
                 'category': row[3], 'opening_date': row[4], 
                 'last_modification_date': row[5], 'closing_date': row[6]} for row in self.cursor.fetchall()]
    def update_last_modification(self, ticket_id):
        """Update last modification date."""
        query = "UPDATE tickets SET last_modification_date=? WHERE id=?"
        self.cursor.execute(query, (datetime.now().strftime("%Y-%m-%d"), ticket_id))
        self.connection.commit()