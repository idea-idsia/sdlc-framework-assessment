from flask import Flask, jsonify
import sqlite3
from datetime import date, timedelta

app = Flask(__name__)

@app.route('/service1', methods=['GET'])
def service1():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    period = request.args.get('period')
    if period == 'hours':
        time_delta = timedelta(hours=int(request.args.get('value')))
    elif period == 'days':
        time_delta = timedelta(days=int(request.args.get('value')))
    else:
        return jsonify({"error": "Invalid period"}), 400
    cursor.execute("SELECT COUNT(*) FROM tickets WHERE opening_date >= ? AND status != 'closed'", (date.today() - time_delta,))
    count = cursor.fetchone()[0]
    return jsonify({"count": count})

@app.route('/service2', methods=['GET'])
def service2():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(closing_date - opening_date) FROM tickets WHERE closing_date IS NOT NULL GROUP BY STRFTIME('%Y-%m', opening_date)")
    avg_resolution_time = cursor.fetchall()
    return jsonify({"avg_resolution_time": avg_resolution_time})

@app.route('/service3', methods=['GET'])
def service3():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT category, COUNT(*) FROM tickets WHERE status = 'active' GROUP BY category")
    active_tickets_per_category = cursor.fetchall()
    return jsonify({"active_tickets_per_category": active_tickets_per_category})

if __name__ == '__main__':
    app.run(debug=True)