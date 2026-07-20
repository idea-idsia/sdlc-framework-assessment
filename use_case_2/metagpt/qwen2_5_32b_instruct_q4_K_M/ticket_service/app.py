## app.py
from flask import Flask, request, jsonify
from models import TicketModel, Comment, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from analytics_service import AnalyticsService  # Corrected import statement

app = Flask(__name__)

# Database setup
DATABASE_URI = 'sqlite:///tickets.db'
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@app.route('/ticket', methods=['POST'])
def create_ticket():
    data = request.get_json()
    title = data['title']
    description = data['description']

    with Session() as session:
        try:
            new_ticket = TicketModel(title=title, description=description)
            session.add(new_ticket)
            session.commit()
            return jsonify({'ticket_id': new_ticket.id}), 201
        except Exception as e:
            session.rollback()
            return jsonify({'error': str(e)}), 500

@app.route('/comment', methods=['POST'])
def add_comment():
    data = request.get_json()
    ticket_id = data['ticket_id']
    content = data['content']

    with Session() as session:
        try:
            comment = Comment(content=content)
            ticket = session.query(TicketModel).filter_by(id=ticket_id).first()

            if not ticket:
                return jsonify({'error': 'Ticket not found'}), 404

            ticket.comments.append(comment)
            session.add(ticket)
            session.commit()
            return jsonify({'comment_id': comment.id}), 201
        except Exception as e:
            session.rollback()
            return jsonify({'error': str(e)}), 500

@app.route('/analytics/resolution_times', methods=['GET'])
def get_resolution_times():
    service = AnalyticsService()
    resolution_times = service.get_resolution_times()
    return jsonify(resolution_times), 200

@app.route('/analytics/active_tickets_by_category', methods=['GET'])
def get_active_tickets_by_category():
    service = AnalyticsService()
    active_tickets = service.get_active_tickets_by_category()
    return jsonify(active_tickets), 200

if __name__ == '__main__':
    app.run(debug=True)
