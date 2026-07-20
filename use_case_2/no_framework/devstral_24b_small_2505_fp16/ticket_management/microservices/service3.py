# microservices/service3.py

import sqlite3

def active_tickets_by_category():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT category, COUNT(*) FROM tickets WHERE status='active' GROUP BY category
    ''')

    results = cursor.fetchall()
    conn.close()

    return dict(results)

if __name__ == "__main__":
    print("Active tickets by category:", active_tickets_by_category())