from sqlalchemy import Column, Integer, String, DateTime, Text, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(Enum('facility', 'it', 'services'), nullable=False)
    status = Column(Enum('open', 'active', 'closed'), default='open')
    # ... other columns ...


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, ForeignKey('tickets.id'))
    content = Column(Text, nullable=False)
    sender_type = Column(Enum('user', 'helpdesk'), nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)