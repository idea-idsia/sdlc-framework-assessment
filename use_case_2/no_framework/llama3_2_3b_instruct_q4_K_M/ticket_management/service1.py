from flask import Flask, request, jsonify
from database import get_session
from models import Ticket

app = Flask(__name__)

@app.route('/tickets', methods=['GET'])
def get_tickets():
    session = get_session()
    tickets = session.query(Ticket).filter_by(status='open').all()
    return jsonify([{'id': ticket.id, 'title': ticket.title} for ticket in tickets])

@app.route('/tickets/<int:ticket_id>', methods=['POST'])
def update_ticket(ticket_id):
    session = get_session()
    ticket = session.query(Ticket).get(ticket_id)
    # Update logic here
    return jsonify({'message': 'Ticket updated'})

if __name__ == '__main__':
    app.run(debug=True)
