from flask import jsonify, request
from models import Ticket, User, HelpDeskStaff, TicketManager, db

def report_issue(title: str, description: str, user_id: int) -> dict:
    """
    Reports a new issue.
    
    Args:
        title (str): The title of the issue.
        description (str): The description of the issue.
        user_id (int): The ID of the user reporting the issue.
    
    Returns:
        dict: A dictionary containing the result of the operation.
    """
    # Validate user
    user = User.query.get(user_id)
    if not user:
        return {'error': 'User not found'}, 404
    
    try:
        # Create a new ticket using TicketManager
        ticket_manager = TicketManager(db.session)
        ticket = Ticket(title=title, description=description, status="open")
        db.session.add(ticket)
        db.session.commit()
        
        # Assign the ticket to the user (assuming relationship is defined in models)
        user.tickets.append(ticket)
        db.session.commit()
        
        return {'message': 'Issue reported successfully'}, 201
    except Exception as e:
        db.session.rollback()  # Roll back the session in case of an error
        return {'error': str(e)}, 500


def view_tickets() -> dict:
    """
    Views all tickets.
    
    Returns:
        dict: A dictionary containing the list of tickets.
    """
    try:
        # Retrieve all tickets using TicketManager
        ticket_manager = TicketManager(db.session)
        tickets = ticket_manager.db_session.query(Ticket).all()
        
        # Serialize the tickets
        serialized_tickets = []
        for ticket in tickets:
            serialized_ticket = {
                'id': ticket.id,
                'title': ticket.title,
                'description': ticket.description,
                'status': ticket.status
            }
            serialized_tickets.append(serialized_ticket)
        
        return {'tickets': serialized_tickets}, 200
    except Exception as e:
        return {'error': str(e)}, 500


def exchange_messages(ticket_id: int, message: str) -> dict:
    """
    Exchanges messages for a ticket.
    
    Args:
        ticket_id (int): The ID of the ticket.
        message (str): The message to be exchanged.
    
    Returns:
        dict: A dictionary containing the result of the operation.
    """
    # Validate ticket
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        return {'error': 'Ticket not found'}, 404
    
    # Check for empty or None message
    if not message:
        return {'error': 'Message cannot be empty'}, 400
    
    try:
        # Exchange messages using TicketManager
        ticket_manager = TicketManager(db.session)
        ticket_manager.exchange_messages(ticket_id, message)
        
        return {'message': 'Messages exchanged successfully'}, 200
    except Exception as e:
        db.session.rollback()  # Roll back the session in case of an error
        return {'error': str(e)}, 500


def update_status(ticket_id: int, status: str) -> dict:
    """
    Updates the status of a ticket.
    
    Args:
        ticket_id (int): The ID of the ticket.
        status (str): The new status of the ticket.
    
    Returns:
        dict: A dictionary containing the result of the operation.
    """
    # Validate ticket
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        return {'error': 'Ticket not found'}, 404
    
    try:
        # Update status using TicketManager
        ticket_manager = TicketManager(db.session)
        ticket_manager.assign_status(ticket_id, status)
        
        return {'message': 'Status updated successfully'}, 200
    except Exception as e:
        db.session.rollback()  # Roll back the session in case of an error
        return {'error': str(e)}, 500


def analyze_data() -> dict:
    """
    Analyzes data related to tickets.
    
    Returns:
        dict: A dictionary containing the analysis results.
    """
    try:
        # Retrieve all tickets using TicketManager
        ticket_manager = TicketManager(db.session)
        tickets = ticket_manager.db_session.query(Ticket).all()
        
        # Example analysis: counting tickets by status
        status_counts = {}
        for ticket in tickets:
            if ticket.status not in status_counts:
                status_counts[ticket.status] = 1
            else:
                status_counts[ticket.status] += 1
        
        return {'analysis': status_counts}, 200
    except Exception as e:
        return {'error': str(e)}, 500

