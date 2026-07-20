from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

@app.route('/tickets/open-count', methods=['POST'])
def open_tickets_count():
    start_date_str = request.json.get('start_date')
    end_date_str = request.json.get('end_date')

    if not (start_date_str and end_date_str):
        return jsonify({"error": "Invalid date format"}), 400

    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()

    count = db.session.query(Ticket).filter(
        Ticket.status == TicketStatus.OPEN,
        Ticket.opening_date.between(start_date, end_date)
    ).count()

    return jsonify({"open_tickets_count": count}), 200