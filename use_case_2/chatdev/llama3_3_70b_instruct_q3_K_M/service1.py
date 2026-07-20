# Service 1: Display the number of tickets opened in a selected period that have not yet been closed
'''
This module provides a service to display the number of tickets opened in a selected period that have not yet been closed.
'''
import datetime
class Service1:
    def __init__(self, db):
        self.db = db
    def get_open_tickets(self, period_hours):
        # Calculate the time frame
        now = datetime.datetime.now()
        past = now - datetime.timedelta(hours=period_hours)
        # Query the database for tickets opened within this timeframe that are not closed
        self.db.cursor.execute('''
            SELECT * FROM tickets 
            WHERE opening_date >= ? AND status != 'closed'
        ''', (past,))
        return self.db.cursor.fetchall()