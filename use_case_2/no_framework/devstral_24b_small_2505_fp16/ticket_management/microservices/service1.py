# microservices/service1.py

import sqlite3
from datetime import datetime, timedelta

def get_open_tickets_period(hours=0, days=0):
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()

    end_date = datetime.now().isoformat()
    start_date = (datetime.now() - timedelta(hours=hours, days=days)).isoformat()

    cursor.execute('''
        SELECT COUNT(*) FROM tickets
        WHERE status='open' AND opening_date BETWEEN ? AND ?
    ''', (start_date, end_date))

    result = cursor.fetchone()
    conn.close()

    return result[0] if result else 0

if __name__ == "__main__":
    print(f"Open tickets in the last 24 hours: {get_open_tickets_period(hours=24)}")