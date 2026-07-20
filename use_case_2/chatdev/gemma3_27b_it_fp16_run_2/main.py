'''
API for providing data visualization and analysis functionalities.
Uses Flask to create API endpoints.
'''
from flask import Flask, jsonify, request
from database_manager import DatabaseManager
import datetime
app = Flask(__name__)
db_manager = DatabaseManager("tickets.db")
@app.route('/api/tickets/period', methods=['GET'])
def get_tickets_in_period():
    """
    Returns the number of tickets opened in a specific period that haven't been closed.
    """
    period = request.args.get('period')
    if period:
        try:
            hours = int(period)
            end_date = datetime.datetime.now().isoformat()
            start_date = (datetime.datetime.now() - datetime.timedelta(hours=hours)).isoformat()
            tickets = db_manager.get_tickets()
            filtered_tickets = [ticket for ticket in tickets if ticket['status'] != 'closed' and start_date <= ticket['opening_date'] <= end_date]
            return jsonify({'count': len(filtered_tickets)})
        except ValueError:
            return jsonify({'error': 'Invalid period format.  Must be an integer (hours).'}), 400
    else:
        return jsonify({'error': 'Period is required.'}), 400
@app.route('/api/tickets/resolution_time', methods=['GET'])
def get_average_resolution_time():
    """
    Returns the average ticket resolution time by opening month.
    """
    tickets = db_manager.get_tickets()
    resolution_times = {}
    for ticket in tickets:
        if ticket['status'] == 'closed':
            try:
                opening_date = datetime.datetime.fromisoformat(ticket['opening_date'])
                closing_date = datetime.datetime.fromisoformat(ticket['closing_date'])
                month = opening_date.month
                resolution_time = (closing_date - opening_date).total_seconds() / 3600
                if month not in resolution_times:
                    resolution_times[month] = []
                resolution_times[month].append(resolution_time)
            except ValueError as e:
                print(f"Error parsing date: {e}")  # Log the error
                continue  # Skip to the next ticket
    average_resolution_times = {}
    for month, times in resolution_times.items():
        if times: #avoid division by zero
            average_resolution_times[month] = sum(times) / len(times)
    return jsonify(average_resolution_times)
@app.route('/api/tickets/category', methods=['GET'])
def get_active_tickets_by_category():
    """
    Returns the number of active tickets per category.
    """
    tickets = db_manager.get_tickets()
    category_counts = {}
    for ticket in tickets:
        if ticket['status'] == 'active':
            category = ticket['category']
            if category not in category_counts:
                category_counts[category] = 0
            category_counts[category] += 1
    return jsonify(category_counts)
if __name__ == '__main__':
    app.run(debug=True)