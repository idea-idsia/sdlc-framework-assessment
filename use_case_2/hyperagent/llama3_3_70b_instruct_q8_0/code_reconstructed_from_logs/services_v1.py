import matplotlib.pyplot as plt
from database import TicketDatabase

class Services:
    def __init__(self):
        self.db = TicketDatabase("tickets.db")

    def get_open_tickets(self, period):
        if period == "hours":
            self.db.cursor.execute("SELECT * FROM tickets WHERE opening_date >= DATE('now', '-1 hour') AND status = 'open'")
        elif period == "days":
            self.db.cursor.execute("SELECT * FROM tickets WHERE opening_date >= DATE('now', '-1 day') AND status = 'open'")
        return len(self.db.cursor.fetchall())

    def get_average_resolution_time(self):
        self.db.cursor.execute("SELECT AVG(closing_date - opening_date) FROM tickets WHERE status = 'closed'")
        return self.db.cursor.fetchone()[0]

    def cluster_tickets_by_category(self):
        self.db.cursor.execute("SELECT category, COUNT(*) FROM tickets GROUP BY category")
        categories = self.db.cursor.fetchall()
        return {category[0]: category[1] for category in categories}

if __name__ == "__main__":
    services = Services()
    print(services.get_open_tickets("hours"))
    print(services.get_average_resolution_time())
    print(services.cluster_tickets_by_category())