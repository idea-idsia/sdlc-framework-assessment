'''
Represents a ticket with its attributes.
'''
class Ticket:
    def __init__(self, ticket_id, status, description, category, opening_date, last_modification_date, closing_date):
        self.ticket_id = ticket_id
        self.status = status
        self.description = description
        self.category = category
        self.opening_date = opening_date
        self.last_modification_date = last_modification_date
        self.closing_date = closing_date
    def __str__(self):
        return f"Ticket ID: {self.ticket_id}, Status: {self.status}, Description: {self.description}"