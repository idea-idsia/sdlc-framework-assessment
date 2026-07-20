'''
Provides methods for getting open tickets, calculating average resolution time by month,
and clustering tickets by category.
'''
import datetime
from db_manager import DatabaseManager
class MicroserviceAPI:
    def __init__(self):
        self.db = DatabaseManager()
    def get_open_tickets_in_period(self, period='last_24_hours'):
        if period == 'last_24_hours':
            one_day_ago = datetime.datetime.now() - datetime.timedelta(days=1)
            open_tickets = [ticket for ticket in self.db.get_open_tickets() if ticket[3] >= one_day_ago]
            return open_tickets
        else:
            return self.db.get_open_tickets()
    def average_ticket_resolution_time_by_month(self):
        start_date = datetime.datetime.now() - datetime.timedelta(days=30)
        end_date = datetime.datetime.now()
        total_resolution_time = 0
        num_resolved_tickets = 0
        resolved_tickets = [ticket for ticket in self.db.get_open_tickets() if ticket[3] == 'resolved']
        for ticket in resolved_tickets:
            if start_date <= ticket[4] < end_date:
                resolution_time = (ticket[5] - ticket[4]).total_seconds() / 3600
                total_resolution_time += resolution_time
                num_resolved_tickets += 1
        if num_resolved_tickets == 0:
            return "No resolved tickets found."
        else:
            average_resolution_time = total_resolution_time / num_resolved_tickets
            return f"Average resolution time: {average_resolution_time:.2f} hours"
    def cluster_tickets_by_category(self):
        active_counts = {}
        open_tickets = [ticket for ticket in self.db.get_open_tickets() if ticket[3] == 'open']
        for ticket in open_tickets:
            category = ticket[1]
            if category not in active_counts:
                active_counts[category] = 0
            active_counts[category] += 1
        return f"Clustered tickets by category: {active_counts}"