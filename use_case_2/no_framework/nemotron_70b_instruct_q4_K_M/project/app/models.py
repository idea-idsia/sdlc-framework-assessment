from app import db

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), nullable=False, default='open')
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    # Relationship with Message model
    messages = db.relationship('Message', backref='ticket', lazy=True)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), nullable=False)