'''
Microservice to calculate open tickets within a specific number of days.
'''
import sqlite3
from datetime import datetime, timedelta
class Service1:
    def __init__(self, db_name="ticket_management.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    def get_open_tickets(self, days):
        start_date = datetime.now() - timedelta(days=days)
        query = '''
            SELECT * FROM tickets
            WHERE status='open' AND created_at >= ?
        '''
        return self.cursor.execute(query, (start_date,)).fetchall()