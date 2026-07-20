'''
Database interaction module.
'''
import sqlite3
class Database:
    def __init__(self, db_name='tickets.db'):
        self.db_name = db_name
        self.conn = None
    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            return self.conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None
    def close(self):
        if self.conn:
            self.conn.close()
    def create_table(self):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tickets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    status TEXT NOT NULL,
                    description TEXT NOT NULL,
                    category TEXT,
                    opening_date TEXT NOT NULL,
                    last_modification_date TEXT NOT NULL,
                    closing_date TEXT,
                    visibility TEXT DEFAULT 'private',
                    assigned_to TEXT
                )
            ''')
            self.conn.commit()
            cursor.close()
    def get_tickets(self, user_role='user'):
        if self.conn:
            cursor = self.conn.cursor()
            if user_role == 'admin':
                cursor.execute("SELECT * FROM tickets")
                tickets = cursor.fetchall()
            else:
                cursor.execute("SELECT * FROM tickets")
                tickets = cursor.fetchall()
            return tickets
        else:
            return []
    def update_ticket_status(self, ticket_id, new_status):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE tickets SET status = ? WHERE id = ?", (new_status, ticket_id))
            self.conn.commit()
            return True
        else:
            return False
    def delete_ticket(self, ticket_id):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
            self.conn.commit()
            return True
        else:
            return False
    def insert_ticket(self, status, description, category, opening_date, last_modification_date, closing_date):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO tickets (status, description, category, opening_date, last_modification_date, closing_date) VALUES (?, ?, ?, ?, ?, ?)",
                           (status, description, category, opening_date, last_modification_date, closing_date))
            self.conn.commit()
            return True
        else:
            return False