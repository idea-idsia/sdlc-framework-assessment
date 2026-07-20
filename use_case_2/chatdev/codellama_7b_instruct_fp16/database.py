'''
Implements a database for storing ticket data and providing basic functionalities to interact with it.
'''
import sqlite3
from tkinter import messagebox
class Ticket:
    def __init__(self, number, description, category):
        self.number = number
        self.description = description
        self.category = category
    def __repr__(self):
        return f"Ticket({self.number}, {self.description}, {self.category})"
class Database:
    def __init__(self, filename="ticket_database.db"):
        self.filename = filename
        self.connection = sqlite3.connect(self.filename)
        self.cursor = self.connection.cursor()
        self._create_tables()
    def _create_tables(self):
        """Creates the tables for storing ticket data"""
        # Create the tickets table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tickets (number TEXT PRIMARY KEY, description TEXT, category TEXT, status TEXT, priority TEXT, assigned_user TEXT)")
    def save_ticket(self, ticket):
        """Saves a new ticket to the database"""
        if isinstance(ticket, Ticket):
            self.cursor.execute("INSERT INTO tickets VALUES (?, ?, ?, ?, ?, ?)", (ticket.number, ticket.description, ticket.category, "open", "medium", None))
            self.connection.commit()
            messagebox.showinfo("Success", "Ticket saved successfully")
        else:
            raise ValueError("Ticket must be of type Ticket")
    def get_tickets(self):
        """Returns all the tickets in the database"""
        self.cursor.execute("SELECT * FROM tickets")
        return [Ticket(*row) for row in self.cursor.fetchall()]