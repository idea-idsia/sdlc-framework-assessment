'''
Microservice Manager Class.
'''
import sqlite3
from datetime import datetime, timedelta
class MicroserviceManager:
    def __init__(self):
        self.conn = sqlite3.connect('tickets.db')
    def get_open_ticket_count(self, hours=0, days=0):
        cursor = self.conn.cursor()
        try:
            time_filter = datetime.now() - timedelta(hours=hours, days=days)
            query = 'SELECT COUNT(*) FROM tickets WHERE status=? AND opened_at >= ?'
            cursor.execute(query, ('open', time_filter))
            result = cursor.fetchone()
            return result[0] if result else 0
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return 0
    def get_open_tickets_by_category(self):
        cursor = self.conn.cursor()
        try:
            query = 'SELECT category, COUNT(*) FROM tickets WHERE status="open" GROUP BY category'
            cursor.execute(query)
            results = cursor.fetchall()
            return {category: count for category, count in results}
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return {}
    def get_active_tickets_by_category(self):
        cursor = self.conn.cursor()
        try:
            query = 'SELECT category, COUNT(*) FROM tickets WHERE status="active" GROUP BY category'
            cursor.execute(query)
            results = cursor.fetchall()
            return {category: count for category, count in results}
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return {}
    def close_connection(self):
        if self.conn:
            self.conn.close()