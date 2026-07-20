from app import db, Ticket

def count_open_tickets(days):
    # Query open tickets within the last X days
    open_tickets = Ticket.query.filter_by(status='open', opening_date=db.func.now() - db.func.timedelta(days=days)).all()
    return len(open_tickets)