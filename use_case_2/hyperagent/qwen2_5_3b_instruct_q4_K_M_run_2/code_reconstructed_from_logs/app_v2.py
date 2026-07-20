from flask import Flask, request, jsonify

app = Flask(__name__)

# Database connection setup (using SQLite in this example)
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create 'tickets' table if not exists
create_tickets_table_sql = """
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category TEXT NOT NULL,
    description TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'open',
    opening_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_modified_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    closing_date TIMESTAMP
);
"""
c.execute(create_tickets_table_sql)
conn.commit()

@app.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.json
    c.execute("""
        INSERT INTO tickets (user_id, category, description) VALUES (?, ?, ?)
    """, (data['user_id'], data['category'], data['description']))
    conn.commit()
    return jsonify({"message": "Ticket created successfully"}), 201

@app.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    c.execute("""
        UPDATE tickets
        SET status = ?, last_modified_date = CURRENT_TIMESTAMP
        WHERE id = ?
    """, ('closed', ticket_id))
    conn.commit()
    return jsonify({"message": "Ticket updated successfully"})

@app.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    c.execute("""
        DELETE FROM tickets
        WHERE id = ?
    """, (ticket_id,))
    conn.commit()
    return jsonify({"message": "Ticket deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)