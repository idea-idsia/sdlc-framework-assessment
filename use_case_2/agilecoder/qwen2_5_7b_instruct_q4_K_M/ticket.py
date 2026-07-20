'''
Representation of a ticket.
'''
class Ticket:
    def __init__(self, category: str, description: str):
        self.category = category
        self.description = description