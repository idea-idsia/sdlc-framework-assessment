from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from models import Ticket, Message

ticket_management = Blueprint('ticket_management', __name__)

@ticket_management.route('/tickets/helpdesk')
def helpdesk_view():
    tickets = Ticket.query.all()
    return render_template('helpdesk_tickets.html', tickets=tickets)

@ticket_management.route('/tickets/simpleuser')
def simple_user_view():
    # Implement logic to show only open and active tickets for simple users
    pass

@ticket_management.route('/ticket/new', methods=['GET', 'POST'])
def new_ticket():
    if request.method == 'POST':
        # Create a new ticket with default status as 'open'
        ticket = Ticket(status='open', description=request.form['description'], category=request.form['category'])
        db.session.add(ticket)
        db.session.commit()
        return redirect(url_for('ticket_management.simple_user_view'))
    return render_template('new_ticket.html')

# Implement other routes for modifying tickets, viewing messages, and posting new messages