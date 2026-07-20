import datetime

class Ticket:
    def __init__(self, description, category, status='open', opening_date=None):
        self.description = description
        self.category = category
        self.status = status
        self.opening_date = opening_date if opening_date else datetime.datetime.now()
        self.last_modification_date = self.opening_date
        self.closing_date = None

    def __repr__(self):
        return f"Ticket(description='{self.description}', category='{self.category}', status='{self.status}')"

class Message:
    def __init__(self, ticket_id, sender, content, timestamp=None):
        self.ticket_id = ticket_id
        self.sender = sender
        self.content = content
        self.timestamp = timestamp if timestamp else datetime.datetime.now()