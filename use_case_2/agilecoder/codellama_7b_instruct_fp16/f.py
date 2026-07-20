'''
File: f.py
Author: $USERNAME
Description: $DESCRIPTION
'''
class Guide:
    def __init__(self):
        pass
    def create_ticket(self, ticket_id, status):
        print("Creating a new ticket with ID {} and status {}"\
              .format(ticket_id, status))
    def view_tickets(self):
        tickets = self.get_all_tickets()
        for ticket in tickets:
            print("Ticket ID:", ticket["ticket_id"], "Status:", ticket["status"])
    def update_ticket(self, ticket_id, status):
        print("Updating ticket with ID {} to status {}"\
              .format(ticket_id, status))
    def delete_ticket(self, ticket_id):
        print("Deleting ticket with ID {}".format(ticket_id))