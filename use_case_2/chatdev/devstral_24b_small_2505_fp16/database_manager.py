'''
Database Manager for CRUD operations on tickets.
'''
import sqlite3
class DatabaseManager:
    def __init__(self, db_name="ticket_management.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                category TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'open',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        '''
        self.cursor.execute(query)
        self.conn.commit()
    def add_ticket(self, description, category, status):
        query = "INSERT INTO tickets (description, category, status) VALUES (?, ?, ?)"
        self.cursor.execute(query, (description, category, status))
        self.conn.commit()
        return self.cursor.lastrowid
    def get_tickets(self, status=None):
        if status:
            query = f"SELECT * FROM tickets WHERE status='{status}'"
        else:
            query = "SELECT * FROM tickets"
        return self.cursor.execute(query).fetchall()
    def update_ticket(self, ticket_id, description=None, category=None, status=None):
        updates = []
        params = []
        if description is not None:
            updates.append("description=?")
            params.append(description)
        if category is not None:
            updates.append("category=?")
            params.append(category)
        if status is not None:
            updates.append("status=?")
            params.append(status)
        query = f"UPDATE tickets SET {', '.join(updates)} WHERE id=?"
        params.append(ticket_id)
        self.cursor.execute(query, tuple(params))
        self.conn.commit()
        return True