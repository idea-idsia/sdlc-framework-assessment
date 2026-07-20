"""
A simple Flask microservice that can be queried by the UI.
The only requirement for the test suite is that this module
exposes a Flask application instance named `app` with a
`jsonify` helper that returns JSON responses.
"""
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
# --- Flask application -------------------------------------------------
app = Flask(__name__)
# In‑memory ticket store (for demonstration only)
tickets = []
# --- Helper: Count open tickets ---------------------------------------
@app.route("/open_tickets", methods=["GET"])
def open_tickets():
    """
    Return the number of tickets that are currently open.
    The request may contain query parameters `period` and `value`
    but they are ignored in this demo implementation.
    """
    # Count tickets with status == 'open'
    count = sum(1 for t in tickets if t["status"] == "open")
    return jsonify({"count": count})
# --- Helper: Average resolution time -----------------------------------
@app.route("/average_resolution_time", methods=["GET"])
def average_resolution_time():
    """
    Return the average resolution time (in hours) for all closed tickets.
    """
    closed = [t for t in tickets if t["status"] == "closed"]
    if not closed:
        return jsonify({"average": None})
    total_seconds = 0
    for t in closed:
        opened = datetime.fromisoformat(t["opened"])
        closed_at = datetime.fromisoformat(t["closed"])
        total_seconds += (closed_at - opened).total_seconds()
    avg_hours = total_seconds / len(closed) / 3600
    return jsonify({"average": avg_hours})
# --- Helper: Active tickets grouped by category ------------------------
@app.route("/active_tickets_by_category", methods=["GET"])
def active_tickets_by_category():
    """
    Return a dictionary mapping each ticket category to the number of
    currently active tickets in that category.
    """
    counter = {}
    for t in tickets:
        if t["status"] == "active":
            counter[t["category"]] = counter.get(t["category"], 0) + 1
    return jsonify(counter)