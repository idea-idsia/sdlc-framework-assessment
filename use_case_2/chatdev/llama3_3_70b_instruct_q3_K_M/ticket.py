# Ticket representation
'''
This module represents a single ticket with attributes such as status, description, category, opening date, last modification date, and closing date.
'''
import datetime
class Ticket:
    def __init__(self, id, status, description, category, opening_date, last_modification_date=None, closing_date=None):
        self.id = id
        self.status = status
        self.description = description
        self.category = category
        self.opening_date = opening_date
        self.last_modification_date = last_modification_date
        self.closing_date = closing_date
    def __str__(self):
        return f'Ticket {self.id}: {self.description} ({self.status})'