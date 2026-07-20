'''
Microservice to cluster tickets by category and count active ones.
'''
import sqlite3
class Service3:
    def __init__(self, db_name="ticket_management.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    def get_active_tickets_by_category(self):
        query = '''
            SELECT category, COUNT(*) as active_count
            FROM tickets
            WHERE status='active'
            GROUP BY category
        '''
        return self.cursor.execute(query).fetchall()