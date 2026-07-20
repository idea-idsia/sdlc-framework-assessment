# Import necessary libraries
from flask import Flask, jsonify, request
from db_manager import DBManager
from ticket_manager import TicketManager
from microservices import Service1, Service2, Service3
'''
This is the main application file.
It initializes the database and ticket manager,
and defines routes for micro-services.
'''
app = Flask(__name__)
# Initialize database and ticket manager
db_manager = DBManager()
ticket_manager = TicketManager(db_manager)
# Define routes for micro-services
@app.route('/service1', methods=['GET'])
def service1():
    """Service 1: Display the number of tickets opened in the selected period."""
    period = request.args.get('period')
    service1 = Service1(db_manager)
    result = service1.get_tickets(period)
    return jsonify(result)
@app.route('/service2', methods=['GET'])
def service2():
    """Service 2: Average ticket resolution time, displayed by the opening month."""
    service2 = Service2(db_manager)
    result = service2.get_average_resolution_time()
    return jsonify(result)
@app.route('/service3', methods=['GET'])
def service3():
    """Service 3: Cluster the tickets by ticket category and display number of active tickets per category."""
    service3 = Service3(db_manager)
    result = service3.get_category_clusters()
    return jsonify(result)
if __name__ == "__main__":
    app.run(debug=True)