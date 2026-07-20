# microservices/service2.py

import sqlite3
from collections import defaultdict
from datetime import datetime

def average_resolution_time_by_month():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT strftime('%Y-%m', opening_date), AVG(julianday(closing_date) - julianday(opening_date)) AS avg_days
        FROM tickets WHERE status='closed'
        GROUP BY strftime('%Y-%m', opening_date)
    ''')

    results = cursor.fetchall()
    conn.close()

    return dict(results)

if __name__ == "__main__":
    print("Average resolution time by month:", average_resolution_time_by_month())