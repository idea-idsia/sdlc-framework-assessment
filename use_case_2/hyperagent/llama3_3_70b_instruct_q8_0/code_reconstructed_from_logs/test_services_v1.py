import matplotlib.pyplot as plt
from database import TicketDatabase
import sqlite3

class Services:
    def __init__(self):
        self.db = TicketDatabase('tickets.db')

    def get_open_tickets(self, period):
        if period == 'hours':
            self.db.cursor.execute(\"SELECT * FROM tickets WHERE opening_date >= DATE('now', '-1 hour') AND status = 'open'\")
        elif period == 'days':
            self.db.cursor.execute(\"SELECT * FROM tickets WHERE opening_date >= DATE('now', '-1 day') AND status = 'open'\")
        return len(self.db.cursor.fetchall())

    def get_average_resolution_time(self):
        self.db.cursor.execute(\"SELECT AVG(closing_date - opening_date) FROM tickets WHERE status = 'closed'\")
        return self.db.cursor.fetchone()[0]

    def cluster_tickets_by_category(self):
        self.db.cursor.execute(\"SELECT category, COUNT(*) FROM tickets GROUP BY category\")
        categories = self.db.cursor.fetchall()
        return {category[0]: category[1] for category in categories}

# Create a test database
conn = sqlite3.connect('test_tickets.db')
cursor = conn.cursor()

# Create table for tickets
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY,
        description TEXT NOT NULL,
        category TEXT NOT NULL CHECK(category IN ('facility management', 'technical IT', 'services complaints')),
        status TEXT NOT NULL CHECK(status IN ('open', 'active', 'closed')),
        opening_date DATE NOT NULL DEFAULT CURRENT_DATE,
        last_modification_date DATE NOT NULL DEFAULT CURRENT_DATE,
        closing_date DATE
    )
''')

# Insert test data
cursor.execute(\"INSERT INTO tickets (description, category, status, opening_date, last_modification_date, closing_date) VALUES ('Test ticket', 'facility management', 'open', DATE('now'), DATE('now'), NULL)\")
conn.commit()

# Test the Services class with the test database
services = Services()
print('Number of open tickets in the last hour:', services.get_open_tickets('hours'))
print('Average resolution time for closed tickets:', services.get_average_resolution_time())
print('Tickets clustered by category:', services.cluster_tickets_by_category())