## models.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class TicketModel(Base):
    __tablename__ = 'tickets'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    description = Column(String(1024), nullable=False)
    status = Column(String(32), default='open')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    comments = relationship("Comment", back_populates="ticket")

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, ForeignKey('tickets.id'))
    content = Column(String(1024), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    ticket = relationship("TicketModel", back_populates="comments")

    def __init__(self, content: str):
        self.content = content
