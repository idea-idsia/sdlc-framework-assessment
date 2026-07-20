'''
DatabaseManager class for handling database interactions.
Uses SQLite to store and retrieve ticket and message data.
'''
import sqlite3
import datetime
class DatabaseManager:
    def __init__(self, db_name):
        """
        Initializes the DatabaseManager with the database name.
        """
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.connect()
        self.create_tables()
    def connect(self):
        """
        Establishes a connection to the SQLite database.
        """
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            raise  # Re-raise the exception
    def disconnect(self):
        """
        Closes the connection to the SQLite database.
        """
        if self.conn:
            self.conn.close()
    def create_tables(self):
        """
        Creates the tickets and messages tables if they don't exist.
        """
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS tickets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    status TEXT NOT NULL,
                    description TEXT NOT NULL,
                    category TEXT NOT NULL,
                    opening_date TEXT NOT NULL,
                    last_modified_date TEXT NOT NULL,
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
        except sqlite3.Error as e:
            print(f"Table creation error: {e}")
            raise
    def insert_ticket(self, status, description, category, opening_date, last_modified_date):
        """
        Inserts a new ticket into the tickets table.
        """
        try:
            self.cursor.execute("""
                INSERT INTO tickets (status, description, category, opening_date, last_modified_date)
                VALUES (?, ?, ?, ?, ?)
            """, (status, description, category, opening_date, last_modified_date))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Ticket insertion error: {e}")
            raise
    def update_ticket_status(self, ticket_id, status):
        """
        Updates the status of a ticket in the tickets table.
        """
        try:
            self.cursor.execute("""
                UPDATE tickets
                SET status = ?, last_modified_date = ?
                WHERE id = ?
            """, (status, datetime.datetime.now().isoformat(), ticket_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Ticket update error: {e}")
            raise
    def get_tickets(self, user_type="simple_user"):
        """
        Retrieves all tickets from the tickets table.
        Filters tickets based on the user type.
        """
        try:
            if user_type == "helpdesk":
                self.cursor.execute("SELECT * FROM tickets")
            else:
                self.cursor.execute("SELECT * FROM tickets WHERE status IN ('open', 'active')")
            return [dict(row) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Ticket retrieval error: {e}")
            raise
    def get_ticket_by_id(self, ticket_id):
        """
        Retrieves a ticket from the tickets table by its ID.
        """
        try:
            self.cursor.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,))
            row = self.cursor.fetchone()
            if row:
                return dict(row)
            else:
                return None
        except sqlite3.Error as e:
            print(f"Ticket retrieval error: {e}")
            raise
    def insert_message(self, ticket_id, sender, content, timestamp):
        """
        Inserts a new message into the messages table.
        """
        try:
            self.cursor.execute("""
                INSERT INTO messages (ticket_id, sender, content, timestamp)
                VALUES (?, ?, ?, ?)
            """, (ticket_id, sender, content, timestamp))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Message insertion error: {e}")
            raise
    def get_messages_by_ticket_id(self, ticket_id):
        """
        Retrieves all messages for a given ticket ID.
        """
        try:
            self.cursor.execute("SELECT * FROM messages WHERE ticket_id = ?", (ticket_id,))
            return [dict(row) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Message retrieval error: {e}")
            raise