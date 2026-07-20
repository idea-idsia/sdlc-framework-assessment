# Import necessary libraries
from db_manager import DBManager
from ticket import Ticket
'''
Ticket manager class.
It provides methods for creating and retrieving tickets.
'''
class TicketManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    def create_ticket(self, description, category):
        ticket = Ticket(description, category)
        # Insert ticket into database
        self.db_manager.insert_ticket(ticket)
        return ticket
    def get_tickets(self):
        query = "SELECT * FROM tickets"
        return self.db_manager.execute_query(query, ())