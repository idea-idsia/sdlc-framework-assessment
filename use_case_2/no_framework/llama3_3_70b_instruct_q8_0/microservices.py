from flask import Flask, jsonify, request
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

# Service 1: Display number of open tickets in last X hours/days
@app.route("/tickets/open", methods=["GET"])
def get_open_tickets():
    period = request.args.get("period")
    if period.endswith("hours"):
        period = int(period[:-6])
        start_date = datetime.now() - timedelta(hours=period)
    elif period.endswith("days"):
        period = int(period[:-5])
        start_date = datetime.now() - timedelta(days=period)
    else:
        return jsonify({"error": "Invalid period"}), 400

    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM tickets WHERE opening_date >= ? AND status = 'open'", (start_date,))
    count = cursor.fetchone()[0]
    conn.close()
    return jsonify({"count": count})

# Service 2: Display average ticket resolution time by month
@app.route("/tickets/average-resolution-time", methods=["GET"])
def get_average_resolution_time():
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute("SELECT opening_date, closing_date FROM tickets WHERE status = 'closed'")
    tickets = cursor.fetchall()
    resolution_times = {}
    for ticket in tickets:
        opening_date = datetime.strptime(ticket[0], "%Y-%m-%d")
        closing_date = datetime.strptime(ticket[1], "%Y-%m-%d")
        resolution_time = (closing_date - opening_date).days
        month = opening_date.strftime("%Y-%m")
        if month not in resolution_times:
            resolution_times[month] = []
        resolution_times[month].append(resolution_time)

    average_resolution_times = {}
    for month, times in resolution_times.items():
        average_resolution_times[month] = sum(times) / len(times)

    conn.close()
    return jsonify(average_resolution_times)

# Service 3: Display number of active tickets per category
@app.route("/tickets/active", methods=["GET"])
def get_active_tickets():
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category, COUNT(*) FROM tickets WHERE status = 'active' GROUP BY category")
    categories = cursor.fetchall()
    active_tickets = {}
    for category in categories:
        active_tickets[category[0]] = category[1]
    conn.close()
    return jsonify(active_tickets)

if __name__ == "__main__":
    app.run(debug=True)