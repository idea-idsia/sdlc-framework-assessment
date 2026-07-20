## main.py

from auth import User  # Import the User class from auth.py
from ticket_manager import TicketManager  # Import the TicketManager class from ticket_manager.py
from message_handler import MessageHandler  # Import the MessageHandler class from message_handler.py
from data_visualizer import DataVisualization  # Import the DataVisualization class from data_visualizer.py

import datetime  # Import the datetime module for handling dates and times
import json  # Import the JSON module for working with JSON data

# Initialize instances of the classes
user = User()
ticket_manager = TicketManager()
message_handler = MessageHandler()
data_visualizer = DataVisualization()

def main():
    """
    Main function to demonstrate the functionality of the ticket management system.
    """
    
    # Example user authentication and login
    login_status, message = user.login("admin", "password123")
    print(f"Login status: {login_status}, Message: {message}")
    
    if login_status:
        # Example ticket creation and update
        ticket_id = ticket_manager.create_ticket("Bug in login page", "Cannot log in with correct credentials.", 1)
        print(f"Created ticket {ticket_id}")
        
        # Update the status of the created ticket
        updated_status = ticket_manager.update_ticket_status(ticket_id, "closed")
        if updated_status:
            print(f"Ticket {ticket_id} updated to closed.")
        else:
            print("Failed to update ticket status.")
    
    # Example sending and receiving messages related to a ticket
    message_handler.send_message("Please investigate this issue.", ticket_id)
    received_messages = message_handler.receive_messages(ticket_id)
    for message in received_messages:
        print(f"Received message: {message}")
    
    # Data visualization of tickets and users
    data_visualizer.fetch_tickets()
    data_visualizer.fetch_users()
    report = data_visualizer.generate_report()
    with open('data_visualization_report.json', 'w') as file:
        json.dump(report, file, indent=4)
    print("Report generated successfully.")

if __name__ == "__main__":
    main()

# Example usage of user authentication methods
if __name__ == "__main__":
    login_status, message = User.login("admin", "password123")
    print(message)

    register_status, message = User.register("newuser", "securepassword", "newuser@example.com")
    print(message)
