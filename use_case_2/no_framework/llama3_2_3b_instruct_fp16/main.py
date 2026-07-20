import sqlite3
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ticket_management.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(15), default='open', nullable=False)
    category = db.Column(db.String(20), nullable=False)
    opened_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_modified_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    closed_at = db.Column(db.DateTime, nullable=True)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401
    login_user(user)
    return jsonify({'message': 'Logged in successfully'})

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'})

@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

@app.route('/tickets', methods=['GET'])
@login_required
def get_tickets():
    if current_user.is_helpdesk:
        tickets = Ticket.query.filter_by(status='open').all()
    else:
        tickets = Ticket.query.filter_by(status='open' | 'active').all()
    return jsonify([{'id': ticket.id, 'title': ticket.title, 'description': ticket.description, 'status': ticket.status, 'category': ticket.category, 'opened_at': ticket.opened_at, 'last_modified_at': ticket.last_modified_at} for ticket in tickets])

@app.route('/tickets/<int:ticket_id>', methods=['GET'])
@login_required
def get_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    return jsonify({'id': ticket.id, 'title': ticket.title, 'description': ticket.description, 'status': ticket.status, 'category': ticket.category, 'opened_at': ticket.opened_at, 'last_modified_at': ticket.last_modified_at})

@app.route('/tickets/<int:ticket_id>/messages', methods=['GET'])
@login_required
def get_messages(ticket_id):
    messages = Message.query.filter_by(ticket_id=ticket_id).all()
    return jsonify([{'id': message.id, 'text': message.text} for message in messages])

@app.route('/tickets/<int:ticket_id>/messages', methods=['POST'])
@login_required
def add_message(ticket_id):
    text = request.json['text']
    new_message = Message(ticket_id=ticket_id, user_id=current_user.id, text=text)
    db.session.add(new_message)
    db.session.commit()
    return jsonify({'message': 'Message added successfully'})

@app.route('/tickets/<int:ticket_id>/close', methods=['POST'])
@login_required
def close_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if current_user.is_helpdesk:
        ticket.status = 'closed'
    else:
        return jsonify({'message': 'You do not have permission to close this ticket'}), 401
    db.session.commit()
    return jsonify({'message': 'Ticket closed successfully'})

class Service1:
    def __init__(self, db):
        self.db = db

    def get_tickets_opened_in_period(self, period):
        tickets = Ticket.query.filter_by(status='open').all()
        opened_in_period = [ticket for ticket in tickets if (datetime.now() - ticket.opened_at).days <= period]
        return len(opened_in_period)

class Service2:
    def __init__(self, db):
        self.db = db

    def get_average_resolution_time(self, month):
        tickets = Ticket.query.filter_by(status='closed').all()
        closed_in_month = [ticket for ticket in tickets if ticket.last_modified_at.month == month]
        resolved_tickets = []
        for ticket in closed_in_month:
            if datetime.now() - ticket.last_modified_at >= 1:
                continue
            resolution_time = (datetime.now() - ticket.last_modified_at).days
            resolved_tickets.append(resolution_time)
        average_resolution_time = sum(resolved_tickets) / len(resolved_tickets)
        return average_resolution_time

class Service3:
    def __init__(self, db):
        self.db = db

    def get_active_tickets_per_category(self):
        tickets = Ticket.query.filter_by(status='active').all()
        categories = {}
        for ticket in tickets:
            category = ticket.category
            if category not in categories:
                categories[category] = 0
            categories[category] += 1
        return categories

services = [Service1(db), Service2(db), Service3(db)]

@app.route('/api/tickets', methods=['GET'])
@login_required
def get_tickets_api():
    tickets = []
    for service in services:
        period = request.json.get('period')
        if period is None:
            continue
        result = getattr(service, f'get_{request.json["service"]}' + str(period))
        tickets.append({'id': ticket.id, 'title': ticket.title, 'description': ticket.description, 'status': ticket.status, 'category': ticket.category, 'opened_at': ticket.opened_at, 'last_modified_at': ticket.last_modified_at})
    return jsonify(tickets)

@app.route('/api/tickets/<int:ticket_id>', methods=['GET'])
@login_required
def get_ticket_api(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    return jsonify({'id': ticket.id, 'title': ticket.title, 'description': ticket.description, 'status': ticket.status, 'category': ticket.category, 'opened_at': ticket.opened_at, 'last_modified_at': ticket.last_modified_at})

@app.route('/api/tickets/<int:ticket_id>/messages', methods=['GET'])
@login_required
def get_messages_api(ticket_id):
    messages = Message.query.filter_by(ticket_id=ticket_id).all()
    return jsonify([{'id': message.id, 'text': message.text} for message in messages])

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)