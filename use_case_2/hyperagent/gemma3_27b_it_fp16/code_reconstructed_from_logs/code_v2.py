import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

DATABASE = 'tickets.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/tickets/create', methods=['POST'])
def create_ticket():
    conn = get_db_connection()
    description = request.form['description']
    conn.execute("INSERT INTO tickets (description, status, opening_date, last_modification_date) VALUES (?, ?, ?, ?)",
                 (description, 'open', 'now', 'now'))
    conn.commit()
    conn.close()
    return redirect(url_for('list_tickets'))

@app.route('/tickets/<int:ticket_id>')
def view_ticket(ticket_id):
    conn = get_db_connection()
    ticket = conn.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
    conn.close()
    return render_template('ticket.html', ticket=ticket)

@app.route('/tickets/<int:ticket_id>/edit', methods=['POST'])
def edit_ticket(ticket_id):
    conn = get_db_connection()
    description = request.form['description']
    status = request.form['status']
    conn.execute("UPDATE tickets SET description = ?, status = ?, last_modification_date = 'now' WHERE id = ?",
                 (description, status, ticket_id))
    conn.commit()
    conn.close()
    return redirect(url_for('view_ticket', ticket_id=ticket_id))

@app.route('/tickets')
def list_tickets():
    conn = get_db_connection()
    tickets = conn.execute("SELECT * FROM tickets").fetchall()
    conn.close()
    return render_template('tickets.html', tickets=tickets)

if __name__ == '__main__':
    app.run(debug=True)