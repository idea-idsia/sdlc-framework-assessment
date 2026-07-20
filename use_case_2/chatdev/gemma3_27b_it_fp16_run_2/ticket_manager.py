'''
TicketManager class for managing ticket operations.
Handles ticket creation, modification, and status changes.
'''
import datetime
class TicketManager:
    def __init__(self, db_manager):
        """
        Initializes the TicketManager with the database manager.
        """
        self.db_manager = db_manager
    def create_ticket(self, description, category):
        """
        Creates a new ticket in the database.
        """
        opening_date = datetime.datetime.now().isoformat()
        last_modified_date = opening_date
        try:
            ticket_id = self.db_manager.insert_ticket("open", description, category, opening_date, last_modified_date)
            return ticket_id
        except Exception as e:
            print(f"Error creating ticket: {e}")
            return None
    def update_ticket_status(self, ticket_id, status):
        """
        Updates the status of a ticket.
        """
        try:
            self.db_manager.update_ticket_status(ticket_id, status)
        except Exception as e:
            print(f"Error updating ticket status: {e}")
            raise
    def add_message(self, ticket_id, content, sender):
        """
        Adds a message to a ticket.
        """
        timestamp = datetime.datetime.now().isoformat()
        try:
            self.db_manager.insert_message(ticket_id, sender, content, timestamp)
        except Exception as e:
            print(f"Error adding message: {e}")
            raise