## models.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    
    tickets = relationship("Ticket", back_populates="user")
    messages = relationship("Message", back_populates="ticket")

    def __init__(self, username: str, password_hash: str):
        self.username = username
        self.password_hash = password_hash

    def login(self) -> bool:
        # Placeholder for actual authentication logic
        return True  # Assume successful login for now

    def report_ticket(self, title: str, description: str) -> 'Ticket':
        ticket = Ticket(title=title, description=description)
        ticket.user_id = self.id
        return ticket

    def modify_ticket(self, ticket_id: int, status: str) -> bool:
        # Placeholder for actual logic to update ticket status
        return True  # Assume successful modification for now


class Ticket(Base):
    __tablename__ = 'tickets'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, default='new', nullable=False)

    user = relationship("User", back_populates="tickets")

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

    def update_status(self, status: str) -> bool:
        # Placeholder for actual logic to update ticket status
        self.status = status
        return True  # Assume successful update for now


class Message(Base):
    __tablename__ = 'messages'
    
    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey('tickets.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    content = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    ticket = relationship("Ticket", back_populates="messages")

    def __init__(self, content: str):
        self.content = content

    def send_message(self, ticket_id: int, content: str) -> bool:
        # Placeholder for actual logic to send message
        return True  # Assume successful message sending for now


class Database(Base):
    __tablename__ = 'database'
    
    engine = None
    SessionLocal = None
    
    @classmethod
    def create_tables(cls):
        cls.engine = Base.metadata.create_all(bind=cls.engine)
        
    @classmethod
    def get_db(cls) -> Generator[Session, None, None]:
        db: Optional[Session] = None
        try:
            db = cls.SessionLocal()
            yield db
        finally:
            if db:
                db.close()
