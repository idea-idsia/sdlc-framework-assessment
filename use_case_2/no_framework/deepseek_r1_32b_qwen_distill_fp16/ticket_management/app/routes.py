from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Ticket, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('login.html')

@main.route('/dashboard')
def dashboard():
    # Get all open tickets for simple users or all for helpdesk
    if current_user.role == 'helpdesk':
        tickets = Ticket.query.all()
    else:
        tickets = Ticket.query.filter_by(status='open').all()
    return render_template('dashboard.html', tickets=tickets)

@main.route('/ticket/<int:ticket_id>', methods=['GET', 'POST'])
def ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    if request.method == 'POST':
        # Update ticket or add message
        pass  # Implement logic based on user role
    return render_template('ticket.html', ticket=ticket)

@main.route('/new_ticket', methods=['GET', 'POST'])
def new_ticket():
    if request.method == 'POST':
        # Create new ticket
        description = request.form['description']
        category = determine_category(description)
        new_ticket = Ticket(
            user_id=current_user.id,
            description=description,
            category=category
        )
        db.session.add(new_ticket)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('new_ticket.html')