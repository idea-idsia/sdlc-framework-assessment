## app.py

from flask import Flask, request, jsonify, current_user
from datetime import datetime
import json

app = Flask(__name__)

# Data structures and interfaces
class User:
    def __init__(self, id=None):
        self.id = id

class Ticket:
    def __init__(self, user_id=None, title=None, description=None, status='open'):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.status = status
        self.reports = []
        self.status_changes = []

class Report:
    def __init__(self, reporter_user_id=None, ticket_id=None, reported_at=datetime.utcnow()):
        self.reporter_user_id = reporter_user_id
        self.ticket_id = ticket_id
        self.reported_at = reported_at

class StatusChange:
    def __init__(self, change_by_user_id=None, change_at=datetime.utcnow(), status_change='open'):
        self.change_by_user_id = change_by_user_id
        self.change_at = change_at
        self.status_change = status_change

# Data models
class UserSchema:
    def __init__(self, user):
        self.id = user.id if user else None

class TicketSchema:
    def __init__(self, ticket):
        self.user_id = ticket.user_id
        self.title = ticket.title
        self.description = ticket.description
        self.status = ticket.status
        self.reports = [report.serialize() for report in ticket.reports]
        self.status_changes = [change.serialize() for change in ticket.status_changes]

    @staticmethod
    def serialize(ticket):
        return TicketSchema(ticket).serialize()

    def serialize(self):
        return {
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'reports': self.reports,
            'status_changes': self.status_changes
        }

class Analytics:
    def __init__(self, data=None):
        if data is None:
            self.data = {}
        else:
            self.data = data

    @staticmethod
    def get_open_tickets_count(data: dict) -> int:
        return len([ticket for ticket in data if ticket['status'] == 'open'])

    @staticmethod
    def get_closed_tickets_count(data: dict) -> int:
        return len([ticket for ticket in data if ticket['status'] == 'closed'])

# Routes
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    current_user.id = user.id
    return jsonify({"message": "Login successful"}), 200

@app.route('/create_ticket', methods=['POST'])
def create_ticket():
    data = request.json
    user_id = data.get('user_id')
    title = data.get('title')
    description = data.get('description')

    if not user_id or not title or not description:
        return jsonify({"error": "Missing required fields"}), 400

    new_ticket = Ticket(user_id=user_id, title=title, description=description)
    db.session.add(new_ticket)
    db.session.commit()

    return jsonify({"message": "Ticket created successfully", "ticket_id": new_ticket.id}), 201

@app.route('/get_open_tickets', methods=['GET'])
def get_open_tickets():
    if not current_user.is_authenticated:
        return jsonify({"error": "Unauthorized access"}), 401

    open_tickets = Ticket.query.filter_by(status='open').all()
    return jsonify([ticket.serialize() for ticket in open_tickets]), 200

@app.route('/get_closed_tickets', methods=['GET'])
def get_closed_tickets():
    if not current_user.is_authenticated:
        return jsonify({"error": "Unauthorized access"}), 401

    closed_tickets = Ticket.query.filter_by(status='closed').all()
    return jsonify([ticket.serialize() for ticket in closed_tickets]), 200

@app.route('/update_ticket', methods=['PUT'])
def update_ticket():
    data = request.json
    ticket_id = data.get('ticket_id')
    new_description = data.get('new_description')

    if not ticket_id or not new_description:
        return jsonify({"error": "Missing required fields"}), 400

    ticket = Ticket.query.filter_by(id=ticket_id).first()
    if not ticket:
        return jsonify({"error": "Ticket not found"}), 404

    ticket.description = new_description
    db.session.commit()

    return jsonify({"message": "Ticket updated successfully", "ticket_id": ticket.id}), 200

@app.route('/change_status', methods=['PUT'])
def change_status():
    data = request.json
    ticket_id = data.get('ticket_id')
    status_change = data.get('status_change')
    user_id = data.get('user_id')
    change_at = data.get('change_at')

    if not ticket_id or not status_change or (not user_id and not change_at):
        return jsonify({"error": "Missing required fields"}), 400

    ticket = Ticket.query.filter_by(id=ticket_id).first()
    if not ticket:
        return jsonify({"error": "Ticket not found"}), 404

    status_change_obj = StatusChange(ticket=ticket, status_change=status_change, change_by_user_id=user_id, change_at=change_at)
    db.session.add(status_change_obj)
    db.session.commit()

    return jsonify({"message": "Status change successful", "ticket_id": ticket.id}), 200

@app.route('/create_report', methods=['POST'])
def create_report():
    data = request.json
    ticket_id = data.get('ticket_id')
    reporter_user_id = data.get('reporter_user_id')

    if not ticket_id or not reporter_user_id:
        return jsonify({"error": "Missing required fields"}), 400

    new_ticket_report = Report(reporter_user_id=reporter_user_id, ticket_id=ticket_id)
    db.session.add(new_ticket_report)
    db.session.commit()

    return jsonify({"message": "Report created successfully", "report_id": new_ticket_report.id}), 201

@app.route('/update_status_change', methods=['PUT'])
def update_status_change():
    data = request.json
    report_id = data.get('report_id')
    new_status_change = data.get('new_status_change')
    user_id = data.get('user_id')
    change_at = data.get('change_at')

    if not report_id or not new_status_change:
        return jsonify({"error": "Missing required fields"}), 400

    ticket_report = Report.query.filter_by(id=report_id).first()
    if not ticket_report:
        return jsonify({"error": "Ticket report not found"}), 404

    status_change_obj = StatusChange(ticket=ticket_report.ticket, status_change=new_status_change, change_by_user_id=user_id, change_at=change_at)
    db.session.add(status_change_obj)
    db.session.commit()

    return jsonify({"message": "Status change updated successfully", "report_id": ticket_report.id}), 200

@app.route('/get_open_tickets_count', methods=['GET'])
def get_open_tickets_count():
    if not current_user.is_authenticated:
        return jsonify({"error": "Unauthorized access"}), 401

    data = Analytics().data
    open_ticket_count = Analytics.get_open_tickets_count(data)
    closed_ticket_count = Analytics.get_closed_tickets_count(data)

    return jsonify({
        'open_tickets_count': open_ticket_count,
        'closed_tickets_count': closed_ticket_count
    }), 200

@app.route('/get_closed_tickets_count', methods=['GET'])
def get_closed_tickets_count():
    if not current_user.is_authenticated:
        return jsonify({"error": "Unauthorized access"}), 401

    data = Analytics().data
    open_ticket_count = Analytics.get_open_tickets_count(data)
    closed_ticket_count = Analytics.get_closed_tickets_count(data)

    return jsonify({
        'open_tickets_count': open_ticket_count,
        'closed_tickets_count': closed_ticket_count
    }), 200

@app.route('/logout', methods=['POST'])
def logout():
    if not current_user.is_authenticated:
        return jsonify({"error": "Unauthorized access"}), 401

    db.session.remove()
    db.session.close()
    current_user.id = None
    return jsonify({"message": "Logout successful"}), 200

# User authentication and authorization logic
@login_manager.unauthorized_handler
def unauthorized_callback():
    return jsonify({"error": "Unauthorized access"}), 401

if __name__ == '__main__':
    app.run(debug=True)
