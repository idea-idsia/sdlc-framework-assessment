from datetime import timedelta
import pandas as pd
from sqlalchemy.orm import sessionmaker
from models import Ticket, Message
from sqlalchemy import func


class Service1:
    @staticmethod
    def get_open_tickets_count(period):
        Session = sessionmaker(bind=db.engine)
        session = Session()

        end_date = datetime.datetime.now()
        start_date = end_date - period

        tickets = session.query(Ticket).filter(Ticket.status == 'open', Ticket.opening_date >= start_date,
                                               Ticket.closing_date.is_(None)).count()
        return tickets


class Service2:
    @staticmethod
    def get_average_resolution_time_by_month():
        Session = sessionmaker(bind=db.engine)
        session = Session()

        resolution_times = []
        for ticket in session.query(Ticket):
            if ticket.status == 'closed':
                opening_date = ticket.opening_date.date()
                closing_date = ticket.closing_date.date()
                duration = (closing_date - opening_date).days
                resolution_times.append((opening_date.month, duration))

        df = pd.DataFrame(resolution_times, columns=['month', 'resolution_time'])
        average_resolution_time = df.groupby('month')['resolution_time'].mean().reset_index(name='average_duration')
        return average_resolution_time


class Service3:
    @staticmethod
    def get_active_tickets_by_category():
        Session = sessionmaker(bind=db.engine)
        session = Session()

        tickets_count = session.query(Ticket.category, func.count(Ticket.id)).filter_by(status='active').group_by(
            Ticket.category).all()
        return tickets_count