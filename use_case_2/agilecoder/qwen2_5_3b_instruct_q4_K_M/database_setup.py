# database_setup.py
'''
Define the database schema and implement CRUD operations for Ticket, User, and Category tables.
'''
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
engine = create_engine('sqlite:///ticket_management.db', echo=True)
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
class Ticket(Base):
    __tablename__ = 'ticket'
    id = Column(Integer, primary_key=True)
    status = Column(String(20))
    description = Column(String(500))
    category_id = Column(Integer, ForeignKey('category.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="tickets")
    category = relationship("Category", back_populates="tickets")
class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    tickets = relationship("Ticket", back_populates="category")
# Create tables
def create_tables():
    Base.metadata.create_all(engine)
# Add a user (for testing purposes)
@sessionmaker(bind=engine).options(no_cache=True)(scope_closure=None)()
def add_user(session):
    session.add(User(username='simple_user'))
    session.commit()
# Function to fetch all tickets for debugging purposes
def read_tickets():
    with engine.connect() as connection:
        result = connection.execute(Ticket.__table__.select())
        return [dict(row) for row in result]