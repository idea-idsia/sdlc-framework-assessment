from flask import Flask, request, jsonify
import json
app = Flask(__name__)
@app.route('/tickets', methods=['GET'])
def get_tickets():
    # In-memory database for simplicity; replace with actual database in production.
    tickets_db = {
        1: {"id": 1, "status": 'Open', "category": 'Facility Management', "description": '', "opened_date": '2023-04-05', "closed_date": None},
        # add more tickets...
    }
    selected_period = request.args.get('period')
    start_time_str = request.args.get('start') or '2023-01-01 00:00:00'
    end_time_str = request.args.get('end') or '2023-04-05 23:59:59'
    start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
    if selected_period:
        time_range = int(selected_period)
    else: # for default, show tickets in the last 24 hours
        time_range = (datetime.now() - start_time).days + 1
    active_tickets = list(filter(lambda ticket: datetime.strptime(ticket['opened_date'], '%Y-%m-%d') < end_time and datetime.strptime(ticket['closed_date'] or '2050-01-01', '%Y-%m-%d') > start_time, tickets_db.values()))
    return jsonify({'active_tickets': active_tickets})
@app.route('/tickets/stats/<int:ticket_id>', methods=['GET'])
def get_stats_by_ticket(ticket_id):
    stats = helpdesk_management_logic.get_opened_tickets()
    for i in range(len(stats)):
        if ticket_id == int(stats[i]['id']):
            ticket_info = {
                'category': stats[i]['category'],
                'count': 1
            }
            break
    else:
        # If the specified ticket ID is not found, add a new entry with count set to zero.
        ticket_info = {'category': str(ticket_id), 'count': 0}
    return jsonify(stats=[ticket_info])
@app.route('/tickets/cluster_by_category', methods=['GET'])
def cluster_tickets():
    stats_by_categories = {}
    for ticket in helpdesk_management_logic.get_opened_tickets():
        category = ticket['category']
        if not stats_by_categories.get(category):
            stats_by_categories[category] = 1
        else:
            stats_by_categories[category] += 1
    return jsonify(stats=stats_by_categories)