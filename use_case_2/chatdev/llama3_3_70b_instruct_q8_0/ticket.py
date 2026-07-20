# Import necessary libraries
from datetime import date
'''
Ticket class.
It represents a ticket with attributes for status, description, category, and dates.
'''
class Ticket:
    def __init__(self, description, category):
        self.status = "open"
        self.description = description
        self.category = category
        self.opening_date = date.today()
        self.last_modification_date = date.today()
        self.closing_date = None
        self.id = None