'''
Database Manager Class.
'''
import sqlite3
class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('tickets.db')
        self.create_tickets_table()
        self.create_messages_table()
    def create_tickets_table(self):
        try:
            query = '''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                category TEXT NOT NULL,
                status TEXT DEFAULT 'open',
                opened_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                closing_date TIMESTAMP
            )
            '''
            cursor = self.conn.cursor()
            cursor.execute(query)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    def create_messages_table(self):
        try:
            query = '''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticket_id INTEGER NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (ticket_id) REFERENCES tickets(id)
            )
            '''
            cursor = self.conn.cursor()
            cursor.execute(query)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    def add_ticket(self, title, description, category):
        try:
            cursor = self.conn.cursor()
            query = 'INSERT INTO tickets (title, description, category) VALUES (?, ?, ?)'
            cursor.execute(query, (title, description, category))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    def modify_ticket(self, ticket_id, new_title, new_description):
        try:
            cursor = self.conn.cursor()
            query = 'UPDATE tickets SET title=?, description=?, last_modified_at=CURRENT_TIMESTAMP WHERE id=?'
            cursor.execute(query, (new_title, new_description, ticket_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    def close_connection(self):
        if self.conn:
            self.conn.close()