from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3
from config import SQLALCHEMY_DATABASE_URI  # We need to set up the database connection

app = Flask(__name__)

# We'll use the same SQLite database as the main app
DATABASE = 'tickets.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/period/<int:hours>', methods=['GET'])
def period_tickets(hours):
    # Calculate the time period
    period_start = datetime.utcnow() - datetime.timedelta(hours=hours)
    period_end = datetime.utcnow()

    # Query the database for tickets opened in the period that are not closed
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM Ticket
        WHERE created_at >= ? AND status != 'closed'
    """, (period_start,))
    tickets = cursor.fetchall()
    conn.close()

    return jsonify({'tickets': [dict(ticket) for ticket in tickets]})

@app.route('/api/period/<int:days>', methods=['GET'])
def period_tickets_days(days):
    period_start = datetime.utcnow() - datetime.timedelta(days=days)
    period_end = datetime.utcnow()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM Ticket
        WHERE created_at >= ? AND status != 'closed'
    """, (period_start,))
    tickets = cursor.fetchall()
    conn.close()

    return jsonify({'tickets': [dict(ticket) for ticket in tickets]})

# We can add more endpoints as needed

if __name__ == '__main__':
    app.run(debug=True)