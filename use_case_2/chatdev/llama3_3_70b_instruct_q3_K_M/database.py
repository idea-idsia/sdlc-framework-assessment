# Database interactions
'''
This module handles database interactions to store and retrieve tickets and user interactions.
'''
import sqlite3
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY,
                status TEXT,
                description TEXT,
                category TEXT,
                opening_date DATE,
                last_modification_date DATE,
                closing_date DATE
            )
        ''')
        self.conn.commit()
    def insert_ticket(self, ticket):
        self.cursor.execute('''
            INSERT INTO tickets (status, description, category, opening_date)
            VALUES (?, ?, ?, ?)
        ''', (ticket.status, ticket.description, ticket.category, ticket.opening_date))
        self.conn.commit()
    def update_ticket(self, ticket):
        self.cursor.execute('''
            UPDATE tickets
            SET status = ?, last_modification_date = ?
            WHERE id = ?
        ''', (ticket.status, ticket.last_modification_date, ticket.id))
        self.conn.commit()
    def get_tickets(self, user_type):
        if user_type == 'helpdesk':
            self.cursor.execute('''
                SELECT * FROM tickets
            ''')
        elif user_type == 'simple_user':
            self.cursor.execute('''
                SELECT * FROM tickets WHERE status IN ('open', 'active')
            ''')
        return self.cursor.fetchall()
    def get_open_tickets(self, period_hours):
        # Calculate the time frame
        now = datetime.datetime.now()
        past = now - datetime.timedelta(hours=period_hours)
        # Query the database for tickets opened within this timeframe that are not closed
        self.cursor.execute('''
            SELECT * FROM tickets 
            WHERE opening_date >= ? AND status != 'closed'
        ''', (past,))
        return self.cursor.fetchall()
    def get_average_resolution_time(self):
        self.cursor.execute('''
            SELECT AVG(strftime('%J', closing_date) - strftime('%J', opening_date)) 
            FROM tickets 
            WHERE status = 'closed'
        ''')
        return self.cursor.fetchone()
    def get_active_tickets_by_category(self):
        self.cursor.execute('''
            SELECT category, COUNT(*) 
            FROM tickets 
            WHERE status = 'active' 
            GROUP BY category
        ''')
        return self.cursor.fetchall()