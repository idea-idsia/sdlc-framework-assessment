## routes.py
from flask import request, jsonify
from models import TicketModel, Comment, Base
from sqlalchemy.orm import sessionmaker

def create_ticket():
    data = request.get_json()
    title = data['title']
    description = data['description']

    with get_session() as session:
        try:
            new_ticket = TicketModel(title=title, description=description)
            session.add(new_ticket)
            session.commit()
            return jsonify({'ticket_id': new_ticket.id}), 201
        except Exception as e:
            session.rollback()
            return jsonify({'error': str(e)}), 500

def add_comment():
    data = request.get_json()
    ticket_id = data['ticket_id']
    content = data['content']

    with get_session() as session:
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

def get_session():
    from sqlalchemy import create_engine
    
    DATABASE_URI = 'sqlite:///tickets.db'
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    
    return Session()

# Refactoring to integrate with Flask routes
from flask import Blueprint

bp = Blueprint('routes', __name__)

@bp.route('/ticket', methods=['POST'])
def route_create_ticket():
    return create_ticket()

@bp.route('/comment', methods=['POST'])
def route_add_comment():
    return add_comment()
