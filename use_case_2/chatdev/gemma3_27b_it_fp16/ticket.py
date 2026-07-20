'''
Represents a ticket in the ticket management system.
'''
class Ticket:
    def __init__(self, ticket_id, description, status, category, opening_date, last_modification_date):
        self.ticket_id = ticket_id
        self.description = description
        self.status = status
        self.category = category
        self.opening_date = opening_date
        self.last_modification_date = last_modification_date
    def __str__(self):
        return f"ID: {self.ticket_id}, Description: {self.description}, Status: {self.status}, Category: {self.category}, Opening Date: {self.opening_date}, Last Modified: {self.last_modification_date}"