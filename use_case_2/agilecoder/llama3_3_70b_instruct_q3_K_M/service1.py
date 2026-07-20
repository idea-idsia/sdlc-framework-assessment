'''
The Service1 class that implements specific service for ticket category clustering.
'''
from database import Database
class Service1:
    def __init__(self, db):
        self.db = db
    def get_ticket_categories(self):
        try:
            self.db.cursor.execute("""
                SELECT DISTINCT category FROM tickets
            """)
            return [row[0] for row in self.db.cursor.fetchall()]
        except Exception as e:
            print(f"An error occurred: {str(e)}")