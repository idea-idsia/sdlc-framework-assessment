"""
ticket_service/models.py
Defines the Ticket model using SQLAlchemy.
"""
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Database configuration (using environment variables is best practice)
DATABASE_URL = "postgresql://user:password@localhost:5432/ticket_db"  # Default value

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Define a base class for declarative models
Base = declarative_base()


class Ticket(Base):
    """
    Represents a ticket in the database.
    """
    __tablename__ = "tickets"

    ticket_id: int = Column(Integer, primary_key=True, index=True)
    description: str = Column(String, nullable=False)
    status: str = Column(String, default="open")  # Default status is 'open'
    category: str = Column(String)
    opening_date: datetime = Column(DateTime, default=datetime.datetime.utcnow)  # Default opening date is now
    last_modification_date: datetime = Column(DateTime, default=datetime.datetime.utcnow)  # Default last modification date is now
    closing_date: datetime = Column(DateTime)

    def __repr__(self) -> str:
        return f"<Ticket ticket_id={self.ticket_id}, description='{self.description}', status='{self.status}'>"


# Create the tables if they don't exist
def init_db() -> None:
    """
    Initializes the database and creates the necessary tables.
    """
    Base.metadata.create_all(engine)
    print("Database initialized successfully.")


# Create a session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> iter:
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
    # from ticket_service.models import get_db, Ticket
    # db = next(get_db())
    # new_ticket = Ticket(description="Test ticket", status="open", category="Bug")
    # db.add(new_ticket)
    # db.commit()
    # print(f"Created ticket with id: {new_ticket.ticket_id}")
