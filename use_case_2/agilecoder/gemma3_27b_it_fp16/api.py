'''
API endpoint for retrieving ticket data in JSON format.
'''
from flask import Flask, jsonify, request
import logging
logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
app = Flask(__name__)
class TicketAPI:
    def __init__(self, db):
        self.db = db
    @app.route('/api/tickets', methods=['GET'])
    def get_tickets(self):
        try:
            user_role = request.args.get('role', 'user')
            tickets = self.db.get_tickets(user_role)
            ticket_list = []
            for ticket in tickets:
                ticket_dict = {
                    'id': ticket[0],
                    'status': ticket[1],
                    'description': ticket[2],
                    'category': ticket[3],
                    'opening_date': ticket[4],
                    'last_modification_date': ticket[5],
                    'closing_date': ticket[6]
                }
                ticket_list.append(ticket_dict)
            return jsonify(ticket_list)
        except Exception as e:
            logging.error(f"Error retrieving tickets via API: {e}")
            print(f"Error retrieving tickets via API: {e}")
            return jsonify({"error": str(e)}), 500