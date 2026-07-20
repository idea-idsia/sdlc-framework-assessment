'''
The Service2 class that implements specific service for average resolution time.
'''
from database import Database
class Service2:
    def __init__(self, db):
        self.db = db
    def get_average_resolution_time(self):
        try:
            self.db.cursor.execute("""
                SELECT AVG(closing_date - opening_date) FROM tickets
            """)
            return self.db.cursor.fetchone()[0]
        except Exception as e:
            print(f"An error occurred: {str(e)}")