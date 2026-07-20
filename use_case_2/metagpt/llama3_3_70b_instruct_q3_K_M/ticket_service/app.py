from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Ticket, HelpDeskStaff, TicketManager
from routes import report_issue, view_tickets, exchange_messages, update_status

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/help_desk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create a TicketManager instance
ticket_manager = TicketManager()

# Define routes
@app.route('/report-issue', methods=['POST'])
def report_issue_route():
    """Report a new issue"""
    data = request.get_json()
    if 'title' not in data or 'description' not in data or 'user_id' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    title = data['title']
    description = data['description']
    user_id = data['user_id']
    
    # Validate user
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    try:
        result = report_issue(title, description, user_id)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/view-tickets', methods=['GET'])
def view_tickets_route():
    """View all tickets"""
    # Authenticate staff
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'error': 'Authentication required'}), 401
    
    staff_id = authenticate_staff(auth_header)
    if not staff_id:
        return jsonify({'error': 'Invalid authentication'}), 401
    
    try:
        result = view_tickets()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/exchange-messages', methods=['POST'])
def exchange_messages_route():
    """Exchange messages for a ticket"""
    data = request.get_json()
    if 'ticket_id' not in data or 'message' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    ticket_id = data['ticket_id']
    message = data['message']
    
    # Validate ticket
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        return jsonify({'error': 'Ticket not found'}), 404
    
    try:
        result = exchange_messages(ticket_id, message)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/update-status', methods=['POST'])
def update_status_route():
    """Update the status of a ticket"""
    data = request.get_json()
    if 'ticket_id' not in data or 'status' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    ticket_id = data['ticket_id']
    status = data['status']
    
    # Validate ticket
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        return jsonify({'error': 'Ticket not found'}), 404
    
    try:
        result = update_status(ticket_id, status)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def authenticate_staff(auth_header):
    # Implement authentication logic here
    # For demonstration purposes, assume a valid token is provided
    staff_id = 1  # Replace with actual staff ID retrieval logic
    return staff_id

if __name__ == '__main__':
    app.run(debug=True)
