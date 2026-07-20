from flask import Flask, request, jsonify

app_service1 = Flask(__name__)
@app_service1.route('/tickets/recent', methods=['GET'])
def recent_tickets():
    period = request.args.get('period')  # e.g., 'last_hour' or 'last_day'
    tickets = Ticket.query.filter(Ticket.status != 'closed').all()
    return jsonify([ticket.__dict__ for ticket in tickets])

app_service2 = Flask(__name__)
@app_service2.route('/tickets/average_resolution', methods=['GET'])
def average_resolution():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    tickets = Ticket.query.filter(Ticket.created_at >= start_date, Ticket.created_at <= end_date).all()
    # Calculate average resolution time (simplified)
    return jsonify({"average_resolution": "calculated"})

app_service3 = Flask(__name__)
@app_service3.route('/tickets/category', methods=['GET'])
def category_stats():
    tickets = Ticket.query.all()
    categories = {}
    for ticket in tickets:
        if ticket.category not in categories:
            categories[ticket.category] = 0
        categories[ticket.category] += 1
    return jsonify(categories)