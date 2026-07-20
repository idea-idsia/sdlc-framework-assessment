"""
Main file for the Ticket Management System.

This file contains the implementation of the main function and the integration with the game module.
"""

import logging
from typing import List
from game import Game  # Import the Game class from the game module

# Set default value for logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TicketManagementSystem:
    """
    Class representing the ticket management system.

    Attributes:
        tickets (List[Ticket]): List of tickets.
        helpdesk_staffs (List[HelpdeskStaff]): List of helpdesk staffs.
    """

    def __init__(self):
        """
        Initialize a new TicketManagementSystem object.
        """
        self.tickets = []  # Initialize an empty list for tickets
        self.helpdesk_staffs = []  # Initialize an empty list for helpdesk staffs

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
        ticket = Game().create_ticket(title, description)  # Use the create_ticket method from the Game class
        self.tickets.append(ticket)
        self.helpdesk_staffs[0].update_ticket_status(ticket.id, 'active')
        self.helpdesk_staffs[0].tickets.append(ticket)  # Assign the ticket to the staff

        return ticket

    def update_ticket_status(self, ticket_id: int, new_status: str):
        """
        Update the status of a ticket.

        Args:
            ticket_id (int): ID of the ticket to update.
            new_status (str): New status for the ticket.
        """
        # Find the ticket with the given id
        ticket = next((t for t in self.tickets if t.id == ticket_id), None)
        if ticket is None:
            logger.error("Ticket not found")
            return

        # Update the ticket status
        ticket.status = new_status  # Directly update the status attribute of the Ticket object

    def get_all_tickets(self) -> List[Ticket]:
        """
        Get all open tickets.

        Returns:
            List[Ticket]: List of open tickets.
        """
        return [ticket for ticket in self.tickets if ticket.status == 'open' or ticket.status == 'active']

    def get_helpdesk_staffs(self) -> List[HelpdeskStaff]:
        """
        Get all helpdesk staffs.

        Returns:
            List[HelpdeskStaff]: List of helpdesk staffs.
        """
        return self.helpdesk_staffs

    def assign_ticket_to_staff(self, ticket_id: int, staff_id: int):
        """
        Assign a ticket to a staff.

        Args:
            ticket_id (int): ID of the ticket to assign.
            staff_id (int): ID of the staff to assign to.
        """
        # Find the ticket with the given id
        ticket = next((t for t in self.tickets if t.id == ticket_id), None)
        if ticket is None:
            logger.error("Ticket not found")
            return

        # Assign the ticket to the staff
        staff = self.helpdesk_staffs[staff_id]
        staff.update_ticket_status(ticket.id, 'active')

def main():
    """
    Main function.
    """
    game = Game()
    ticket_management_system = TicketManagementSystem()

    # Create a new staff
    staff = HelpdeskStaff(1, "John Doe")

    # Create a new ticket
    ticket = ticket_management_system.create_ticket("Test Ticket", "This is a test ticket.")

    # Print the ticket details
    print(f"Ticket ID: {ticket.id}")
    print(f"Title: {ticket.title}")
    print(f"Description: {ticket.description}")
    print(f"Status: {ticket.status}")

if __name__ == "__main__":
    main()
