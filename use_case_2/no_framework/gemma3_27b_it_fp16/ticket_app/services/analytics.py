import pandas as pd
from datetime import datetime, timedelta
from database import Database

class AnalyticsService:
    def __init__(self):
        self.db = Database()

    def tickets_opened_in_period(self, period, period_unit):
        # Period unit can be "hours" or "days"
        if period_unit == "hours":
            end_date = datetime.now()
            start_date = end_date - timedelta(hours=period)
        elif period_unit == "days":
            end_date = datetime.now()
            start_date = end_date - timedelta(days=period)
        else:
            return "Invalid period unit"

        tickets = self.db.get_tickets()
        recent_tickets = [t for t in tickets if start_date <= t.opening_date <= end_date and t.status != 'closed']
        return len(recent_tickets)

    def average_resolution_time(self):
        tickets = self.db.get_tickets()
        df = pd.DataFrame([
            {'opening_month': t.opening_date.month, 'closing_date': t.closing_date} for t in tickets if t.closing_date
        ])
        df['resolution_time'] = (df['closing_date'] - df['opening_date']).dt.days
        return df.groupby('opening_month')['resolution_time'].mean().to_dict()

    def cluster_tickets_by_category(self):
        tickets = self.db.get_tickets()
        category_counts = {}
        for ticket in tickets:
            if ticket.status == 'active':
                category = ticket.category
                category_counts[category] = category_counts.get(category, 0) + 1
        return category_counts