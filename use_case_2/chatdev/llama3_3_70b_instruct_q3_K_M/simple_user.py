# Simple user representation
'''
This module represents a simple user who can create tickets.
'''
class SimpleUser:
    def __init__(self, name):
        self.name = name
    def create_ticket(self, db, description, category):
        ticket = Ticket(None, 'open', description, category, datetime.date.today())
        db.insert_ticket(ticket)