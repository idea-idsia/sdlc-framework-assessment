'''
Handles message exchange between users and helpdesk staff.
'''
class MessageSystem:
    def __init__(self):
        self.messages = {}
    def add_message(self, ticket_id, message):
        if ticket_id not in self.messages:
            self.messages[ticket_id] = []
        self.messages[ticket_id].append(message)
    def view_messages(self, ticket_id):
        return self.messages.get(ticket_id, [])