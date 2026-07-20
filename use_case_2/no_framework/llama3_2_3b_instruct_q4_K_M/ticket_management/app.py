from flask import Flask, render_template, request, redirect, url_for
from forms import LoginForm, TicketForm, MessageForm
from database import get_session
from models import User, Ticket, Message

app = Flask(__name__)

@app.route('/')
def index():
    session = get_session()
    tickets = session.query(Ticket).filter_by(status='open').all()
    return render_template('index.html', tickets=tickets)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Logout logic here
    pass

@app.route('/create_ticket', methods=['POST'])
def create_ticket():
    session = get_session()
    ticket = Ticket(title=request.form['title'], description=request.form['description'], category='facility_management')
    session.add(ticket)
    session.commit()
    return redirect(url_for('index'))

@app.route('/ticket/<int:ticket_id>')
def ticket(ticket_id):
    session = get_session()
    ticket = session.query(Ticket).get(ticket_id)
    messages = session.query(Message).filter_by(ticket_id=ticket_id).all()
    return render_template('ticket.html', ticket=ticket, messages=messages)

@app.route('/message/<int:ticket_id>', methods=['POST'])
def message(ticket_id):
    session = get_session()
    message = Message(ticket_id=ticket_id, user_id=request.form['user_id'], content=request.form['content'])
    session.add(message)
    session.commit()
    return redirect(url_for('ticket', ticket_id=ticket_id))

@app.route('/close_ticket/<int:ticket_id>')
def close_ticket(ticket_id):
    session = get_session()
    ticket = session.query(Ticket).get(ticket_id)
    ticket.status = 'closed'
    session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
