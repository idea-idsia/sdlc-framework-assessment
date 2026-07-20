"""
User interface for managing tickets.
"""
from db_manager import DatabaseManager
class TicketManagementUI:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
    def add_new_ticket(self):
        category = input("Enter ticket category: ")
        description = input("Enter ticket description: ")
        new_ticket = {"category": category, "description": description}
        self.db_manager.insert_ticket(new_ticket)
        print("Ticket added successfully.")
    def update_status_of_ticket(self):
        open_tickets = self.db_manager.get_open_tickets()
        for i, ticket in enumerate(open_tickets):
            print(f"{i + 1}. ID: {ticket[0]}, Category: {ticket[2]}, Description: {ticket[3]}, Status: {ticket[4]}")
        choice = int(input("Enter the number of the ticket to update (0 to exit): ")) - 1
        if choice == -1:
            return
        new_status = input("Enter the new status (resolved/closed): ")
        self.db_manager.update_ticket_status(open_tickets[choice][0], new_status)
        print("Ticket status updated successfully.")