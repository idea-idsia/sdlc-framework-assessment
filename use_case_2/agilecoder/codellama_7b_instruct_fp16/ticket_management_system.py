'''
File: ticket_management_system.py
Author: $USERNAME
Description: This file contains the class that implements the ticket management system functionality.
'''
import sqlite3
from database import Database
from guide import Guide
class TicketManagementSystem():
    '''
    Class for implementing the ticket management system functionality.
    Attributes:
        tms: The TicketManagementSystem object that provides access to the database and other functionalities.
        db: The Database object used to interact with the database.
        guide: The Guide object used to display a guide on how to use the ticket management system.
    '''
    def __init__(self, database_file):
        '''
        Constructor for the TicketManagementSystem class.
        Args:
            database_file: The file path of the SQLite database.
        '''
        self.tms = self
        self.db = Database(self)
        self.guide = Guide(self)
    def create_new_ticket(self, description, category):
        '''
        Creates a new ticket in the database.
        Args:
            description: A brief description of the issue.
            category: The category of the issue (e.g.: facility management, technical IT, services complaints).
        '''
        self.db.execute_query("INSERT INTO tickets VALUES (NULL, %s, %s, 'open')" % (description, category))
        print("New ticket created with ID number %d." % self.db.cursor.lastrowid)
    def display_tickets(self):
        '''
        Displays a list of all open and active tickets in the database.
        '''
        result = self.db.execute_query("SELECT * FROM tickets WHERE status='open' OR status='active'")
        for row in result:
            print("ID number: %d" % row[0])
            print("Description: %s" % row[1])
            print("Category: %s" % row[2])
            print("Status: %s\n" % row[3])
    def update_ticket(self, id, new_status):
        '''
        Updates the status of a ticket in the database.
        Args:
            id: The unique identifier of the ticket.
            new_status: The new status of the ticket (e.g.: open, active, closed).
        '''
        self.db.execute_query("UPDATE tickets SET status=%s WHERE id=%d" % (new_status, id))
        print("Ticket with ID number %d updated to have status %s." % (id, new_status))