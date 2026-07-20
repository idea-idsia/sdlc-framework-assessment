Python
'''
This file contains the HelpDesk class, which is responsible for managing tickets.
It provides methods for inserting and updating tickets.
'''
from database import Database
class HelpDesk:
    def __init__(self, db):
        self.db = db
    def insert_ticket(self, description, status, opening_date, last_modification_date, closing_date, category):
        '''
        Insert a new ticket into the database.
        '''
        from ticket import Ticket
        ticket = Ticket(description, status, opening_date, last_modification_date, closing_date, category)
        self.db.insert_ticket(ticket)
    def change_ticket_status(self, ticket_id, new_status):
        '''
        Change the status of a ticket in the database.
        '''
        self.db.update_ticket(ticket_id, new_status)