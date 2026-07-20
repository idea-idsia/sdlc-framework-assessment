'''
Class for managing ticket management user interface.
'''
from .database_manager import DatabaseManager
class TicketManagementUI:
    def __init__(self):
        self.db = DatabaseManager()
    def add_new_ticket(self, category, description):
        self.db.insert_ticket({"category": category, "description": description})
        print("Ticket added successfully.")
    def update_ticket_status(self, id_, new_status):
        self.db.update_ticket_status(id_, new_status)
        print("Ticket status updated successfully.")