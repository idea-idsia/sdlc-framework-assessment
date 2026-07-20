'''
microservices_api.py
This file contains the API functions for the microservices architecture.
'''
import requests
from flask import Flask, jsonify, request
from constants import CATEGORY_CHOICES
app = Flask(__name__)
@app.route("/tickets", methods=["GET"])
def get_tickets():
    # Get all tickets in the database
    query = "SELECT id, description, category FROM tickets"
    results = app.conn.cursor().execute(query).fetchall()
    return jsonify({"tickets": [{"id": ticket[0], "description": ticket[1], "category": CATEGORY_CHOICES[ticket[2]]} for ticket in results]})
@app.route("/tickets/<int:ticket_id>", methods=["GET"])
def get_ticket(ticket_id):
    # Get a specific ticket from the database
    query = "SELECT id, description, category FROM tickets WHERE id=?"
    results = app.conn.cursor().execute(query, (ticket_id,)).fetchone()
    if not results:
        return jsonify({"error": "Ticket does not exist"}), 404
    else:
        return jsonify({"id": ticket[0], "description": ticket[1], "category": CATEGORY_CHOICES[ticket[2]]})
@app.route("/tickets", methods=["POST"])
def create_ticket():
    # Create a new ticket in the database
    description = request.form["description"]
    category = request.form["category"]
    query = "INSERT INTO tickets (description, category) VALUES (?, ?)"
    app.conn.cursor().execute(query, (description, category))
    app.conn.commit()
    return jsonify({"message": "Ticket created successfully"}), 201
@app.route("/tickets/<int:ticket_id>", methods=["PUT"])
def update_ticket(ticket_id):
    # Update a specific ticket in the database
    description = request.form["description"]
    category = request.form["category"]
    query = "UPDATE tickets SET description=?, category=? WHERE id=?"
    app.conn.cursor().execute(query, (description, category, ticket_id))
    app.conn.commit()
    return jsonify({"message": "Ticket updated successfully"}), 200
@app.route("/tickets/<int:ticket_id>", methods=["DELETE"])
def delete_ticket(ticket_id):
    # Delete a specific ticket from the database
    query = "DELETE FROM tickets WHERE id=?"
    app.conn.cursor().execute(query, (ticket_id,))
    app.conn.commit()
    return jsonify({"message": "Ticket deleted successfully"}), 200