from flask import Flask, request, jsonify
from app import db

app = Flask(__name__)

@app.route('/tickets/over/time', methods=['POST'])
def tickets_over_time():
    data = request.get_json()
    period = data['period']  # X hours/days
    # Query database for tickets within the specified period that haven't been closed
    tickets = Ticket.query.filter(Ticket.status != 'closed', Ticket.opened >= datetime.now() - timedelta(**period)).all()
    return jsonify({'tickets': len(tickets)})