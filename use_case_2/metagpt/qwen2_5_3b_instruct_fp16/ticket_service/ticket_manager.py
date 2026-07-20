from datetime import datetime
import bcrypt

class Ticket:
    def __init__(self):
        self.id = None
        self.title = ""
        self.description = ""
        self.status = "open"
        self.created_at = datetime.now()
        self.modified_at = datetime.now()
        self.reporter_id = 0
        self.assignee_id = 0

class TicketManager:
    def __init__(self):
        self.tickets = []

    @staticmethod
    def create_ticket(title, description, reporter_id):
        ticket = Ticket()
        ticket.title = title
        ticket.description = description
        ticket.reporter_id = reporter_id
        ticket.status = "active"
        ticket.created_at = datetime.now()
        ticket.modified_at = datetime.now()
        
        # Add the new ticket to the list of tickets
        ticket.id = len(self.tickets) + 1
        self.tickets.append(ticket)
        
        return ticket

    def update_ticket_status(self, ticket_id, new_status):
        for ticket in self.tickets:
            if ticket.id == ticket_id:
                ticket.status = new_status
                ticket.modified_at = datetime.now()
                return True
        
        # Ticket not found
        return False

class Message:
    def __init__(self):
        self.id = None
        self.ticket_id = 0
        self.sender_id = 0
        self.receiver_id = 0
        self.content = ""
        self.timestamp = datetime.now()

class MessageHandler:
    @staticmethod
    def send_message(content, receiver_id):
        message = Message()
        message.content = content
        message.sender_id = 1  # Assuming the sender is always user with id 1
        message.receiver_id = receiver_id
        message.timestamp = datetime.now()
        
        return True

class DataVisualization:
    def __init__(self):
        self.tickets_data = {}
        self.users_data = {}
        self.metrics = {}

    @staticmethod
    def fetch_tickets():
        tickets = [ticket.__dict__ for ticket in TicketManager().tickets]
        return tickets

    @staticmethod
    def fetch_users():
        users = []
        # Assuming we have a function to get all registered users, this is just a placeholder.
        user_list = [{"id": 1, "username": "admin"}, {"id": 2, "username": "user1"}]
        for user in user_list:
            users.append(user)
        
        return users

    @staticmethod
    def generate_report():
        report = {
            'tickets': DataVisualization.fetch_tickets(),
            'users': DataVisualization.fetch_users()
        }
        # Placeholder for actual data visualization logic.
        return "Generated Report"

# Example usage of TicketManager, MessageHandler, and DataVisualization classes
if __name__ == "__main__":
    ticket_manager = TicketManager()
    
    # Create a new ticket
    ticket_id = ticket_manager.create_ticket("Bug in login page", "Cannot log in with correct credentials.", 1)
    print(f"Created ticket {ticket_id}")
    
    # Update the status of the ticket
    if ticket_manager.update_ticket_status(ticket_id, "closed"):
        print(f"Ticket {ticket_id} updated to closed.")
    else:
        print("Failed to update ticket status.")
    
    # Send a message related to the ticket
    if MessageHandler.send_message("Please investigate this issue.", ticket_id):
        print("Message sent successfully.")
    else:
        print("Failed to send message.")
    
    # Fetch tickets for data visualization
    tickets = DataVisualization.fetch_tickets()
    print(tickets)
    
    # Generate a report and display it
    report = DataVisualization.generate_report()
    print(report)

