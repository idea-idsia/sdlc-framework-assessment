from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/service2', methods=['GET'])
def service2():
    conn = get_db_connection()
    tickets = conn.execute('SELECT opening_date, closing_date FROM tickets WHERE status = ?',
                           ('closed',)).fetchall()
    conn.close()

    from collections import defaultdict
    resolution_times_by_month = defaultdict(float)
    count_by_month = defaultdict(int)

    for ticket in tickets:
        open_time = datetime.strptime(ticket['opening_date'], '%Y-%m-%d %H:%M:%S')
        close_time = datetime.strptime(ticket['closing_date'], '%Y-%m-%d %H:%M:%S')
        resolution_time = (close_time - open_time).total_seconds() / 3600.0
        month_key = open_time.strftime('%Y-%m')

        resolution_times_by_month[month_key] += resolution_time
        count_by_month[month_key] += 1

    result = {}
    for month in resolution_times_by_month:
        avg_resolution_time = resolution_times_by_month[month] / count_by_month[month]
        result[month] = avg_resolution_time

    return jsonify(result)


if __name__ == '__main__':
    app.run(port=5002)