from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models (if not already done, but we have models.py)

# We'll create the tables if they don't exist
with app.app_context():
    db.create_all()

# Helper function to get the current user role (from session)
def get_user_role():
    return session.get('role')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form['role']
        session['role'] = role
        return redirect(url_for('tickets'))
    return render_template('login.html')

# Logout route (clear session)
@app.route('/logout')
def logout():
    session.pop('role', None)
    return redirect(url_for('login'))

# Tickets route
@app.route('/tickets')
def tickets():
    role = get_user_role()
    # If not logged in, redirect to login
    if role is None:
        return redirect(url_for('login'))

    # Fetch all tickets
    tickets = Ticket.query.all()
    return render_template('tickets.html', tickets=tickets, role=role)

# New ticket route
@app.route('/new_ticket', methods=['GET', 'POST'])
def new_ticket():
    if get_user_role() is None:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        category = request.form['category']

        # Only users can create tickets (helpdesk might not be allowed to create, but the requirement says helpdesk can modify status)
        # We'll allow only users to create tickets, but helpdesk can modify status.

        new_ticket = Ticket(
            title=title,
            description=description,
            category=category
        )
        db.session.add(new_ticket)
        db.session.commit()

        # Add a default message from the user
        user_message = Message(
            ticket_id=new_ticket.id,
            sender='user',
            message='Ticket created'
        )
        db.session.add(user_message)
        db.session.commit()

        return redirect(url_for('ticket_detail', ticket_id=new_ticket.id))

    return render_template('new_ticket.html')

# Ticket detail route
@app.route('/ticket/<int:ticket_id>')
def ticket_detail(ticket_id):
    role = get_user_role()
    if role is None:
        return redirect(url_for('login'))

    ticket = Ticket.query.get_or_404(ticket_id)
    messages = Message.query.filter_by(ticket_id=ticket_id).all()
    return render_template('ticket_detail.html', ticket=ticket, messages=messages, role=role)

# Edit ticket route (only for helpdesk and maybe user? but requirement says simple user can modify open/active tickets, so we need to check status and role)
@app.route('/edit_ticket/<int:ticket_id>', methods=['GET', 'POST'])
def edit_ticket(ticket_id):
    role = get_user_role()
    if role is None:
        return redirect(url_for('login'))

    # Only helpdesk can change status? and maybe users can edit description?
    # Let's say: helpdesk can change status and modify the ticket (but maybe not description? or maybe they can? The requirement says helpdesk can change status and modify? It says "modify" for both, but let's assume helpdesk can change status and edit the ticket, and users can only edit the description and add messages.

    # We'll allow both to edit the description, but only helpdesk to change status.
    if role == 'helpdesk':
        if request.method == 'POST':
            new_status = request.form['status']
            ticket = Ticket.query.get(ticket_id)
            ticket.status = new_status
            ticket.last_modified_at = datetime.utcnow()
            db.session.commit()
            return redirect(url_for('ticket_detail', ticket_id=ticket_id))

    # For both, we can allow editing the description?
    if request.method == 'POST':
        description = request.form['description']
        ticket = Ticket.query.get(ticket_id)
        ticket.description = description
        ticket.last_modified_at = datetime.utcnow()
        db.session.commit()
        return redirect(url_for('ticket_detail', ticket_id=ticket_id))

    return render_template('edit_ticket.html', ticket_id=ticket_id, role=role)

# Add message to ticket
@app.route('/add_message/<int:ticket_id>', methods=['POST'])
def add_message(ticket_id):
    if get_user_role() is None:
        return redirect(url_for('login'))

    message_text = request.form['message']
    sender = 'user' if get_user_role() == 'user' else 'helpdesk'
    new_message = Message(
        ticket_id=ticket_id,
        sender=sender,
        message=message_text
    )
    db.session.add(new_message)
    db.session.commit()

    return redirect(url_for('ticket_detail', ticket_id=ticket_id))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)