from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False, default='open')
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    opening_date = db.Column(db.DateTime, server_default=db.func.now())
    last_modification_date = db.Column(db.DateTime, onupdate=db.func.current_timestamp())
    closing_date = db.Column(db.DateTime)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_type = db.Column(db.String(50), nullable=False)  # 'helpdesk' or 'user'
    created_at = db.Column(db.DateTime, server_default=db.func.now())