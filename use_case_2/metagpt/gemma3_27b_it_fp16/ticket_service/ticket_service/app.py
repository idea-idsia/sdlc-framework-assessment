"""
ticket_service/app.py
Flask app for ticket management, defines API endpoints.
"""
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from sqlalchemy.orm import Session
from ticket_service.models import Ticket, init_db, get_db
from datetime import datetime
import logging

# Initialize Flask app
app = Flask(__name__)
api = Api(app)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize database
init_db()  # Ensure the database is initialized when the app starts

class TicketService(Resource):
    """
    Resource for managing tickets.
    """

    def create_ticket(self) -> jsonify:
        """
        Creates a new ticket.
        """
        try:
            data = request.get_json()
            description: str = data.get("description", "")
            status: str = data.get("status", "open")
            category: str = data.get("category", "")

            if not description:
                return {"message": "Description is required"}, 400

            db: Session = next(get_db())
            new_ticket = Ticket(description=description, status=status, category=category)
            db.add(new_ticket)
            db.commit()
            db.refresh(new_ticket)  # Refresh to get the assigned ticket_id
            logging.info(f"Created ticket with id: {new_ticket.ticket_id}")
            return jsonify({"ticket_id": new_ticket.ticket_id, "description": new_ticket.description, "status": new_ticket.status, "category": new_ticket.category}), 201
        except Exception as e:
            logging.error(f"Error creating ticket: {e}")
            return {"message": "Failed to create ticket"}, 500
        finally:
            if 'db' in locals():
                db.close()

    def get_ticket(self, ticket_id: int) -> jsonify:
        """
        Retrieves a ticket by ID.
        """
        try:
            db: Session = next(get_db())
            ticket: Ticket = db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()

            if ticket is None:
                return {"message": "Ticket not found"}, 404

            return jsonify({
                "ticket_id": ticket.ticket_id,
                "description": ticket.description,
                "status": ticket.status,
                "category": ticket.category,
                "opening_date": ticket.opening_date,
                "last_modification_date": ticket.last_modification_date,
                "closing_date": ticket.closing_date
            }), 200
        except Exception as e:
            logging.error(f"Error getting ticket: {e}")
            return {"message": "Failed to get ticket"}, 500
        finally:
            if 'db' in locals():
                db.close()

    def update_ticket(self, ticket_id: int) -> jsonify:
        """
        Updates a ticket by ID.
        """
        try:
            data = request.get_json()
            status: str = data.get("status")
            description: str = data.get("description")
            category: str = data.get("category")

            db: Session = next(get_db())
            ticket: Ticket = db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()

            if ticket is None:
                return {"message": "Ticket not found"}, 404

            if status:
                ticket.status = status
            if description:
                ticket.description = description
            if category:
                ticket.category = category

            ticket.last_modification_date = datetime.utcnow()
            db.commit()

            return jsonify({
                "ticket_id": ticket.ticket_id,
                "description": ticket.description,
                "status": ticket.status,
                "category": ticket.category,
                "last_modification_date": ticket.last_modification_date
            }), 200
        except Exception as e:
            logging.error(f"Error updating ticket: {e}")
            return {"message": "Failed to update ticket"}, 500
        finally:
            if 'db' in locals():
                db.close()

    def delete_ticket(self, ticket_id: int) -> jsonify:
        """
        Deletes a ticket by ID.
        """
        try:
            db: Session = next(get_db())
            ticket: Ticket = db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()

            if ticket is None:
                return {"message": "Ticket not found"}, 404

            db.delete(ticket)
            db.commit()

            return {"message": "Ticket deleted successfully"}, 200
        except Exception as e:
            logging.error(f"Error deleting ticket: {e}")
            return {"message": "Failed to delete ticket"}, 500
        finally:
            if 'db' in locals():
                db.close()


# Add resources to the API
api.add_resource(TicketService, '/tickets', '/tickets/<int:ticket_id>')

if __name__ == '__main__':
    app.run(debug=True)
