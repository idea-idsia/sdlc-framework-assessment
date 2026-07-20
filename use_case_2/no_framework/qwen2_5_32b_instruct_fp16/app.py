from flask import Flask, render_template, request, redirect, url_for
from models import db, Ticket

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'  # Use SQLite for simplicity
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login_page():
    return render_template('login.html')  # Placeholder template


@app.route('/tickets', methods=['GET', 'POST'])
def tickets():
    if request.method == 'POST':
        description = request.form.get('description')
        category = request.form.get('category')
        new_ticket = Ticket(description=description, category=category)
        db.session.add(new_ticket)
        db.session.commit()
        return redirect(url_for('tickets'))

    # GET request
    tickets_query = Ticket.query.all()  # Adjust query based on user role.
    return render_template('tickets.html', tickets=tickets_query)


# Implement other routes for ticket modification, status change, etc.

if __name__ == '__main__':
    app.run(debug=True)