from flask import Flask, request, jsonify, render_template, redirect, url_for
from models import db, Ticket, Message
from flask_restful import Api, Resource

app = Flask(__name__)
init_db(app)
api = Api(app)

# GUI Routes
@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/tickets', methods=['GET', 'POST'])
def tickets():
    if request.method == 'POST':
        description = request.form.get('description')
        category = request.form.get('category')
        new_ticket = Ticket(description=description, category=category)
        db.session.add(new_ticket)
        db.session.commit()
    user_type = request.args.get('user_type', 'user')
    if user_type == 'helpdesk':
        tickets = Ticket.query.all()
    else:
        tickets = Ticket.query.filter_by(status='open').all()
    return render_template('tickets.html', tickets=tickets, user_type=user_type)

@app.route('/ticket/<int:ticket_id>', methods=['GET', 'POST'])
def ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    messages = Message.query.filter_by(ticket_id=ticket.id).all()
    if request.method == 'POST':
        content = request.form.get('content')
        new_message = Message(content=content, ticket_id=ticket.id)
        db.session.add(new_message)
        db.session.commit()
    user_type = request.args.get('user_type', 'user')
    return render_template('ticket_detail.html', ticket=ticket, messages=messages, user_type=user_type)

@app.route('/update_ticket/<int:ticket_id>', methods=['POST'])
def update_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    if request.form.get('status'):
        ticket.status = request.form['status']
    db.session.commit()
    return redirect(url_for('tickets', user_type='helpdesk'))

# RESTful API
class TicketCount(Resource):
    def get(self, period):
        from datetime import datetime, timedelta
        end_date = datetime.now()
        start_date = end_date - timedelta(days=int(period))
        tickets = Ticket.query.filter(Ticket.opened_at >= start_date, Ticket.closed_at.is_(None)).all()
        return {'count': len(tickets)}

class AverageResolutionTime(Resource):
    def get(self):
        from sqlalchemy import extract
        results = db.session.query(extract('month', Ticket.opened_at).label('month'),
                                   db.func.avg(Ticket.closed_at - Ticket.opened_at).label('avg_time')).\
                                   filter(Ticket.status == 'closed').\
                                   group_by(extract('month', Ticket.opened_at)).all()
        return [{'month': row.month, 'average_resolution_time': str(row.avg_time)} for row in results]

class ClusterTickets(Resource):
    def get(self):
        from sqlalchemy import func
        results = db.session.query(Ticket.category, func.count()).\
                                   filter(Ticket.status != 'closed').\
                                   group_by(Ticket.category).all()
        return [{'category': category, 'count': count} for category, count in results]

api.add_resource(TicketCount, '/api/tickets/count/<string:period>')
api.add_resource(AverageResolutionTime, '/api/tickets/average_resolution_time')
api.add_resource(ClusterTickets, '/api/tickets/cluster')

if __name__ == '__main__':
    app.run(debug=True)