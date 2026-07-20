"""
Game class and functions shared across the project.

This file contains the implementation of the Game class and its associated methods.
"""

import logging

# Set default value for logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Ticket:
    """Class representing a ticket."""
    
    def __init__(self, id: int, title: str, description: str, status: str):
        """
        Initialize a new Ticket object.

        Args:
            id (int): Unique identifier for the ticket.
            title (str): Title of the ticket.
            description (str): Description of the ticket.
            status (str): Status of the ticket (e.g., 'open', 'active').
        """
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def update_status(self, new_status: str):
        """
        Update the status of the ticket.

        Args:
            new_status (str): New status for the ticket.
        """
        # Check if new_status is valid
        if not isinstance(new_status, str) or len(new_status) != 10:
            logger.error("Invalid new status")
            return

        self.status = new_status


class HelpdeskStaff:
    """Class representing a helpdesk staff."""
    
    def __init__(self, id: int, name: str):
        """
        Initialize a new HelpdeskStaff object.

        Args:
            id (int): Unique identifier for the staff.
            name (str): Name of the staff.
        """
        self.id = id
        self.name = name

    def update_ticket_status(self, ticket_id: int, new_status: str):
        """
        Update the status of a ticket assigned to this staff.

        Args:
            ticket_id (int): ID of the ticket to update.
            new_status (str): New status for the ticket.
        """
        # Find the ticket with the given id
        ticket = next((t for t in tickets if t.id == ticket_id), None)
        if ticket is None:
            logger.error("Ticket not found")
            return

        # Update the ticket status
        ticket.update_status(new_status)


class Game:
    """Class representing the game."""
    
    def __init__(self):
        """
        Initialize a new Game object.
        """
        self.tickets = []
        self.helpdesk_staffs = []

    def create_ticket(self, title: str, description: str) -> Ticket:
        """
        Create a new ticket.

        Args:
            title (str): Title of the ticket.
            description (str): Description of the ticket.

        Returns:
            Ticket: The newly created ticket.
        """
        # Check if the staff is assigned
        if not self.helpdesk_staffs:
            logger.error("No staff assigned")
            return None

        # Create a new ticket and assign it to the first staff
        ticket = Ticket(0, title, description, 'open')
        self.tickets.append(ticket)
        self.helpdesk_staffs[0].update_ticket_status(ticket.id, 'active')

        return ticket


def main():
    """
    Main function.
    """
    game = Game()

    # Create a new staff
    staff = HelpdeskStaff(1, "John Doe")

    # Create a new ticket
    ticket = game.create_ticket("Test Ticket", "This is a test ticket.")

    # Print the ticket details
    print(f"Ticket ID: {ticket.id}")
    print(f"Title: {ticket.title}")
    print(f"Description: {ticket.description}")
    print(f"Status: {ticket.status}")


if __name__ == "__main__":
    main()
