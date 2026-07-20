from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import timedelta

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    role = Column(Enum('user', 'helpdesk'))

class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    status = Column(Enum('open', 'active', 'closed'))
    category = Column(Enum('facility_management', 'technical_IT', 'services_complaints'))
    created_at = Column(DateTime, default=lambda: datetime.now())
    updated_at = Column(DateTime, default=lambda: datetime.now(), onupdate=lambda: datetime.now())

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, ForeignKey('tickets.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String)

class Category:
    FACILITY_MANAGEMENT = 'facility_management'
    TECHNICAL_IT = 'technical_IT'
    SERVICES_COMPLAINTS = 'services_complaints'

class TicketSchema(metaclass=Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    status = fields.Enum(['open', 'active', 'closed'])
    category = fields.Enum([Category.FACILITY_MANAGEMENT, Category.TECHNICAL_IT, Category.SERVICES_COMPLAINTS])
    created_at = fields.DateTime
    updated_at = fields.DateTime

class MessageSchema(metaclass=Schema):
    id = fields.Int()
    ticket_id = fields.Int()
    user_id = fields.Int()
    content = fields.Str()
