'''
Represents a single ticket.
'''
class Ticket:
    def __init__(self, description, category):
        self.description = description
        self.category = category
        self.status = 'open'
    def update_status(self, new_status):
        self.status = new_status