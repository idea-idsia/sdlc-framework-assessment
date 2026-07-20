'''
ticket_ui.py
This file contains the GUI for the ticket management system.
'''
from tkinter import *
import sqlite3
import constants
class TicketUI():
    def __init__(self, master):
        self.master = master
        self.master.title("Ticket Management System")
        self.create_widgets()
    def create_widgets(self):
        # Create a new ticket in the database and update the UI
        Label(self.master, text="Create Ticket").grid(row=0, column=1)
        Button(self.master, text="Create", command=self.create_ticket).grid(row=1, column=1)
        self.tickets = Listbox(self.master)
        self.tickets.grid(row=2, column=1)
    def create_ticket(self):
        # Create a new ticket in the database and update the UI
        description = input("Please enter a brief description of the issue: ")
        category = constants.CATEGORY_CHOICES[input("Please select a category for this ticket (facility management, technical IT, services complaints): ")]
        self.create_ticket_in_db(description, category)
    def create_ticket_in_db(self, description, category):
        # Create a new ticket in the database
        query = "INSERT INTO tickets (description, category) VALUES (?, ?)"
        values = (description, category)
        self.conn.cursor().execute(query, values)
        self.conn.commit()
    def update_tickets(self):
        # Update the list of tickets in the UI
        query = "SELECT id, description, category FROM tickets"
        results = self.conn.cursor().execute(query).fetchall()
        for row in results:
            print(row)
    def close(self):
        # Close the database connection
        self.conn.close()