class Services:
    def __init__(self):
        self.db = TicketDatabase('tickets.db')

    def get_open_tickets(self, period, category=None, status=None):
        if period == 'hours':
            query = "SELECT * FROM tickets WHERE opening_date >= DATE('now', '-1 hour')"
        elif period == 'days':
            query = "SELECT * FROM tickets WHERE opening_date >= DATE('now', '-1 day')"

        if category:
            query += " AND category = '{}'".format(category)
        if status:
            query += " AND status = '{}'".format(status)

        self.db.cursor.execute(query)
        return len(self.db.cursor.fetchall())

    def get_average_resolution_time(self, category=None):
        query = "SELECT AVG(closing_date - opening_date) FROM tickets WHERE status = 'closed'"
        if category:
            query += " AND category = '{}'".format(category)
        self.db.cursor.execute(query)
        return self.db.cursor.fetchone()[0]

    def cluster_tickets_by_category(self, status=None):
        query = "SELECT category, COUNT(*) FROM tickets"
        if status:
            query += " WHERE status = '{}'".format(status)
        query += " GROUP BY category"
        self.db.cursor.execute(query)
        categories = self.db.cursor.fetchall()
        return {category[0]: category[1] for category in categories}