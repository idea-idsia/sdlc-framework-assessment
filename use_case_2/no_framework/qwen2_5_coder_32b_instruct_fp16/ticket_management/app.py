from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/tickets', methods=['GET', 'POST'])
def user_tickets():
    if request.method == 'POST':
        description = request.form['description']
        category = request.form['category']

        conn = get_db_connection()
        conn.execute('INSERT INTO tickets (description, category, status) VALUES (?, ?, ?)',
                     (description, category, 'open'))
        conn.commit()
        conn.close()

    conn = get_db_connection()
    tickets = conn.execute('SELECT * FROM tickets WHERE status IN ("open", "active")').fetchall()
    conn.close()

    return render_template('ticket_form.html', tickets=tickets)


@app.route('/helpdesk/tickets', methods=['GET', 'POST'])
def helpdesk_tickets():
    if request.method == 'POST':
        ticket_id = request.form['ticket_id']
        new_status = request.form['new_status']

        conn = get_db_connection()
        conn.execute('UPDATE tickets SET status = ? WHERE id = ?', (new_status, ticket_id))
        conn.commit()
        conn.close()

    conn = get_db_connection()
    tickets = conn.execute('SELECT * FROM tickets').fetchall()
    conn.close()

    return render_template('ticket_detail.html', tickets=tickets)


if __name__ == '__main__':
    app.run(debug=True)