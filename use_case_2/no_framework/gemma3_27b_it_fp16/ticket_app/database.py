import sqlite3
from models import Ticket, Message

class Database:
    def __init__(self, db_name="tickets.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                category TEXT NOT NULL,
                status TEXT NOT NULL,
                opening_date TEXT NOT NULL,
                last_modification_date TEXT NOT NULL,
                closing_date TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticket_id INTEGER NOT NULL,
                sender TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                FOREIGN KEY (ticket_id) REFERENCES tickets(id)
            )
        """)
        self.conn.commit()

    def insert_ticket(self, ticket):
        self.cursor.execute("""
            INSERT INTO tickets (description, category, status, opening_date, last_modification_date)
            VALUES (?, ?, ?, ?, ?)
        """, (ticket.description, ticket.category, ticket.status, ticket.opening_date.isoformat(), ticket.last_modification_date.isoformat()))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_tickets(self, status=None):
        if status:
            self.cursor.execute("SELECT * FROM tickets WHERE status = ?", (status,))
        else:
            self.cursor.execute("SELECT * FROM tickets")
        return [Ticket(
            description=row[1],
            category=row[2],
            status=row[3],
            opening_date=datetime.datetime.fromisoformat(row[4]),
        ) for row in self.cursor.fetchall()]

    def update_ticket_status(self, ticket_id, new_status):
        self.cursor.execute("UPDATE tickets SET status = ? WHERE id = ?", (new_status, ticket_id))
        self.conn.commit()

    def insert_message(self, message):
        self.cursor.execute("""
            INSERT INTO messages (ticket_id, sender, content, timestamp)
            VALUES (?, ?, ?, ?)
        """, (message.ticket_id, message.sender, message.content, message.timestamp.isoformat()))
        self.conn.commit()

    def get_messages_by_ticket_id(self, ticket_id):
        self.cursor.execute("SELECT * FROM messages WHERE ticket_id = ?", (ticket_id,))
        return [Message(
            ticket_id=row[1],
            sender=row[2],
            content=row[3],
            timestamp=datetime.datetime.fromisoformat(row[4]),
        ) for row in self.cursor.fetchall()]

    def close(self):
        self.conn.close()