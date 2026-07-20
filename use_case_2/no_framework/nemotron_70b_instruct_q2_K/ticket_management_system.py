from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tickets.db"
db = SQLAlchemy(app)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(10), nullable=False, default='open')

@app.route('/new_ticket', methods=['POST'])
def new_ticket():
    # Process new ticket form
    pass

@app.route('/view_tickets')
def view_tickets():
    # Display tickets with appropriate actions based on user type
    pass