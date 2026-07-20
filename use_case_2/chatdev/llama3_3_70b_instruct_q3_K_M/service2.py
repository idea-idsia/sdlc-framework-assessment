# Service 2: Display the average resolution time of all tickets
'''
This module provides a service to display the average resolution time of all tickets.
'''
import datetime
class Service2:
    def __init__(self, db):
        self.db = db
    def get_average_resolution_time(self):
        self.db.cursor.execute('''
            SELECT AVG(strftime('%J', closing_date) - strftime('%J', opening_date)) 
            FROM tickets 
            WHERE status = 'closed'
        ''')
        return self.db.cursor.fetchone()