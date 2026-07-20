from flask import Flask, render_template, request, redirect, url_for
from models import db, User, Ticket, HelpDeskStaff, TicketManagementSystem, DataVisualizer
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ticket_management.db'
db.init_app(app)

@app.route('/')
def index():
    """
    The main route for the application.
    
    Returns:
        A rendered HTML template for the index page.
    """
    return render_template('index.html')

@app.route('/report_issue', methods=['POST'])
def report_issue():
    """
    Handles the reporting of an issue by creating a new ticket.
    
    Returns:
        A redirect to the index page after creating the ticket.
    """
    try:
        user_id = request.form.get('user_id')
        issue = request.form.get('issue')
        user = User.query.get(user_id)
        if user:
            ticket = TicketManagementSystem.report_issue(user, issue)
            return redirect(url_for('index'))
        else:
            return "User not found. Please check the user ID and try again.", 404
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/view_tickets')
def view_tickets():
    """
    Retrieves a list of all tickets in the system.
    
    Returns:
        A rendered HTML template for viewing tickets.
    """
    try:
        tickets = TicketManagementSystem.view_tickets()
        return render_template('view_tickets.html', tickets=tickets)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/assign_ticket', methods=['POST'])
def assign_ticket():
    """
    Assigns a ticket to a help desk staff member.
    
    Returns:
        A redirect to the index page after assigning the ticket.
    """
    try:
        helpdesk_staff_id = request.form.get('helpdesk_staff_id')
        ticket_id = request.form.get('ticket_id')
        helpdesk_staff = HelpDeskStaff.query.get(helpdesk_staff_id)
        if helpdesk_staff:
            TicketManagementSystem.assign_ticket(helpdesk_staff, int(ticket_id))
            return redirect(url_for('index'))
        else:
            return "Help desk staff not found. Please check the staff ID and try again.", 404
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/visualize_ticket_data')
def visualize_ticket_data():
    """
    Visualizes the ticket data using matplotlib and seaborn.
    
    Returns:
        A rendered HTML template for visualizing ticket data.
    """
    try:
        data_visualizer = DataVisualizer()
        plot_url = data_visualizer.visualize_ticket_data()
        return render_template('visualize_ticket_data.html', plot_url=plot_url)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
