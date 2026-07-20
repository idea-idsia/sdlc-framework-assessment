# Service 3: Display the number of active tickets by category
'''
This module provides a service to display the number of active tickets by category.
'''
import datetime
class Service3:
    def __init__(self, db):
        self.db = db
    def get_active_tickets_by_category(self):
        self.db.cursor.execute('''
            SELECT category, COUNT(*) 
            FROM tickets 
            WHERE status = 'active' 
            GROUP BY category
        ''')
        return self.db.cursor.fetchall()