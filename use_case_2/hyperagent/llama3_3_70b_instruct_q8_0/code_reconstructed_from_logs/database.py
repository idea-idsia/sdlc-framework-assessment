import sqlite3

class TicketDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        # Create tickets table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY,
                status TEXT DEFAULT 'open',
                description TEXT,
                category TEXT,
                opening_date DATE,
                last_modification_date DATE,
                closing_date DATE
            );
        """)

        # Create messages table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY,
                ticket_id INTEGER,
                message TEXT,
                sender TEXT,
                date DATE,
                FOREIGN KEY (ticket_id) REFERENCES tickets (id)
            );
        """)

    def insert_ticket(self, description, category):
        self.cursor.execute("INSERT INTO tickets (description, category, opening_date) VALUES (?, ?, DATE('now'))", (description, category))
        self.conn.commit()

    def get_tickets(self, status=None):
        if status:
            self.cursor.execute("SELECT * FROM tickets WHERE status = ?", (status,))
        else:
            self.cursor.execute("SELECT * FROM tickets")
        return self.cursor.fetchall()

    def update_ticket_status(self, ticket_id, status):
        self.cursor.execute("UPDATE tickets SET status = ? WHERE id = ?", (status, ticket_id))
        self.conn.commit()

    def insert_message(self, ticket_id, message, sender):
        self.cursor.execute("INSERT INTO messages (ticket_id, message, sender, date) VALUES (?, ?, ?, DATE('now'))", (ticket_id, message, sender))
        self.conn.commit()