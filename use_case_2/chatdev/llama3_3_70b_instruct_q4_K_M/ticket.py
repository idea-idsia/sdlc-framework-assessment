Python
'''
This file contains the Ticket class, which represents a ticket.
It has attributes for the ticket ID, description, status, opening date, last modification date, closing date, and category.
'''
class Ticket:
    def __init__(self, description, status, opening_date, last_modification_date, closing_date, category):
        self.description = description
        self.status = status
        self.opening_date = opening_date
        self.last_modification_date = last_modification_date
        self.closing_date = closing_date
        self.category = category
    def __str__(self):
        return f"Description: {self.description}, Status: {self.status}, Opening Date: {self.opening_date}, Last Modification Date: {self.last_modification_date}, Closing Date: {self.closing_date}, Category: {self.category}"