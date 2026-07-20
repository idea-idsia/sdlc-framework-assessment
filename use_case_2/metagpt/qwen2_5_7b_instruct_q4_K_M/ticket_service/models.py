## models.py

from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import bcrypt

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    tickets = relationship("Ticket", back_populates="user")

    def __init__(self, username: str, password_hash: str):
        self.username = username
        self.password_hash = password_hash

    def login(self) -> bool:
        # Placeholder for actual authentication logic
        return True  # Assume successful login for now

    def report_issue(self, issue: str) -> 'Ticket':
        from .microservices_api import MicroservicesAPI
        db_session = MicroservicesAPI.get_db_session()
        ticket = db_session.create_ticket(user_id=self.id, issue=issue)
        db_session.commit()
        return ticket

    def modify_ticket(self, ticket_id: int, status: str) -> bool:
        from .microservices_api import MicroservicesAPI
        db_session = MicroservicesAPI.get_db_session()
        success = db_session.update_ticket(ticket_id=ticket_id, status=status)
        db_session.commit()
        return success

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    issue = Column(String, nullable=False)
    status = Column(String, default='new')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="tickets")

    def update_status(self, status: str) -> bool:
        self.status = status
        return True  # Assume successful update for now

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, ForeignKey('tickets.id'), nullable=False)
    sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    ticket = relationship("Ticket", back_populates="messages")
    sender = relationship("User")

class HelpdeskStaff(User):
    __tablename__ = 'helpdesk_staff'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def view_tickets(self, status: str) -> list['Ticket']:
        from .microservices_api import MicroservicesAPI
        db_session = MicroservicesAPI.get_db_session()
        tickets = db_session.view_tickets(status=status)
        return tickets

    def change_ticket_status(self, ticket_id: int, new_status: str) -> bool:
        from .microservices_api import MicroservicesAPI
        db_session = MicroservicesAPI.get_db_session()
        success = db_session.change_ticket_status(ticket_id=ticket_id, new_status=new_status)
        db_session.commit()
        return success

class DatabaseAPI(Base):
    __tablename__ = 'database_api'

    id = Column(Integer, primary_key=True)

    def create_user(self, username: str, password_hash: str) -> User:
        user = User(username=username, password_hash=password_hash)
        return user

    def get_user_by_username(self, username: str) -> 'User':
        # Placeholder for actual query logic
        return None  # Assume no user found for now

    def create_ticket(self, user_id: int, issue: str) -> Ticket:
        ticket = Ticket(user_id=user_id, issue=issue)
        return ticket

    def update_ticket(self, ticket_id: int, status: str) -> bool:
        # Placeholder for actual update logic
        return True  # Assume successful update for now

    def create_message(self, ticket_id: int, sender: User, content: str) -> Message:
        message = Message(ticket_id=ticket_id, sender=sender, content=content)
        return message

class MicroservicesAPI(Base):
    __tablename__ = 'microservices_api'

    id = Column(Integer, primary_key=True)

    def __init__(self, db_api: DatabaseAPI):
        self.db_api = db_api

    def report_issue(self, username: str, issue: str) -> Ticket:
        user = self.db_api.get_user_by_username(username)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user.report_issue(issue)

    def modify_ticket(self, username: str, ticket_id: int, status: str) -> bool:
        user = self.db_api.get_user_by_username(username)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user.modify_ticket(ticket_id=ticket_id, status=status)

    def view_tickets(self, status: str) -> list['Ticket']:
        # Placeholder for actual query logic
        return []  # Assume no tickets found for now

    def change_ticket_status(self, ticket_id: int, new_status: str) -> bool:
        # Placeholder for actual update logic
        return True  # Assume successful update for now
