from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

# Service 1: Get number of open tickets in the last X hours/days
@app.route('/open_tickets', methods=['GET'])
def get_open_tickets():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    period = request.args.get('period')
    if period.endswith('hours'):
        delta = timedelta(hours=int(period[:-6]))
    elif period.endswith('days'):
        delta = timedelta(days=int(period[:-5]))
    else:
        return jsonify({'error': 'Invalid period'}), 400
    cursor.execute("SELECT COUNT(*) FROM tickets WHERE opening_date >= ? AND status='open'", (datetime.now() - delta,))
    count = cursor.fetchone()[0]
    conn.close()
    return jsonify({'count': count})

# Service 2: Get average ticket resolution time by opening month
@app.route('/average_resolution_time', methods=['GET'])
def get_average_resolution_time():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT STRFTIME('%Y-%m', opening_date) AS month, AVG(STRFTIME('%s', closing_date) - STRFTIME('%s', opening_date)) AS avg_resolution_time FROM tickets WHERE status='closed' GROUP BY month")
    result = cursor.fetchall()
    conn.close()
    return jsonify([{'month': row[0], 'avg_resolution_time': row[1]} for row in result])

# Service 3: Get number of active tickets per category
@app.route('/active_tickets_by_category', methods=['GET'])
def get_active_tickets_by_category():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT category, COUNT(*) AS count FROM tickets WHERE status='active' GROUP BY category")
    result = cursor.fetchall()
    conn.close()
    return jsonify([{'category': row[0], 'count': row[1]} for row in result])

if __name__ == '__main__':
    app.run(debug=True)