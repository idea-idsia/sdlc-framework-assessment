'''
The Service3 class that implements specific service for ticket status updating.
'''
from database import Database
class Service3:
    def __init__(self, db):
        self.db = db
    def update_ticket_status(self, ticket_id, new_status):
        try:
            self.db.cursor.execute("""
                UPDATE tickets SET status = ? WHERE id = ?
            """, (new_status, ticket_id))
            self.db.conn.commit()
        except Exception as e:
            print(f"An error occurred: {str(e)}")