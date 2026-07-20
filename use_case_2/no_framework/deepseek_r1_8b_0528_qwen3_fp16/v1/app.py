import os
import sqlite3
import datetime
from datetime import datetime, timedelta
from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_socketio import SocketIO, emit
from flask_cors import CORS

# Initialize the main Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# Database models
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)

    # Relationships
    tickets = db.relationship('Ticket', backref='user', lazy=True)
    messages = db.relationship('Message', backref='user', lazy=True)


class Ticket(db.Model):
    __tablename__ = autoincrement = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='open')
    opening_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_modification_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    closing_date = db.Column(db.DateTime, nullable=True)

    # Relationships
    messages = db.relationship('Message', backref='ticket', lazy=True)


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


# Microservices endpoints
@app.route('/api/period/<int:hours>')
@login_required
def api_period(hours):
    if current_user.role != 'helpdesk':
        return jsonify({'error': 'Unauthorized'}), 403

    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Calculate the time period
    period_end = datetime.utcnow()
    period_start = period_end - timedelta(hours=hours)

    # Get tickets opened in the period that are still open
    cursor.execute("""
                   SELECT COUNT(*)
                   FROM tickets
                   WHERE opening_date >= ?
                     AND opening_date <= ?
                     AND status != 'closed'
                   """, (period_start, period_end))

    count = cursor.fetchone()[0]

    conn.close()

    return jsonify({'count': count})


@app.route('/api/avg_resolution_time')
@login_required
def api_avg_resolution_time():
    if current_user.role != 'helpdesk':
        return jsonify({'error': 'Unauthorized'}), 403

    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Get all closed tickets with their resolution time
    cursor.execute("""
                   SELECT strftime('%Y-%m', closing_date) as month,
            AVG(JULIANDAY(closing_date) - JULIANDAY(opening_date)) as avg_days
                   FROM tickets
                   WHERE status = 'closed' AND closing_date IS NOT NULL
                   GROUP BY month
                   ORDER BY month
                   """)

    result = []
    for row in cursor.fetchall():
        result.append({
            'month': row['month'],
            'avg_days': row['avg_days'] if row['avg_days'] is not None else 0
        })

    conn.close()

    return jsonify({'data': result})


@app.route('/api/categories')
@login_required
def api_categories():
    if current_user.role != 'helpdesk':
        return jsonify({'error': 'Unauthorized'}), 403

    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Get ticket distribution by category
    cursor.execute("""
                   SELECT category,
                          COUNT(*) as count
                   FROM tickets
                   WHERE status != 'closed'
                   GROUP BY category
                   ORDER BY count DESC
                   """)

    result = []
    for row in cursor.fetchall():
        result.append({
            'category': row['category'],
            'count': row['count']
        })

    conn.close()

    return jsonify({'data': result})


# Helper function to get database connection
def get_db_connection():
    conn = sqlite3.connect('tickets.db')
    conn.row_factory = sqlite3.Row
    return conn


# Initialize database
def init_db():
    db_fd = open('tickets.db', 'w').close()
    app.app_context().push()
    db.create_all()
    return


# Create database tables
with app.app_context():
    db.create_all()


# SocketIO for real-time updates
@socketio.on('update_tickets')
def handle_update_tickets():
    emit('ticket_updated', {'message': 'Ticket status changed'}, broadcast=True)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Routes
@app.route('/')
@login_required
def index():
    if current_user.role == 'user':
        return redirect(url_for('user_dashboard'))
    elif current_user.role == 'helpdesk':
        return redirect(url_for('helpdesk_dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')

        user = User.query.filter_by(username=username).first()

        if user and user.password == password and user.role == role:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username, password, or role')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/user/dashboard')
@login_required
def user_dashboard():
    if current_user.role != 'user':
        return redirect(url_for('index'))

    # Get all open and active tickets for the user
    tickets = Ticket.query.filter(
        Ticket.user_id == current_user.id,
        Ticket.status.in_(['open', 'active'])
    ).all()

    return render_template('user_dashboard.html', tickets=tickets)


@app.route('/helpdesk/dashboard')
@login_required
def helpdesk_dashboard():
    if current_user.role != 'helpdesk':
        return redirect(url_for('index'))

    # Get all open and active tickets
    tickets = Ticket.query.filter(Ticket.status.in_(['open', 'active'])).all()

    # Get statistics
    open_tickets = Ticket.query.filter_by(status='open').count()
    active_tickets = Ticket.query.filter_by(status='active').count()
    closed_tickets = Ticket.query.filter_by(status='closed').count()

    return render_template('helpdesk_dashboard.html',
                           tickets=tickets,
                           open_tickets=open_tickets,
                           active_tickets=active_tickets,
                           closed_tickets=closed_tickets)


