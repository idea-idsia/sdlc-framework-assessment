# Helpdesk user representation
'''
This module represents a helpdesk staff member who can view, update, and close tickets.
'''
class HelpdeskUser:
    def __init__(self, name):
        self.name = name
    def update_ticket(self, db, ticket_id, new_status):
        db.cursor.execute('''
            UPDATE tickets
            SET status = ?
            WHERE id = ?
        ''', (new_status, ticket_id))
        db.conn.commit()
    def close_ticket(self, db, ticket_id):
        self.update_ticket(db, ticket_id, 'closed')