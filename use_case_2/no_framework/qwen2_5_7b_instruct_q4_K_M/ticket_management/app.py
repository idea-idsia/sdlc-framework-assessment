from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
from models import db, Ticket, Message
from services.data_visualization import Service1, Service2, Service3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
db.init_app(app)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    # Placeholder for logged-in user type
    user_type = request.args.get('user_type', 'user')

    if user_type == 'helpdesk':
        tickets = Ticket.query.filter_by(status='active').all()
    else:
        open_tickets = Ticket.query.filter_by(status='open').all()
        active_tickets = Ticket.query.filter_by(status='active').all()

        return render_template('ticket_list.html', open_tickets=open_tickets, active_tickets=active_tickets)


@app.route('/create_ticket', methods=['GET', 'POST'])
def create_ticket():
    if request.method == 'POST':
        category = request.form['category']
        description = request.form['description']
        ticket = Ticket(category=category, description=description)
        db.session.add(ticket)
        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('create_ticket.html')


@app.route('/ticket/<int:ticket_id>', methods=['GET', 'POST'])
def ticket_detail(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    if request.method == 'POST':
        status = request.form['status']
        ticket.status = status
        db.session.commit()

    messages = Message.query.filter_by(ticket_id=ticket_id).all()

    return render_template('ticket_detail.html', ticket=ticket, messages=messages)


@app.route('/message/<int:ticket_id>', methods=['POST'])
def message(ticket_id):
    content = request.form['content']
    user_type = 'helpdesk'  # Placeholder for logged-in user type
    message = Message(content=content, ticket_id=ticket_id, user_type=user_type)
    db.session.add(message)
    db.session.commit()

    return redirect(url_for('ticket_detail', ticket_id=ticket_id))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)