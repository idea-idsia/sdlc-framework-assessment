# Import necessary libraries
from db_manager import DBManager
'''
Micro-services class.
It provides methods for data visualization and analysis functionalities.
'''
class Service1:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    def get_tickets(self, period):
        # Query database to retrieve tickets within the specified period
        query = "SELECT * FROM tickets WHERE opening_date >= ? AND opening_date <= ?"
        params = (period['start'], period['end'])
        results = self.db_manager.execute_query(query, params)
        return results
class Service2:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    def get_average_resolution_time(self):
        # Query database to retrieve average resolution time
        query = "SELECT AVG(closing_date - opening_date) FROM tickets"
        results = self.db_manager.execute_query(query, ())
        return results
class Service3:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    def get_category_clusters(self):
        # Query database to retrieve category clusters
        query = "SELECT category, COUNT(*) FROM tickets GROUP BY category"
        results = self.db_manager.execute_query(query, ())
        return results