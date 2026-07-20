from flask import Flask, request, jsonify
import sqlite3
from datetime import timedelta

app = Flask(__name__)

# Connect to SQLite database
conn = sqlite3.connect('database.db')
c = conn.cursor()


@app.route('/ticket_analysis_service_2', methods=['POST'])
def average_ticket_resolution_time():
    c.execute("""
              SELECT strftime('%Y-%m', opening_date),
                     AVG(datediff(closing_date, opening_date))
              FROM tickets
              WHERE closing_date IS NOT NULL
              GROUP BY strftime('%Y-%m', opening_date)
              """)

    results = c.fetchall()

    return jsonify({"results": results})


def datediff(date1_str, date2_str):
    date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d %H:%M:%S')
    date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d %H:%M:%S')
    return abs((date1 - date2).days)


if __name__ == '__main__':
    app.run(debug=True)