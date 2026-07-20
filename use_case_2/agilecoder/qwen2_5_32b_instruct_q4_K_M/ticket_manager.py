'''
Handles ticket creation, viewing, and modification.
Interfaces with the database to perform CRUD operations.
'''
import database_handler
class TicketManager:
    def __init__(self, db):
        self.db = db
    def create_ticket(self, description, category):
        try:
            self.db.insert_ticket(description, category)
            return True
        except Exception as e:
            raise ValueError(str(e))
    def modify_ticket(self, ticket_id, description=None, category=None):
        try:
            if not description and not category:
                raise ValueError("At least one field must be provided for modification.")
            self.db.update_ticket(ticket_id, description=description or None, category=category or None)
            return True
        except Exception as e:
            raise ValueError(str(e))
    def view_messages(self, ticket_id):
        try:
            messages = self.db.get_messages(ticket_id)
            if not messages:
                raise ValueError("No messages found for this ticket.")
            return messages
        except Exception as e:
            raise ValueError(str(e))