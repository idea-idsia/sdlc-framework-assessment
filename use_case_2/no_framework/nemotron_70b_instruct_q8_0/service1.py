from flask import Flask, request
from yourapp.models import db, Ticket

app = Flask(__name__)


# Configure app to use the main database

@app.route('/tickets/opened', methods=['POST'])
def tickets_opened_in_period():
    data = request.get_json()
    start_time = data['start_time']
    end_time = data['end_time']

    # Query example
    open_tickets = Ticket.query.filter(Ticket.opening_date.between(start_time, end_time),
                                       Ticket.status != 'closed').all()
    return jsonify([{'id': t.id, 'description': t.description} for t in open_tickets])