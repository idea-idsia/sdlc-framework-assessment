# Expand app.py with more functionality

with open("ticket_management/app.py", "a") as f:
    f.write('''

from flask import flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = LoginForm()
    if form.validate_on_submit():
        user_type = form.user_type.data
        if user_type == 'user':
            return redirect(url_for('user_dashboard'))
        elif user_type == 'helpdesk':
            return redirect(url_for('helpdesk_dashboard'))

    return render_template('login.html', form=form)

@app.route('/user_dashboard')
def user_dashboard():
    tickets = Ticket.query.filter(Ticket.status.in_(['open', 'active'])).all()
    return render_template('user_dashboard.html', tickets=tickets)

@app.route('/helpdesk_dashboard')
def helpdesk_dashboard():
    tickets = Ticket.query.all()
    return render_template('helpdesk_dashboard.html', tickets=tickets)

@app.route('/create_ticket', methods=['GET', 'POST'])
def create_ticket():
    if request.method == 'POST':
        description = request.form['description']
        category = request.form['category']

        new_ticket = Ticket(description=description, category=category)
        db.session.add(new_ticket)

        try:
            db.session.commit()
            flash('Ticket created successfully!', 'success')
            return redirect(url_for('user_dashboard'))
        except IntegrityError:
            db.session.rollback()
            flash('There was an error creating the ticket.', 'danger')

    categories = ['facility management', 'technical IT', 'services complaints']
    return render_template('create_ticket.html', categories=categories)

@app.route('/ticket/<int:ticket_id>', methods=['GET', 'POST'])
def ticket_details(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)

    if request.method == 'POST':
        if 'status' in request.form:
            new_status = request.form['status']
            ticket.status = new_status
            ticket.last_modification_date = datetime.datetime.utcnow()
            if new_status == 'closed':
                ticket.closing_date = datetime.datetime.utcnow()

            db.session.commit()
            flash('Ticket status updated!', 'success')
            return redirect(url_for('helpdesk_dashboard'))

        if 'message' in request.form:
            message_text = request.form['message']
            # Add message handling logic here (not implemented in this basic example)
            flash('Message added!', 'success')

    return render_template('ticket_details.html', ticket=ticket)

@app.route('/update_ticket/<int:ticket_id>', methods=['GET', 'POST'])
def update_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)

    if request.method == 'POST':
        ticket.description = request.form['description']
        ticket.category = request.form['category']
        ticket.last_modification_date = datetime.datetime.utcnow()

        db.session.commit()
        flash('Ticket updated!', 'success')
        return redirect(url_for('user_dashboard'))

    categories = ['facility management', 'technical IT', 'services complaints']
    return render_template('update_ticket.html', ticket=ticket, categories=categories)
''')

# Create create_ticket template
create_ticket_html = '''
{% extends "base.html" %}

{% block content %}
<h2>Create Ticket</h2>
<form method="post">
    <div>
        <label for="description">Description:</label><br>
        <textarea id="description" name="description" rows="4" cols="50"></textarea>
    </div>
    <div>
        <label for="category">Category:</label><br>
        <select id="category" name="category">
            {% for category in categories %}
                <option value="{{ category }}">{{ category }}</option>
            {% endfor %}
        </select>
    </div>
    <button type="submit">Create Ticket</button>
</form>
{% endblock %}
'''

with open("ticket_management/templates/create_ticket.html", "w") as f:
    f.write(create_ticket_html)

# Create ticket_details template
ticket_details_html = '''
{% extends "base.html" %}

{% block content %}
<h2>Ticket Details - {{ ticket.id }}</h2>
<p><strong>Status:</strong> {{ ticket.status }}</p>
<p><strong>Description:</strong> {{ ticket.description }}</p>
<p><strong>Category:</strong> {{ ticket.category }}</p>
<p><strong>Opening Date:</strong> {{ ticket.opening_date.strftime('%Y-%m-%d %H:%M:%S') }}</p>
{% if ticket.last_modification_date %}
    <p><strong>Last Modified:</strong> {{ ticket.last_modification_date.strftime('%Y-%m-%d %H:%M:%S') }}</p>
{% endif %}
{% if ticket.closing_date %}
    <p><strong>Closed Date:</strong> {{ ticket.closing_date.strftime('%Y-%m-%d %H:%M:%S') }}</p>
{% endif %}

{% if user_type == 'helpdesk' %}
    <h3>Update Status</h3>
    <form method="post">
        <select name="status">
            <option value="open" {% if ticket.status == "open" %}selected{% endif %}>Open</option>
            <option value="active" {% if ticket.status == "active" %}selected{% endif %}>Active</option>
            <option value="closed" {% if ticket.status == "closed" %}selected{% endif %}>Closed</option>
        </select>
        <button type="submit">Update Status</button>
    </form>
{% endif %}

<h3>Add Message</h3>
<form method="post">
    <textarea name="message" rows="4" cols="50"></textarea><br>
    <button type="submit">Add Message</button>
</form>

<a href="{{ url_for('user_dashboard') }}">Back to Dashboard</a>
{% endblock %}
'''

with open("ticket_management/templates/ticket_details.html", "w") as f:
    f.write(ticket_details_html)

# Create update_ticket template
update_ticket_html = '''
{% extends "base.html" %}

{% block content %}
<h2>Update Ticket - {{ ticket.id }}</h2>
<form method="post">
    <div>
        <label for="description">Description:</label><br>
        <textarea id="description" name="description" rows="4" cols="50">{{ ticket.description }}</textarea>
    </div>
    <div>
        <label for="category">Category:</label><br>
        <select id="category" name="category">
            {% for category in categories %}
                <option value="{{ category }}" {% if ticket.category == category %}selected{% endif %}>{{ category }}</option>
            {% endfor %}
        </select>
    </div>
    <button type="submit">Update Ticket</button>
</form>

<a href="{{ url_for('user_dashboard') }}">Back to Dashboard</a>
{% endblock %}
'''

with open("ticket_management/templates/update_ticket.html", "w") as f:
    f.write(update_ticket_html)

# Install dependencies and run the application
import sys
subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], cwd="ticket_management")
subprocess.run([sys.executable, "app.py"], cwd="ticket_management")