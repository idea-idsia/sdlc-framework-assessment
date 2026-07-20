from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
db = SQLAlchemy(app)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(10), default='open')
    category = db.Column(db.String(20), nullable=False)
    opening_date = db.Column(db.DateTime, default=db.func.now())
    last_modification_date = db.Column(db.DateTime, onupdate=db.func.now(), default=db.func.now())
    closing_date = db.Column(db.DateTime)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)  # 'user' or 'helpdesk'
    content = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, default=db.func.now())

db.create_all()