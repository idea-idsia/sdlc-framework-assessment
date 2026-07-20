from flask import Flask, request, jsonify
import sqlite3
import datetime

app = Flask(__name__)

# Connect to SQLite database
conn = sqlite3.connect('database.db')
c = conn.cursor()


@app.route('/ticket_analysis_service_1', methods=['POST'])
def ticket_analysis_by_period():
    data = request.json
    start_time = datetime.datetime.strptime(data['start_time'], '%Y-%m-%d %H:%M:%S')
    end_time = datetime.datetime.strptime(data['end_time'], '%Y-%m-%d %H:%M:%S')

    c.execute("""
              SELECT COUNT(*)
              FROM tickets
              WHERE opening_date >= ?
                AND closing_date IS NULL
              """, (start_time,))

    total_open_tickets = c.fetchone()[0]

    return jsonify({"total_open_tickets": total_open_tickets})


if __name__ == '__main__':
    app.run(debug=True)