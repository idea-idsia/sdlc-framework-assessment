from flask import Flask, request, jsonify
from database import get_session
from models import Ticket

app = Flask(__name__)

@app.route('/tickets', methods=['GET'])
def get_average_resolution_time():
    session = get_session()
    tickets = session.query(Ticket).all()
    # Calculate average resolution time logic here
    return jsonify({'message': 'Average resolution time calculated'})

if __name__ == '__main__':
    app.run(debug=True)
