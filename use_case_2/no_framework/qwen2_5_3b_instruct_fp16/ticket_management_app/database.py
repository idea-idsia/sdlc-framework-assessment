from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True)
    username = db.Column(String(50), unique=True, nullable=False)
    password_hash = db.Column(String(128), nullable=False)

class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(100))
    description = db.Column(String(500))
    category = db.Column(String(50))
    status = db.Column(String(20), default='open')
    opening_date = db.Column(DateTime, nullable=False)
    last_modification_date = db.Column(DateTime)
    closing_date = db.Column(DateTime)

class TicketMessages(db.Model):
    __tablename__ = 'ticket_messages'
    id = db.Column(Integer, primary_key=True)
    ticket_id = db.Column(Integer, ForeignKey('tickets.id'), nullable=False)
    message_content = db.Column(String(500))
    sender_username = db.Column(String(50), nullable=False)
    date_sent = db.Column(DateTime, nullable=False)

def init_db():
    db.create_all()