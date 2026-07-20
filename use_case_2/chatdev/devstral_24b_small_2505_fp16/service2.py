'''
Microservice to calculate average ticket resolution time by opening month.
'''
import sqlite3
class Service2:
    def __init__(self, db_name="ticket_management.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    def get_avg_resolution_time(self):
        query = '''
            SELECT strftime('%Y-%m', created_at) AS month,
                   AVG(julianday(closed_at) - julianday(created_at)) as avg_res_time
            FROM tickets
            WHERE status='closed'
            GROUP BY strftime('%Y-%m', created_at)
        '''
        return self.cursor.execute(query).fetchall()