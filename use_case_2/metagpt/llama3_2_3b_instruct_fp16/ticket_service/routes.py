## routes.py
"""
Ticket Management System Routes

This file contains the API endpoints for creating, updating, and retrieving tickets.
"""

from flask import Blueprint, request, jsonify
from models import TicketManager, Ticket, HelpdeskStaff
from forms import TicketForm
import bcrypt

routes = Blueprint('routes', __name__)

# Set default values for database and authentication
TICKET_MANAGER = TicketManager()

def create_ticket(title: str, description: str, status: str) -> int:
    """
    Create a new ticket.

    Args:
        title (str): The title of the ticket.
        description (str): The description of the ticket.
        status (str): The initial status of the ticket.

    Returns:
        int: The ID of the newly created ticket.
    """
    new_ticket = Ticket(len(TICKET_MANAGER.tickets) + 1, title, description, status)
    TICKET_MANAGER.tickets.append(new_ticket)
    return new_ticket.id

@routes.route('/tickets', methods=['POST'])
def create_ticket_view():
    """
    Create a new ticket.

    Request Body:
        title (str): The title of the ticket.
        description (str): The description of the ticket.
        status (str): The initial status of the ticket.

    Returns:
        int: The ID of the newly created ticket.
    """
    form = TicketForm()
    if form.validate_on_submit():
        ticket_id = create_ticket(form.title.data, form.description.data, 'open')
        TICKET_MANAGER.create_ticket(ticket_id, form.title.data, 'open')
        return jsonify({'ticket_id': ticket_id})
    else:
        return jsonify({'error': 'Invalid request'}), 400

@routes.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket_status_view(ticket_id: int):
    """
    Update the status of a ticket.

    Request Body:
        status (str): The new status of the ticket.

    Returns:
        dict: The updated ticket information.
    """
    TICKET_MANAGER.update_ticket_status(ticket_id, request.json['status'])
    return jsonify(TICKET_MANAGER.get_tickets())

@routes.route('/tickets/<int:ticket_id>/assign', methods=['PUT'])
def assign_ticket_to_staff_view(ticket_id: int):
    """
    Assign a ticket to a staff member.

    Request Body:
        staff_id (int): The ID of the staff member.

    Returns:
        dict: The assigned ticket information.
    """
    TICKET_MANAGER.assign_ticket_to_staff(ticket_id, request.json['staff_id'])
    return jsonify(TICKET_MANAGER.get_tickets())

@routes.route('/users/<int:user_id>/tickets', methods=['GET'])
def get_user_tickets_view(user_id: int):
    """
    Get the tickets assigned to a user.

    Request Body:
        user_id (int): The ID of the user.

    Returns:
        list: A list of ticket information.
    """
    return jsonify(TICKET_MANAGER.get_user_tickets(user_id))

if __name__ == '__main__':
    routes.init_app(app)
