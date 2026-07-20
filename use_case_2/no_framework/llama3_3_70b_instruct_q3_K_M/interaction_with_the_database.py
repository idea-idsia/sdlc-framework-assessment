from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route('/tickets', methods=['GET'])
def get_tickets():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()
    return jsonify({"tickets": tickets})

@app.route('/tickets', methods=['POST'])
def insert_ticket():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    data = request.get_json()
    cursor.execute("INSERT INTO tickets (category, description) VALUES (?, ?)", (data['category'], data['description']))
    conn.commit()
    return jsonify({"message": "Ticket inserted successfully"})

@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,))
    ticket = cursor.fetchone()
    return jsonify({"ticket": ticket})

@app.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    data = request.get_json()
    cursor.execute("UPDATE tickets SET category = ?, description = ? WHERE id = ?", (data['category'], data['description'], ticket_id))
    conn.commit()
    return jsonify({"message": "Ticket updated successfully"})

if __name__ == '__main__':
    app.run(debug=True)