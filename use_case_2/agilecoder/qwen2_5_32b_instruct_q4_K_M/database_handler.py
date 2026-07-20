'''
Handles CRUD operations on tickets and user interactions.
Manages data integrity and validation.
'''
import sqlite3
class DatabaseHandler:
    def __init__(self):
        self.conn = sqlite3.connect('tickets.db')
        self.cursor = self.conn.cursor()
        self._create_tables()
    def _create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tickets
                            (id INTEGER PRIMARY KEY, description TEXT, category TEXT, status TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS messages
                            (id INTEGER PRIMARY KEY, ticket_id INTEGER, message TEXT, sender_role TEXT,
                            FOREIGN KEY(ticket_id) REFERENCES tickets(id))''')
    def insert_ticket(self, description, category):
        if not description or not category:
            raise ValueError("Description and Category cannot be empty.")
        self.cursor.execute('INSERT INTO tickets (description, category, status) VALUES (?, ?, ?)',
                            (description, category, 'open'))
        self.conn.commit()
    def update_ticket(self, ticket_id, description=None, category=None):
        if not description and not category:
            raise ValueError("At least one field must be provided for modification.")
        query = "UPDATE tickets SET "
        params = []
        if description:
            query += "description = ?, "
            params.append(description)
        if category:
            query += "category = ?, "
            params.append(category)
        query = query.rstrip(", ") + f" WHERE id = ?"
        params.append(ticket_id)
        self.cursor.execute(query, tuple(params))
        self.conn.commit()
    def get_messages(self, ticket_id):
        return self.cursor.execute('SELECT * FROM messages WHERE ticket_id = ?', (ticket_id,)).fetchall()
    def add_message(self, ticket_id, message, sender_role):
        if not message or sender_role not in ['helpdesk', 'user']:
            raise ValueError("Invalid message or sender role.")
        self.cursor.execute(
            "INSERT INTO messages (ticket_id, message, sender_role) VALUES (?, ?, ?)",
            (ticket_id, message, sender_role)
        )
        self.conn.commit()
    def get_open_tickets(self, period):
        return self.cursor.execute('SELECT * FROM tickets WHERE status = ?', ('open',)).fetchall()
    def avg_resolution_time(self):
        # Implement logic to calculate average resolution time
        pass
    def category_counts(self):
        # Implement logic to count categories
        pass