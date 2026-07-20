from flask_sqlalchemy import SQLAlchemy
from typing import List
import matplotlib.pyplot as plt
import seaborn as sns

db = SQLAlchemy()

class User(db.Model):
    """
    Represents a user in the system.
    
    Attributes:
        id (int): Unique identifier for the user.
        username (str): The username chosen by the user.
        email (str): The email address of the user.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username: str, email: str):
        """
        Initializes a new User instance.
        
        Args:
            username (str): The username chosen by the user.
            email (str): The email address of the user.
        """
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
        user_id (int): The ID of the user who reported the issue.
        helpdesk_staff_id (int): The ID of the help desk staff member assigned to the ticket.
    """
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(64), default="Open")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    helpdesk_staff_id = db.Column(db.Integer, db.ForeignKey('helpdesk_staff.id'))

    def __init__(self, title: str, description: str, user_id: int):
        """
        Initializes a new Ticket instance.
        
        Args:
            title (str): The title of the ticket.
            description (str): The description of the ticket.
            user_id (int): The ID of the user who reported the issue.
        """
        self.title = title
        self.description = description
        self.user_id = user_id

    def update_status(self, status: str) -> None:
        """
        Updates the status of the ticket.
        
        Args:
            status (str): The new status of the ticket.
        
        Raises:
            ValueError: If the status is not one of "Open", "In Progress", or "Closed".
        """
        if status not in ["Open", "In Progress", "Closed"]:
            raise ValueError("Invalid status")
        self.status = status
        db.session.commit()


class HelpDeskStaff(db.Model):
    """
    Represents a help desk staff member in the system.
    
    Attributes:
        id (int): Unique identifier for the staff member.
        username (str): The username chosen by the staff member.
        email (str): The email address of the staff member.
    """
    __tablename__ = 'helpdesk_staff'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username: str, email: str):
        """
        Initializes a new HelpDeskStaff instance.
        
        Args:
            username (str): The username chosen by the staff member.
            email (str): The email address of the staff member.
        """
        self.username = username
        self.email = email

    def assign_ticket(self, ticket_id: int) -> None:
        """
        Assigns a ticket to the staff member.
        
        Args:
            ticket_id (int): The ID of the ticket to be assigned.
        """
        ticket = Ticket.query.get(ticket_id)
        if ticket:
            ticket.helpdesk_staff_id = self.id
            db.session.commit()


class TicketManagementSystem:
    """
    Represents the ticket management system.
    
    Attributes:
        tickets (List[Ticket]): A list of all tickets in the system.
        users (List[User]): A list of all users in the system.
        helpdesk_staff (List[HelpDeskStaff]): A list of all help desk staff members in the system.
    """
    def __init__(self):
        """
        Initializes a new TicketManagementSystem instance.
        """
        pass

    @staticmethod
    def report_issue(user: User, issue: str) -> Ticket:
        """
        Reports an issue by creating a new Ticket instance.
        
        Args:
            user (User): The user reporting the issue.
            issue (str): The description of the issue.
        
        Returns:
            Ticket: The newly created ticket.
        """
        ticket = Ticket(title="Issue reported by " + user.username, description=issue, user_id=user.id)
        db.session.add(ticket)
        db.session.commit()
        return ticket

    @staticmethod
    def view_tickets() -> List[Ticket]:
        """
        Retrieves a list of all tickets in the system.
        
        Returns:
            List[Ticket]: A list of all tickets.
        """
        return Ticket.query.all()

    @staticmethod
    def assign_ticket(helpdesk_staff: HelpDeskStaff, ticket_id: int) -> None:
        """
        Assigns a ticket to a help desk staff member.
        
        Args:
            helpdesk_staff (HelpDeskStaff): The staff member to be assigned the ticket.
            ticket_id (int): The ID of the ticket to be assigned.
        """
        helpdesk_staff.assign_ticket(ticket_id)


class DataVisualizer:
    """
    Represents a data visualizer for ticket data.
    
    Attributes:
        ticket_data (dict): A dictionary containing ticket data.
    """
    def __init__(self):
        """
        Initializes a new DataVisualizer instance.
        """
        pass

    @staticmethod
    def visualize_ticket_data() -> None:
        """
        Visualizes the ticket data using matplotlib and seaborn.
        """
        tickets = Ticket.query.all()
        statuses = [ticket.status for ticket in tickets]
        sns.countplot(x=statuses)
        plt.xlabel("Status")
        plt.ylabel("Count")
        plt.title("Ticket Status Distribution")
        plt.show()

