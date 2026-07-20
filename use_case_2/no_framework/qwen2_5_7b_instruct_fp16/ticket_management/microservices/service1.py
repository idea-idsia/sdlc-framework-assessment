from flask import Flask, jsonify
from datetime import timedelta
import arrow

app = Flask(__name__)


@app.route('/service1/<int:x_hours>')
def service1(x_hours):
    now = arrow.utcnow()
    start_time = (now - timedelta(hours=x_hours)).datetime

    tickets_open = Ticket.query.filter(Ticket.status == 'open', Ticket.opening_date >= start_time).count()

    return jsonify({'tickets_open': tickets_open})