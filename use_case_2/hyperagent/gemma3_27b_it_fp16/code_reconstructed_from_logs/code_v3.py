from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = 'tickets.db'  # Assuming your database file is named tickets.db

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn

# 1. /tickets/create
@app.route('/tickets/create', methods=['GET', 'POST'])
def create_ticket():
    if request.method == 'POST':
        description = request.form['description']
        conn = get_db_connection()
        now = datetime.now()
        conn.execute("INSERT INTO tickets (description, opening_date, last_modification_date, status) VALUES (?, ?, ?, ?)",
                     (description, now, now, 'open'))
        conn.commit()
        conn.close()
        return redirect(url_for('list_tickets'))  # Redirect to a list view (you'll need to implement this)
    return render_template('create_ticket.html') # You'll need to create this template

# 2. /tickets/<int:ticket_id>
@app.route('/tickets/<int:ticket_id>')
def view_ticket(ticket_id):
    conn = get_db_connection()
    ticket = conn.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
    conn.close()
    if ticket:
        return render_template('view_ticket.html', ticket=ticket) # You'll need to create this template
    else:
        return "Ticket not found" # Basic error message

# 3. /tickets/<int:ticket_id>/edit
@app.route('/tickets/<int:ticket_id>/edit', methods=['GET', 'POST'])
def edit_ticket(ticket_id):
    conn = get_db_connection()
    ticket = conn.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
    conn.close()

    if not ticket:
        return "Ticket not found"

    if request.method == 'POST':
        description = request.form['description']
        status = request.form['status']
        now = datetime.now()
        conn = get_db_connection()
        conn.execute("UPDATE tickets SET description = ?, status = ?, last_modification_date = ? WHERE id = ?",
                     (description, status, now, ticket_id))
        conn.commit()
        conn.close()
        return redirect(url_for('view_ticket', ticket_id=ticket_id))
    return render_template('edit_ticket.html', ticket=ticket) # You'll need to create this template

# Example route for listing tickets (you'll need to implement this)
@app.route('/tickets')
def list_tickets():
    conn = get_db_connection()
    tickets = conn.execute("SELECT * FROM tickets").fetchall()
    conn.close()
    return render_template('list_tickets.html', tickets=tickets)

if __name__ == '__main__':
    app.run(debug=True)