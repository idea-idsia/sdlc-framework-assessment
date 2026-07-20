from flask import Flask, request, jsonify
from database import get_session
from models import Ticket

app = Flask(__name__)

@app.route('/tickets', methods=['GET'])
def get_active_tickets_by_category():
    session = get_session()
    tickets = session.query(Ticket).filter_by(status='open').all()
    # Group by category logic here
    return jsonify([{'category': category, 'count': count} for category, count in categories])

if __name__ == '__main__':
    app.run(debug=True)
