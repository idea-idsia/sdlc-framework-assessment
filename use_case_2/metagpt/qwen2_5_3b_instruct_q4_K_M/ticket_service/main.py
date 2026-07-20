from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
import datetime

app = Flask(__name__)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='open')
    reports = relationship("TicketReport", back_populates="ticket")
    status_changes = relationship("TicketStatusChange", back_populates="ticket")

class TicketReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), nullable=False)
    reporter_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    reported_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    ticket = relationship("Ticket", back_populates="reports")
    reports = relationship("TicketReport", backref=db.backref("reporter", lazy=True))

class HelpdeskStaff(User):
    pass

class TicketStatusChange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), nullable=False)
    status_change = db.Column(db.String(20), default='open')
    change_by_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    change_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    ticket = relationship("Ticket", back_populates="status_changes")

class Analytics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON(), nullable=False, default=dict)

    @staticmethod
    def get_open_tickets_count(data: dict) -> int:
        return len([ticket for ticket in data if ticket['status'] == 'open'])

    @staticmethod
    def get_closed_tickets_count(data: dict) -> int:
        return len([ticket for ticket in data if ticket['status'] == 'closed'])

@login_manager.unauthorized_handler
def unauthorized_callback():
    return jsonify({"message": "Unauthorized access"}), 401

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        login_user(user)
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

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

    status_change_obj = TicketStatusChange(ticket=ticket, status_change=status_change, change_by_user_id=user_id, change_at=change_at)
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

    new_ticket_report = TicketReport(ticket=ticket_id, reporter_user_id=reporter_user_id)
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

    ticket_report = TicketReport.query.filter_by(id=report_id).first()
    if not ticket_report:
        return jsonify({"error": "Ticket report not found"}), 404

    status_change_obj = TicketStatusChange(ticket=ticket_report.ticket, status_change=new_status_change, change_by_user_id=user_id, change_at=change_at)
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

    logout_user()
    return jsonify({"message": "Logout successful"}), 200

class TicketSchema:
    def __init__(self, ticket):
        self.id = ticket.id
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
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'reports': self.reports,
            'status_changes': self.status_changes
        }
