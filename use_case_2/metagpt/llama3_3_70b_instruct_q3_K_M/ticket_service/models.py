from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class BaseUser(db.Model):
    """
    Base class for users and staff.
    
    Attributes:
        id (int): Unique identifier.
        username (str): The chosen username.
        email (str): The email address.
        password_hash (str): Hashed password.
    """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password: str):
        """
        Sets the password.
        
        Args:
            password (str): The password to be set.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """
        Checks if the provided password matches.
        
        Args:
            password (str): The password to be checked.
        
        Returns:
            bool: True if the password matches, False otherwise.
        """
        return check_password_hash(self.password_hash, password)


class User(BaseUser):
    """
    Represents a user in the system.
    
    Attributes:
        id (int): Unique identifier for the user.
        username (str): The username chosen by the user.
        email (str): The email address of the user.
    """
    __tablename__ = 'users'

    def __init__(self, id: int = None, username: str = None, email: str = None):
        """
        Initializes a new User instance.
        
        Args:
            id (int): Unique identifier for the user. Defaults to None.
            username (str): The username chosen by the user. Defaults to None.
            email (str): The email address of the user. Defaults to None.
        """
        self.id = id
        self.username = username
        self.email = email


class HelpDeskStaff(BaseUser):
    """
    Represents a help desk staff member in the system.
    
    Attributes:
        id (int): Unique identifier for the staff member.
        username (str): The username chosen by the staff member.
        email (str): The email address of the staff member.
    """
    __tablename__ = 'help_desk_staff'

    def __init__(self, id: int = None, username: str = None, email: str = None):
        """
        Initializes a new HelpDeskStaff instance.
        
        Args:
            id (int): Unique identifier for the staff member. Defaults to None.
            username (str): The username chosen by the staff member. Defaults to None.
            email (str): The email address of the staff member. Defaults to None.
        """
        self.id = id
        self.username = username
        self.email = email


class Ticket(db.Model):
    """
    Represents a ticket in the system.
    
    Attributes:
        id (int): Unique identifier for the ticket.
        title (str): The title of the ticket.
        description (str): The description of the ticket.
        status (str): The current status of the ticket.
    """
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __init__(self, id: int = None, title: str = None, description: str = None, status: str = "open"):
        """
        Initializes a new Ticket instance.
        
        Args:
            id (int): Unique identifier for the ticket. Defaults to None.
            title (str): The title of the ticket. Defaults to None.
            description (str): The description of the ticket. Defaults to None.
            status (str): The current status of the ticket. Defaults to "open".
        """
        self.id = id
        self.title = title
        self.description = description
        self.status = status


class TicketManager:
    """
    Manages tickets in the system.
    
    Attributes:
        db_session: The database session used for CRUD operations.
    """
    def __init__(self, db_session):
        """
        Initializes a new TicketManager instance.
        
        Args:
            db_session: The database session to be used.
        """
        self.db_session = db_session

    def assign_status(self, ticket_id: int, status: str):
        """
        Assigns a status to a ticket.
        
        Args:
            ticket_id (int): The ID of the ticket.
            status (str): The status to be assigned.
        
        Raises:
            ValueError: If the ticket ID is not found.
        """
        ticket = self.db_session.query(Ticket).filter_by(id=ticket_id).first()
        if ticket is None:
            raise ValueError("Ticket ID not found")
        ticket.status = status
        self.db_session.commit()

    def exchange_messages(self, ticket_id: int, message: str):
        """
        Exchanges messages for a ticket.
        
        Args:
            ticket_id (int): The ID of the ticket.
            message (str): The message to be exchanged.
        
        Raises:
            ValueError: If the ticket ID is not found.
        """
        ticket = self.db_session.query(Ticket).filter_by(id=ticket_id).first()
        if ticket is None:
            raise ValueError("Ticket ID not found")
        # For demonstration, assuming messages are stored in a list
        if not hasattr(ticket, 'messages'):
            ticket.messages = []
        ticket.messages.append(message)
        self.db_session.commit()

    def analyze_data(self):
        """
        Analyzes data related to tickets.
        
        Returns:
            dict: A dictionary containing the analysis results.
        """
        # Example analysis: counting tickets by status
        status_counts = {}
        for ticket in self.db_session.query(Ticket).all():
            if ticket.status not in status_counts:
                status_counts[ticket.status] = 1
            else:
                status_counts[ticket.status] += 1
        return status_counts
