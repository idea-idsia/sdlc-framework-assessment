from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/api/tickets/open', methods=['GET'])
def get_open_tickets():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM tickets WHERE status IN ("open", "active") AND opening_date >= DATE("now", "-1 day")')
    open_tickets = cursor.fetchone()[0]

    conn.close()

    return jsonify({'num_open_tickets': open_tickets})

@app.route('/api/tickets/resolution_time', methods=['GET'])
def get_resolution_time():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute('SELECT AVG(CASE WHEN status = "closed" THEN closing_date - opening_date ELSE NULL END) FROM tickets WHERE status IN ("open", "active")')
    resolution_time = cursor.fetchone()[0]

    conn.close()

    return jsonify({'resolution_time': resolution_time})

@app.route('/api/tickets/active_by_category', methods=['GET'])
def get_active_by_category():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM tickets WHERE status IN ("open", "active") GROUP BY category HAVING COUNT(*) > 1')
    active_by_category = cursor.fetchall()

    conn.close()

    return jsonify(active_by_category)

if __name__ == '__main__':
    app.run(debug=True)