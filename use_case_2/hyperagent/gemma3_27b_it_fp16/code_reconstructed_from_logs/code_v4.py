import sqlite3
from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

DATABASE = 'tickets.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/tickets/create', methods=['GET', 'POST'])
def create_ticket():
    if request.method == 'POST':
        conn = get_db_connection()
        description = request.form['description']
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn.execute("INSERT INTO tickets (description, status, opening_date, last_modification_date) VALUES (?, ?, ?, ?)",
                     (description, 'open', now, now))
        conn.commit()
        conn.close()
        return redirect(url_for('list_tickets'))
    return render_template('create.html')

@app.route('/tickets/<int:ticket_id>')
def view_ticket(ticket_id):
    conn = get_db_connection()
    ticket = conn.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
    conn.close()
    return render_template('ticket.html', ticket=ticket)

@app.route('/tickets/<int:ticket_id>/edit', methods=['GET', 'POST'])
def edit_ticket(ticket_id):
    conn = get_db_connection()
    if request.method == 'POST':
        description = request.form['description']
        status = request.form['status']
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn.execute("UPDATE tickets SET description = ?, status = ?, last_modification_date = ? WHERE id = ?",
                     (description, status, now, ticket_id))
        conn.commit()
        conn.close()
        return redirect(url_for('view_ticket', ticket_id=ticket_id))
    ticket = conn.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
    conn.close()
    return render_template('edit.html', ticket=ticket)

@app.route('/tickets')
def list_tickets():
    conn = get_db_connection()
    tickets = conn.execute("SELECT * FROM tickets").fetchall()
    conn.close()
    return render_template('tickets.html', tickets=tickets)

if __name__ == '__main__':
    app.run(debug=True)