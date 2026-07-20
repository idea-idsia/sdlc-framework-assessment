from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/service1', methods=['GET'])
def service1():
    period = request.args.get('period', 'days')
    value = int(request.args.get('value', 7))

    if period == 'hours':
        cutoff_time = datetime.now() - timedelta(hours=value)
    elif period == 'days':
        cutoff_time = datetime.now() - timedelta(days=value)
    else:
        return jsonify({"error": "Invalid period"}), 400

    conn = get_db_connection()
    tickets = conn.execute('SELECT * FROM tickets WHERE status != ? AND opening_date >= ?',
                           ('closed', cutoff_time)).fetchall()
    conn.close()

    result = {"open_tickets": len(tickets)}
    return jsonify(result)


if __name__ == '__main__':
    app.run(port=5001)