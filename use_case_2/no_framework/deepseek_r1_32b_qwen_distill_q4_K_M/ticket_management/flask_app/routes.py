from flask import Blueprint, render_template, request, redirect, url_for, session
from models.ticket import Ticket, Message
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('login.html')

@bp.route('/login', methods=['POST'])
def login():
    user_type = request.form.get('user_type')
    session['user_type'] = user_type
    return redirect(url_for('main.dashboard'))

@bp.route('/dashboard', methods=['GET'])
def dashboard():
    user_type = session.get('user_type')
    tickets = Ticket.query.filter_by(status='open') if user_type == 'simple' else Ticket.query.all()
    return render_template('dashboard.html', tickets=tickets, user_type=user_type)

# Add more routes for ticket creation, modification, message handling...