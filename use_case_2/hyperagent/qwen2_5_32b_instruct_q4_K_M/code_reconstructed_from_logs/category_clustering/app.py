from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for demonstration purposes
tickets_db = [
    {"id": 1, "category": "Support", "opened_date": "2023-01-05", "closed_date": None},
    {"id": 2, "category": "Bug", "opened_date": "2023-02-10", "closed_date": "2023-02-15"},
    # Add more tickets as needed
]

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
    app.run(debug=True, port=5003)