## main.py

from fastapi import FastAPI, Depends, HTTPException
from flask import Flask, request, jsonify
from sqlalchemy.orm import Session
import models  # Import the data model definitions
from routes import user_routes, ticket_routes  # Import route handlers
from microservices_api import MicroservicesAPI  # Import microservices API logic

# Initialize FastAPI and Flask applications
fastapi_app = FastAPI()
flask_app = Flask(__name__)

# Dependency injection for database session
def get_db_session():
    db_session = models.create_db_session()  # Assume create_db_session is defined in models.py
    try:
        yield db_session
    finally:
        db_session.close()

# Initialize Microservices API with the database session dependency
microservices_api = MicroservicesAPI(db_api=Depends(get_db_session))

# Register routes for FastAPI and Flask applications
fastapi_app.include_router(user_routes, prefix="/users")
fastapi_app.include_router(ticket_routes, prefix="/tickets")

flask_app.add_url_rule('/users/login', 'login', user_routes.login, methods=['POST'])
flask_app.add_url_rule('/tickets/report-issue', 'report_issue', ticket_routes.report_issue, methods=['POST'])
flask_app.add_url_rule('/tickets/view-tickets', 'view_tickets', ticket_routes.view_tickets, methods=['GET'])
flask_app.add_url_rule('/tickets/modify-ticket-status', 'modify_ticket_status', ticket_routes.modify_ticket_status, methods=['PUT'])

@flask_app.route('/')
def index():
    return "Welcome to Helpdesk Management System"

# Main function to run the applications
if __name__ == "__main__":
    import uvicorn  # Import Uvicorn for running FastAPI application

    # Run Flask and FastAPI applications
    flask_app.run()
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)
