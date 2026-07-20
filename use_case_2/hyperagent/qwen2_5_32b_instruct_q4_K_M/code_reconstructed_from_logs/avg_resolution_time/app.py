from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Mock database for demonstration purposes
tickets_db = [
    {"id": 1, "category": "Support", "opened_date": "2023-01-05", "closed_date": None},
    {"id": 2, "category": "Bug", "opened_date": "2023-02-10", "closed_date": "2023-02-15"},
    # Add more tickets as needed
]

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

if __name__ == '__main__':
    app.run(debug=True, port=5002)