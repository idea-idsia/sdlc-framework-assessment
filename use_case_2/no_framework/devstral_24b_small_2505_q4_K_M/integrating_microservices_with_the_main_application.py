# Update app.py with microservice integration

with open("ticket_management/app.py", "a") as f:
    f.write('''

import requests

@app.route('/ticket_stats')
def ticket_stats():
    # Get counts from the ticket count service
    statuses = ['open', 'active', 'closed']
    stats = {}
    for status in statuses:
        response = requests.get(f'http://localhost:5001/count_by_status?status={status}')
        if response.status_code == 200:
            data = response.json()
            stats[f"count_{status}"] = data[f"count_{status}"]

    # Get average response time from the ticket analysis service
    categories = ['facility management', 'technical IT', 'services complaints']
    for category in categories:
        response = requests.get(f'http://localhost:5002/average_response_time?category={category}')
        if response.status_code == 200:
            data = response.json()
            stats[f"average_response_time_{category}"] = data[f"average_response_time_{category}"]

    return render_template('ticket_stats.html', stats=stats)

# Create ticket_stats template
ticket_stats_html = '''
{% extends "base.html" %}

{% block content %}
<h2>Ticket Statistics</h2>
<ul>
    <li>Open Tickets: {{ stats.count_open }}</li>
    <li>Active Tickets: {{ stats.count_active }}</li>
    <li>Closed Tickets: {{ stats.count_closed }}</li>
    <li>Average Response Time - Facility Management: {{ stats.average_response_time_facility_management }} days</li>
    <li>Average Response Time - Technical IT: {{ stats.average_response_time_technical_it }} days</li>
    <li>Average Response Time - Services Complaints: {{ stats.average_response_time_services_complaints }} days</li>
</ul>

<a href="{{ url_for('helpdesk_dashboard') }}">Back to Dashboard</a>
{% endblock %}
'''

with open("ticket_management/templates/ticket_stats.html", "w") as f:
    f.write(ticket_stats_html)
''')

# Run the main application
import sys
subprocess.run([sys.executable, "app.py"], cwd="ticket_management")