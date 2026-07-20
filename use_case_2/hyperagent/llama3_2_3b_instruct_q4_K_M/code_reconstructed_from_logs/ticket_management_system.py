from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
db = SQLAlchemy(app)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    opening_date = db.Column(db.Date, nullable=False)
    last_modification_date = db.Column(db.Date, nullable=True)
    closing_date = db.Column(db.Date, nullable=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report', methods=['GET', 'POST'])
def report_issue():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        category = request.form['category']

        ticket = Ticket(title=title, description=description, category=category, status='open')
        db.session.add(ticket)
        db.session.commit()

        return redirect(url_for('view_tickets'))
    return render_template('report.html')

@app.route('/tickets', methods=['GET'])
def view_tickets():
    tickets = Ticket.query.filter_by(status='open').all()
    return render_template('tickets.html', tickets=tickets)

@app.route('/ticket/<int:ticket_id>', methods=['GET', 'POST'])
def ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if request.method == 'POST':
        if request.form['action'] == 'close':
            ticket.status = 'closed'
            db.session.commit()

    return render_template('ticket.html', ticket=ticket)

if __name__ == '__main__':
    app.run(debug=True)