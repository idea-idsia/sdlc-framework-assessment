from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/api/tickets', methods=['GET'])
def get_tickets():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tickets WHERE status IN ("open", "active")')
    tickets = cursor.fetchall()

    conn.close()

    return jsonify(tickets)

@app.route('/api/ticket/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tickets WHERE id = ?', (ticket_id,))
    ticket = cursor.fetchone()

    conn.close()

    return jsonify({'title': ticket[1], 'description': ticket[2]})

if __name__ == '__main__':
    app.run(debug=True)