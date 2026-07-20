from flask import Flask, request, jsonify
from database import TicketDatabase

app = Flask(__name__)
db = TicketDatabase("tickets.db")

@app.route("/api/tickets", methods=["GET"])
def get_tickets():
    status = request.args.get("status")
    tickets = db.get_tickets(status)
    return jsonify([{"id": ticket[0], "status": ticket[1], "description": ticket[2]} for ticket in tickets])

@app.route("/api/tickets/<int:ticket_id>/status", methods=["PUT"])
def update_ticket_status(ticket_id):
    status = request.json["status"]
    db.update_ticket_status(ticket_id, status)
    return jsonify({"message": "Ticket status updated"})

@app.route("/api/tickets/<int:ticket_id>/messages", methods=["GET"])
def get_messages(ticket_id):
    messages = db.cursor.execute("SELECT * FROM messages WHERE ticket_id = ?", (ticket_id,)).fetchall()
    return jsonify([{"id": message[0], "message": message[2]} for message in messages])

@app.route("/api/tickets/<int:ticket_id>/messages", methods=["POST"])
def insert_message(ticket_id):
    message = request.json["message"]
    sender = request.json["sender"]
    db.insert_message(ticket_id, message, sender)
    return jsonify({"message": "Message inserted"})

if __name__ == "__main__":
    app.run(debug=True)