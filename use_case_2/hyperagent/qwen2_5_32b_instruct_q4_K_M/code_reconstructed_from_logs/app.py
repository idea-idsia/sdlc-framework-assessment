from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Mock database for demonstration purposes
tickets_db = [
    {"id": 1, "category": "Support", "opened_date": "2023-01-05", "closed_date": None},
    {"id": 2, "category": "Bug", "opened_date": "2023-02-10", "closed_date": "2023-02-15"},
    # Add more tickets as needed
]

@app.route('/tickets/opened', methods=['GET'])
def get_open_tickets():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not start_date or not end_date:
        return jsonify({"error": "Missing date parameters"}), 400

    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

    open_tickets_count = sum(
        1 for ticket in tickets_db
        if (start_date <= datetime.datetime.strptime(ticket['opened_date'], '%Y-%m-%d').date() <= end_date)
           and not ticket['closed_date']
    )

    return jsonify({"open_ticket_count": open_tickets_count})

@app.route('/tickets/average_resolution_time', methods=['GET'])
def get_average_resolution_time():
    month = request.args.get('month')

    if not month:
        return jsonify({"error": "Missing month parameter"}), 400

    tickets_in_month = [
        ticket for ticket in tickets_db
        if datetime.datetime.strptime(ticket['opened_date'], '%Y-%m-%d').date().strftime('%B') == month.capitalize()
           and ticket['closed_date']
    ]

    total_days = sum(
        (datetime.datetime.strptime(ticket['closed_date'], '%Y-%m-%d').date() -
         datetime.datetime.strptime(ticket['opened_date'], '%Y-%m-%d').date()).days
        for ticket in tickets_in_month
    )

    average_time = total_days / len(tickets_in_month) if tickets_in_month else 0

    return jsonify({"average_resolution_time": average_time})

@app.route('/tickets/active_by_category', methods=['GET'])
def get_active_tickets_by_category():
    active_tickets_per_category = {}

    for ticket in tickets_db:
        category = ticket['category']
        if not ticket['closed_date']:
            if category not in active_tickets_per_category:
                active_tickets_per_category[category] = 0
            active_tickets_per_category[category] += 1

    return jsonify(active_tickets_per_category)

if __name__ == '__main__':
    app.run(debug=True)