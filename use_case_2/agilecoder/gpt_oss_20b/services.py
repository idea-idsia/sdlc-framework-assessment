'''
Flask micro‑services that expose analysis endpoints.
'''
import datetime
import threading
from flask import Flask, request, jsonify
from database import Database
from models import Ticket
app = Flask(__name__)
app.config['HOST'] = '127.0.0.1'
app.config['PORT'] = 5000
def parse_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default
@app.route('/service1', methods=['GET'])
def service1():
    """
    Query param: period_type ('hours' or 'days'), period_value (int)
    Returns number of tickets opened in that period and not yet closed.
    """
    period_type = request.args.get('period_type', 'days')
    period_value = parse_int(request.args.get('period_value', 1))
    now = datetime.datetime.utcnow()
    delta = datetime.timedelta(hours=period_value) if period_type == 'hours' else datetime.timedelta(days=period_value)
    start_ts = now - delta
    rows = Database.instance().query('''
        SELECT COUNT(*) AS cnt FROM tickets
        WHERE opening_date >= ? AND status != ?
    ''', (start_ts.isoformat(), Ticket.STATUS_CLOSED))
    return jsonify({'open_tickets': rows[0]['cnt']})
@app.route('/service2', methods=['GET'])
def service2():
    """
    Returns the count of active tickets per category.
    """
    rows = Database.instance().query('''
        SELECT category, COUNT(*) AS cnt FROM tickets
        WHERE status = ?
        GROUP BY category
    ''', (Ticket.STATUS_ACTIVE,))
    result = {row['category']: row['cnt'] for row in rows}
    return jsonify(result)
@app.route('/service3', methods=['GET'])
def service3():
    """
    Returns average time from creation to closure for closed tickets.
    """
    rows = Database.instance().query('''
        SELECT AVG(julianday(closing_date) - julianday(opening_date)) AS avg_time
        FROM tickets WHERE status = ?
    ''', (Ticket.STATUS_CLOSED,))
    return jsonify({'average_time_days': rows[0]['avg_time']})
def run_services():
    app.run(host=app.config['HOST'], port=app.config['PORT'])
def start_service_thread():
    thread = threading.Thread(target=run_services, daemon=True)
    thread.start()