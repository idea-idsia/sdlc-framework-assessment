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

if __name__ == '__main__':
    app.run(debug=True, port=5001)