'''
Handles database operations like inserting, updating tickets, and fetching data.
'''
import sqlite3
class DatabaseManager:
    def __init__(self, db_name="tickets.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    def insert_ticket(self, ticket: Ticket):
        query = 'INSERT INTO tickets (category, description, status, created_time, last_modified_time) VALUES (?, ?, "open", CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)'
        self.cursor.execute(query, (ticket.category, ticket.description))
        self.conn.commit()
    def update_ticket_status(self, id_: int, new_status: str):
        query = 'UPDATE tickets SET status = ?, last_modified_time = CURRENT_TIMESTAMP WHERE id = ?'
        self.cursor.execute(query, (new_status, id_))
        self.conn.commit()
    def get_open_tickets(self) -> list:
        query = "SELECT * FROM tickets WHERE status = 'open'"
        self.cursor.execute(query)
        return self.cursor.fetchall()