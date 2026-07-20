from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True)
    username = db.Column(String(64), unique=True, nullable=False)
    password_hash = db.Column(String(128))

class TicketStatus:
    OPEN = 0
    ACTIVE = 1
    CLOSED = 2

class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(255), nullable=False)
    category_id = Column(ForeignKey('categories.id'), index=True, nullable=False)
    user_id = Column(ForeignKey('users.id'))
    status = Column(Integer, default=TicketStatus.OPEN)
    opening_date = Column(Date, default=date.today())
    last_modified_date = Column(Date, onupdate=date.today(), server_default="CURRENT_TIMESTAMP")
    closing_date = Column(Date)

    category = relationship("Category", back_populates="tickets")
    user = relationship("User", backref=db.backref('tickets', lazy='dynamic'))

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)

    tickets = relationship("Ticket", back_populates="category")