@app.route('/ticket/new', methods=['GET', 'POST'])
@login_required
def create_ticket():
    if request.method == 'POST':
        category = request.form.get('category')
        description = request.form.get('description')

        if not category or not description:
            flash('Please fill all fields')
            return redirect(url_for('user_dashboard'))

        # Create new ticket
        new_ticket = Ticket(
            user_id=current_user.id,
            category=category,
            description=description
        )

        db.session.add(new_ticket)
        db.session.commit()

        flash('Ticket created successfully')
        return redirect(url_for('user_dashboard'))

    return render_template('create_ticket.html')


@app.route('/ticket/<int:ticket_id>')
@login_required
def view_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)

    if current_user.role == 'user' and ticket.user_id != current_user.id:
        flash('You don\'t have permission to view this ticket')
        return redirect(url_for('index'))

    messages = Message.query.filter_by(ticket_id=ticket_id).all()

    return render_template('view_ticket.html', ticket=ticket, messages=messages)


@app.route('/ticket/<int:ticket_id}/update', methods=['POST'])
@login_required
def update_ticket(ticket_id):
    if current_user.role != 'helpdesk':
        flash('Only helpdesk staff can update tickets')
        return redirect(url_for('view_ticket', ticket_id=ticket_id))

    ticket = Ticket.query.get_or_404(ticket_id)

    if request.form.get('status') == 'close':
        ticket.status = 'closed'
        ticket.closing_date = datetime.utcnow()
    elif request.form.get('status') == 'open':
        ticket.status = 'open'
        ticket.closing_date = None
    elif request.form.get('status') == 'active':
        ticket.status = 'active'
        ticket.closing_date = None

    db.session.commit()

    # Notify all users about the update
    socketio.emit('ticket_updated', {
        'ticket_id': ticket_id,
        'status': ticket.status
    }, broadcast=True)

    flash('Ticket status updated')
    return redirect(url_for('view_ticket', ticket_id=ticket_id))


@app.route('/message/<int:ticket_id>', methods=['POST'])
@login_required
def add_message(ticket_id):
    if current_user.role == 'helpdesk' and current_user.id == 1:  # Assuming admin is user with id 1
        content = request.form.get('content')

        if not content:
            flash('Please enter a message')
            return redirect(url_for('view_ticket', ticket_id=ticket_id))

        new_message = Message(
            ticket_id=ticket_id,
            sender_id=current_user.id,
            content=content
        )

        db.session.add(new_message)
        db.session.commit()

        flash('Message sent')
        return redirect(url_for('view_ticket', ticket_id=ticket_id))

    # Regular users can only respond if they're the ticket creator
    ticket = Ticket.query.get_or_404(ticket_id)
    if ticket.user_id == current_user.id:
        content = request.form.get('content')

        if not content:
            flash('Please enter a message')
            return redirect(url_for('view_ticket', ticket_id=ticket_id))

        new_message = Message(
            ticket_id=ticket_id,
            sender_id=current_user.id,
            content=content
        )

        db.session.add(new_message)
        db.session.commit()

        flash('Message sent')
        return redirect(url_for('view_ticket', ticket_id=ticket_id))

    flash('You don\'t have permission to send messages on this ticket')
    return redirect(url_for('view_ticket', ticket_id=ticket_id))


# Microservice routes
@app.route('/api/period/<int:hours>')
@login_required
def api_period_endpoint(hours):
    return api_period(hours)


@app.route('/api/avg_resolution_time')
@login_required
def api_avg_resolution_time_endpoint():
    return api_avg_resolution_time()


@app.route('/api/categories')
@login_required
def api_categories_endpoint():
    return api_categories()


# Template filters
@app.template_filter('time_since')
def time_since(date):
    now = datetime.utcnow()
    diff = now - date
    seconds = diff.total_seconds()

    if seconds < 60:
        return f"{int(seconds)} seconds ago"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        return f"{minutes} minutes ago"
    elif seconds < 86400:
        hours = int(seconds / 3600)
        return f"{hours} hours ago"
    else:
        days = int(seconds / 86400)
        return f"{days} days ago"


if __name__ == '__main__':
    socketio.run(app, debug=True)