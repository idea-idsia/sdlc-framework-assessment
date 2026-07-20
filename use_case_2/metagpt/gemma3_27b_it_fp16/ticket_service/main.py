"""
This file contains the main application logic for the ticket management system.
It includes the Ticket class and functions for creating, updating, and deleting tickets.
"""
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Ticket:
    """
    Represents a ticket in the ticket management system.
    """

    def __init__(self, ticket_id: int, title: str, description: str, status: str = "open",
                 created_at: datetime.datetime = datetime.datetime.now(),
                 updated_at: datetime.datetime = datetime.datetime.now()):
        """
        Initializes a new Ticket object.

        Args:
            ticket_id (int): The unique identifier for the ticket.
            title (str): The title of the ticket.
            description (str): A detailed description of the ticket.
            status (str, optional): The current status of the ticket. Defaults to "open".
            created_at (datetime, optional): The date and time the ticket was created. Defaults to now.
            updated_at (datetime, optional): The date and time the ticket was last updated. Defaults to now.
        """
        self.ticket_id: int = ticket_id
        self.title: str = title
        self.description: str = description
        self.status: str = status
        self.created_at: datetime.datetime = created_at
        self.updated_at: datetime.datetime = updated_at

    def update_status(self, new_status: str):
        """
        Updates the status of the ticket.

        Args:
            new_status (str): The new status of the ticket.
        """
        self.status = new_status
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Returns a string representation of the Ticket object.
        """
        return f"Ticket ID: {self.ticket_id}, Title: {self.title}, Status: {self.status}"


class TicketManagementSystem:
    """
    Manages a collection of tickets.
    """

    def __init__(self):
        """
        Initializes a new TicketManagementSystem object.
        """
        self.tickets: dict[int, Ticket] = {}  # Use a dictionary to store tickets by ID
        self.next_ticket_id: int = 1

    def create_ticket(self, title: str, description: str) -> Ticket:
        """
        Creates a new ticket and adds it to the system.

        Args:
            title (str): The title of the ticket.
            description (str): A detailed description of the ticket.

        Returns:
            Ticket: The newly created ticket.
        """
        ticket_id: int = self.next_ticket_id
        new_ticket: Ticket = Ticket(ticket_id, title, description)
        self.tickets[ticket_id] = new_ticket
        self.next_ticket_id += 1
        logging.info(f"Created ticket with ID: {ticket_id}")
        return new_ticket

    def get_ticket(self, ticket_id: int) -> Ticket | None:
        """
        Retrieves a ticket by its ID.

        Args:
            ticket_id (int): The ID of the ticket to retrieve.

        Returns:
            Ticket | None: The ticket with the specified ID, or None if no such ticket exists.
        """
        if ticket_id in self.tickets:
            return self.tickets[ticket_id]
        else:
            logging.warning(f"Ticket with ID: {ticket_id} not found.")
            return None

    def update_ticket_status(self, ticket_id: int, new_status: str):
        """
        Updates the status of a ticket.

        Args:
            ticket_id (int): The ID of the ticket to update.
            new_status (str): The new status of the ticket.
        """
        ticket: Ticket | None = self.get_ticket(ticket_id)
        if ticket:
            ticket.update_status(new_status)
            logging.info(f"Updated status of ticket with ID: {ticket_id} to {new_status}")
        else:
            logging.warning(f"Ticket with ID: {ticket_id} not found.")

    def delete_ticket(self, ticket_id: int):
        """
        Deletes a ticket from the system.

        Args:
            ticket_id (int): The ID of the ticket to delete.
        """
        if ticket_id in self.tickets:
            del self.tickets[ticket_id]
            logging.info(f"Deleted ticket with ID: {ticket_id}")
        else:
            logging.warning(f"Ticket with ID: {ticket_id} not found.")

    def list_tickets(self) -> list[Ticket]:
        """
        Lists all tickets in the system.

        Returns:
            list[Ticket]: A list of all tickets in the system.
        """
        return list(self.tickets.values())


if __name__ == "__main__":
    # Example Usage
    ticket_system: TicketManagementSystem = TicketManagementSystem()

    # Create some tickets
    ticket1: Ticket = ticket_system.create_ticket("Bug Report", "The application crashes when...")
    ticket2: Ticket = ticket_system.create_ticket("Feature Request", "Add a dark mode option.")

    # List all tickets
    print("All Tickets:")
    for ticket in ticket_system.list_tickets():
        print(ticket)

    # Update the status of a ticket
    ticket_system.update_ticket_status(1, "in progress")

    # List all tickets again
    print("\nTickets After Update:")
    for ticket in ticket_system.list_tickets():
        print(ticket)

    # Delete a ticket
    ticket_system.delete_ticket(2)

    # List all tickets one last time
    print("\nTickets After Deletion:")
    for ticket in ticket_system.list_tickets():
        print(ticket)
