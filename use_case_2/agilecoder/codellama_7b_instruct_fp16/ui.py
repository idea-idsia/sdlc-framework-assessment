'''
File: ui.py
Author: $USERNAME
Description: This file contains the user interface for the ticket management system.
'''
from tkinter import *
from tkinter.ttk import *
import sqlite3
import constants
class TicketUI():
    '''
    The main UI class for the ticket management system.
    '''
    def __init__(self, master):
        self.master = master
        self.master.title("Ticket Management System")
        self.create_widgets()
        self.update_tickets()
    def create_widgets(self):
        '''
        Creates the widgets for the UI.
        '''
        Label(self.master, text="Tickets").grid(row=0, column=1)
        Button(self.master, text="Create Ticket", command=self.create_ticket).grid(row=1, column=1)
        self.tickets = Listbox(self.master)
        self.tickets.grid(row=2, column=1)
    def create_ticket(self):
        '''
        Creates a new ticket in the database and updates the UI.
        '''
        description = input("Please enter a brief description of the issue: ")
        category = constants.CATEGORY_CHOICES[input("Please select a category for this ticket (facility management, technical IT, services complaints): ")]
        self.create_ticket_in_db(description, category)
    def create_ticket_in_db(self, description, category):
        '''
        Creates a new ticket in the database.
        Args:
            description: The brief description of the issue.
            category: The category of the ticket (facility management, technical IT, services complaints).
        '''
        query = "INSERT INTO tickets (description, category) VALUES (?, ?)"
        values = (description, category)
        self.sqlite_db.execute(query, values)
    def update_tickets(self):
        '''
        Updates the list of tickets in the UI.
        '''
        query = "SELECT id, description, category FROM tickets"
        results = self.sqlite_db.execute(query).fetchall()
        for row in results:
            self.tickets.insert(END, str(row[0]) + ": " + row[1] + " (" + constants.CATEGORY_CHOICES[row[2]] + ")")