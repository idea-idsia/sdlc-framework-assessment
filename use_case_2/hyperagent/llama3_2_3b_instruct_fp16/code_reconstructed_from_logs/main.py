from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Create a database to store ticket data
tickets_db = pd.DataFrame({
    "id": [1, 2, 3],
    "status": ["open", "active", "closed"],
    "description": ["Ticket 1", "Ticket 2", "Ticket 3"]
})

@app.route("/get_tickets", methods=["GET"])
def get_tickets():
    # Get the number of open tickets in the last X hours
    x_hours = int(request.args.get("x_hours"))
    open_tickets = tickets_db[tickets_db["status"] == "open"][tickets_db["created_at"].dt.date - pd.Timestamp.now().date()] <= x_hours
    return jsonify({"count": len(open_tickets)})


@app.route("/get_average_resolution_time", methods=["GET"])
def get_average_resolution_time():
    # Get the average resolution time by month
    monthlyResolutionTime = tickets_db[tickets_db["status"] == "closed"].groupby(tickets_db["created_at"].dt.month)["resolution_time"].mean()
    return jsonify({"average": monthlyResolutionTime.mean()})


@app.route("/get_tickets_by_category", methods=["GET"])
def get_tickets_by_category():
    # Get the number of active tickets per category
    categories = tickets_db[tickets_db["status"] == "active"]["category"].unique()
    active_tickets_per_category = [len(tickets_db[(tickets_db["status"] == "active") & (tickets_db["category"] == category)]) for category in categories]
    return jsonify({"categories": [{"category": category, "count": count} for category, count in zip(categories, active_tickets_per_category)]})

if __name__ == "__main__":
    app.run(debug=True)