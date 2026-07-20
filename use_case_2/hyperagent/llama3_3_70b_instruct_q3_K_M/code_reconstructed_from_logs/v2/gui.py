# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
db = SQLAlchemy(app)

# Define the Ticket model
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), default='open')
    description = db.Column(db.Text)
    category = db.Column(db.String(50))
    opening_date = db.Column(db.DateTime)
    last_modification_date = db.Column(db.DateTime)
    closing_date = db.Column(db.DateTime)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    role = db.Column(db.String(50))

# Implement the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        if user:
            return redirect(url_for('index'))
    return render_template('login.html')

# Implement the ticket management logic
@app.route('/tickets', methods=['GET', 'POST'])
def tickets():
    if request.method == 'POST':
        description = request.form['description']
        category = request.form['category']
        ticket = Ticket(description=description, category=category)
        db.session.add(ticket)
        db.session.commit()
    tickets = Ticket.query.all()
    return render_template('tickets.html', tickets=tickets)

if __name__ == '__main__':
    app.run(debug=True)