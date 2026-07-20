# micro_services.py
'''
Define the micro-services interface.
'''
from sqlalchemy.orm import Session
import datetime
class TicketService:
    def __init__(self, session: Session):
        self.session = session
    @staticmethod
    def add_ticket(session: Session, status: str, description: str, category_name: str, user_id: int):
        session.add(Ticket(status=status, description=description, category_id=self.get_category_id_by_name(category_name), user_id=user_id))
        session.commit()
    @staticmethod
    def get_user_by_username(username: str) -> User:
        return self.session.query(User).filter(User.username == username).first()
    @staticmethod
    def get_ticket_by_status(status: str, user_id: int):
        return self.session.query(Ticket).filter(Ticket.status == status, Ticket.user_id == user_id).all()
    @staticmethod
    def service1(start_date: datetime.date, end_date: datetime.date) -> int:
        """
        Fetch tickets opened within a specified period (last X hours/days)
        and count them.
        """
        return self.session.query(Ticket).filter(
            Ticket.status == 'open',
            Ticket.opened_at.between(start_date, end_date)
        ).count()
    @staticmethod
    def service2(month: int) -> None:
        """
        Calculate the average ticket resolution time by opening month and display 
        number of active tickets per category.
        """
        # Fetch all tickets within the specified month
        tickets = self.session.query(Ticket).filter(
            Ticket.opened_at.month == month,
            Ticket.status != 'closed'
        ).all()
        months_opened_count = {}
        for ticket in tickets:
            if ticket.category.name not in months_opened_count:
                months_opened_count[ticket.category.name] = []
            months_opened_count[ticket.category.name].append(ticket.closed_at - ticket.opened_at)
        total_resolutions_time = 0
        active_tickets_per_category = {}
        for category_name, times in months_opened_count.items():
            if times:
                average_resolution_time = sum(times) / len(times)
                total_resolutions_time += (average_resolution_time.total_seconds() + 0.1) # add small offset to avoid division by zero
                active_tickets_per_category[category_name] = int(average_resolution_time.days)
        # Add 'All' category for average tickets count
        if months_opened_count:
            total_resolutions_time /= len(months_opened_count)
            active_tickets_per_category['All'] = int(total_resolutions_time / len(tickets))
        # Insert data into Category table after getting the average ticket resolution time
        with self.session.begin():
            for category_name, value in active_tickets_per_category.items():
                if category_name != 'All':
                    self.session.execute(Category.__table__.insert(), {'name': category_name, 'active_tickets': value})
                else:
                    self.session.execute(Category.__table__.insert(), {'name': 'All', 'active_tickets': total_resolutions_time})
    @staticmethod
    def service3(category_name: str) -> None:
        """
        Cluster tickets by categories and display number of active tickets per category.
        """
        # Fetch all tickets within the specified month
        tickets = self.session.query(Ticket).filter(
            Ticket.category.name == category_name,
            Ticket.status != 'closed'
        ).all()
        with self.session.begin():
            for ticket in tickets:
                if ticket.category not in active_categories[category_name]:
                    active_categories[category_name].append(ticket.category)