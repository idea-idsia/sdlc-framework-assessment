## analytics_service.py
from sqlalchemy.orm import sessionmaker
from models import TicketModel, Base
from sqlalchemy import create_engine

class AnalyticsService:
    def __init__(self):
        # Initialize the database engine and session factory
        DATABASE_URI = 'sqlite:///tickets.db'
        self.engine = create_engine(DATABASE_URI)
        Session = sessionmaker(bind=self.engine)
        self.Session = Session  # Store session class for reuse

    def get_resolution_times(self) -> list[dict]:
        """
        Fetches resolution times for tickets.
        
        Returns:
            A list of dictionaries containing ticket ID and its resolution time.
        """
        with self.Session() as session:  # Use context manager to ensure session is closed
            tickets = session.query(TicketModel).all()
            result = [
                {"ticket_id": t.id, "resolution_time": (t.updated_at - t.created_at).total_seconds() if t.status == 'closed' else None}
                for t in tickets
            ]
        return result

    def get_active_tickets_by_category(self) -> list[dict]:
        """
        Fetches active tickets by category.
        
        Returns:
            A list of dictionaries containing ticket ID and its status.
        """
        with self.Session() as session:  # Use context manager to ensure session is closed
            tickets = session.query(TicketModel).filter_by(status='open').all()
            result = [{"ticket_id": t.id, "category": t.status} for t in tickets]
        return result

    def __del__(self):
        # Ensure the engine is disposed when the object is destroyed
        self.engine.dispose()
