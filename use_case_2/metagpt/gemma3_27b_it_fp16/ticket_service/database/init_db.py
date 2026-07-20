"""
database/init_db.py
Initializes the PostgreSQL database and creates the necessary tables.
"""
import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Database configuration
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://user:password@localhost:5432/ticket_db")
# Default database URL if not provided in environment variables

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Define a base class for declarative models
Base = declarative_base()

# Define the Ticket model
class Ticket(Base):
    """
    Represents a ticket in the database.
    """
    __tablename__ = "tickets"

    ticket_id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    status = Column(String, default="open")  # Default status is 'open'
    category = Column(String)
    opening_date = Column(DateTime, default=datetime.datetime.utcnow)  # Default opening date is now
    last_modification_date = Column(DateTime, default=datetime.datetime.utcnow)  # Default last modification date is now
    closing_date = Column(DateTime)

    def __repr__(self):
        return f"<Ticket ticket_id={self.ticket_id}, description='{self.description}', status='{self.status}'>"


# Create the tables if they don't exist
def init_db():
    """
    Initializes the database and creates the necessary tables.
    """
    Base.metadata.create_all(engine)
    print("Database initialized successfully.")


# Create a session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Creates a database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    init_db()
    # Example usage:
    # from database.init_db import get_db
    # db = next(get_db())
    # new_ticket = Ticket(description="Test ticket", status="open", category="Bug")
    # db.add(new_ticket)
    # db.commit()
    # print(f"Created ticket with id: {new_ticket.ticket_id}")
