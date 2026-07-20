'''
Manages database operations such as inserting, updating, and querying tickets.
'''
import sqlite3
import logging
# Set up logging
logging.basicConfig(level=logging.DEBUG)
class DatabaseManager:
    def __init__(self, db_name="tickets.db"):
        self.conn = None
        self.cursor = None
        self.connect(db_name)
    def connect(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            logging.error(f"Database connection error: {e}")
    def insert_ticket(self, ticket_data):
        query = 'INSERT INTO tickets (category, description, status) VALUES (?, ?, "open")'
        try:
            self.cursor.execute(query, (ticket_data["category"], ticket_data["description"]))
            self.conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Insertion error: {e}")
    def update_ticket_status(self, id_, new_status):
        query = 'UPDATE tickets SET status = ?, last_modified_time = CURRENT_TIMESTAMP WHERE id = ?'
        try:
            self.cursor.execute(query, (new_status, id_))
            self.conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Update error: {e}")
    def get_open_tickets(self):
        query = "SELECT * FROM tickets WHERE status = 'open'"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()  # Use cursor.fetchall() to ensure correct context
        except sqlite3.Error as e:
            logging.error(f"Query error: {e}")