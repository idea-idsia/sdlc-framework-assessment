from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10), nullable=False, default='open')
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(20), nullable=False) # Facility, IT, Services
    opening_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    last_modification = db.Column(db.DateTime, onupdate=db.func.current_timestamp())
    closing_date = db.Column(db.DateTime)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), nullable=False)
    ticket = db.relationship('Ticket', backref=db.backref('messages', lazy=True))
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())