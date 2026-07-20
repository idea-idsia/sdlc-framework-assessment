'''
Main entry point of the application.
'''
from user import User
from database_manager import DatabaseManager
from microservices import MicroserviceManager
def main():
    # Initialize the database manager
    db_manager = DatabaseManager()
    db_manager.create_tickets_table()
    db_manager.create_messages_table()
    # Create users
    user1 = User("Alice", "helpdesk")
    user2 = User("Bob", "simple_user")
    # Example of creating and modifying tickets
    ticket_id = 1
    title = "Issue with login"
    description = "Unable to login after resetting password"
    category = "auth"
    if user1.create_ticket(db_manager, title, description, category):
        print(f"Ticket {ticket_id} created successfully by helpdesk user")
    # Change ticket status
    user1.change_ticket_status(db_manager, ticket_id, 'active')
    # Adding messages to a ticket
    message_content = "Please check the server logs for more details."
    if user2.add_message(db_manager, ticket_id, message_content):
        print(f"Message added to ticket {ticket_id}")
    # Viewing messages of a ticket
    messages = user1.get_messages(db_manager, ticket_id)
    for msg in messages:
        print(msg)
    # Close connections
    db_manager.close_connection()
if __name__ == "__main__":
    main()