from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
import os
import pdfkit

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In a real application, you would use a database. Here we use a simple list.
tickets = []
users = [
    {"username": "user", "password": "password", "role": "user"},
    {"username": "helpdesk", "password": "password", "role": "helpdesk"}
]

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = None
        for u in users:
            if u['username'] == username and u['password'] == password:
                user = u
                break
        if user:
            session['user'] = user
            if user['role'] == 'user':
                return redirect(url_for('user_dashboard'))
            else:
                return redirect(url_for('helpdesk_dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/user_dashboard')
def user_dashboard():
    if 'user' not in session or session['user']['role'] != 'user':
        return redirect(url_for('index'))
    # Fetch user's tickets
    user_tickets = [t for t in tickets if t['submitter'] == session['user']['username']]
    return render_template('user_dashboard.html', tickets=user_tickets)

@app.route('/helpdesk_dashboard')
def helpdesk_dashboard():
    if 'user' not in session or session['user']['role'] != 'helpdesk':
        return redirect(url_for('index'))
    # Fetch all tickets
    all_tickets = tickets
    return render_template('helpdesk_dashboard.html', tickets=all_tickets)

@app.route('/create_ticket', methods=['GET', 'POST'])
def create_ticket():
    if 'user' not in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        submitter = session['user']['username']
        status = 'Open'
        created_at = datetime.now()
        ticket = {
            'id': len(tickets) + 1,
            'title': title,
            'description': description,
            'submitter': submitter,
            'status': status,
            'created_at': created_at
        }
        tickets.append(ticket)
        return redirect(url_for('user_dashboard'))
    return render_template('create_ticket.html')

@app.route('/view_ticket/<int:ticket_id>', methods=['GET', 'POST'])
def view_ticket(ticket_id):
    if 'user' not in session:
        return redirect(url_for('index'))
    ticket = None
    for t in tickets:
        if t['id'] == ticket_id:
            ticket = t
            break
    if not ticket:
        return redirect(url_for('user_dashboard'))
    if request.method == 'POST':
        new_status = request.form['status']
        ticket['status'] = new_status
        return redirect(url_for('view_ticket', ticket_id=ticket_id))
    return render_template('view_ticket.html', ticket=ticket)

@app.route('/download_pdf/<int:ticket_id>')
def download_pdf(ticket_id):
    if 'user' not in session:
        return redirect(url_for('index'))
    ticket = None
    for t in tickets:
        if t['id'] == ticket_id:
            ticket = t
            break
    if not ticket:
        return redirect(url_for('user_dashboard'))
    # Generate PDF from ticket data
    html = f"""
    <html>
    <head>
        <title>Ticket {ticket_id}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .ticket {{ border: 1px solid #ccc; padding: 20px; margin: 20px 0; }}
        </style>
    </head>
    <body>
        <div class="ticket">
            <h1>Ticket {ticket_id}</h1>
            <h2>{ticket['title']}</h2>
            <p><strong>Submitter:</strong> {ticket['submitter']}</p>
            <p><strong>Status:</strong> {ticket['status']}</p>
            <p><strong>Created At:</strong> {ticket['created_at'].strftime('%Y-%m-%d %H:%M')}</p>
            <p><strong>Description:</strong> {ticket['description']}</p>
        </div>
    </body>
    </html>
    """
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename=ticket_{ticket_id}.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)