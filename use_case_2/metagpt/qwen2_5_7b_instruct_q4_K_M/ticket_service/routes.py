## routes.py

from fastapi import APIRouter, Depends, HTTPException
from flask import request, jsonify
import datetime
from sqlalchemy.orm import Session
from models import User, Ticket, Message, HelpdeskStaff, DatabaseAPI, MicroservicesAPI  # Import data model definitions
from microservices_api import MicroservicesAPI  # Import microservices API logic

# Initialize router for FastAPI
user_router = APIRouter()
ticket_router = APIRouter()

# Dependency injection for database session
def get_db_session() -> Session:
    db_session = DatabaseAPI.create_db_session()  # Assume create_db_session is defined in models.py
    try:
        yield db_session
    finally:
        db_session.close()

@user_router.post('/users/login')
async def login(username: str, password_hash: str) -> dict:
    user = MicroservicesAPI.get_user_by_username(db_api=Depends(get_db_session), username=username)
    if not user or not bcrypt.checkpw(password_hash.encode('utf-8'), user.password_hash.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}

@ticket_router.post('/tickets/report-issue')
async def report_issue(username: str, issue: str) -> dict:
    db_session = get_db_session()
    user = MicroservicesAPI.get_user_by_username(db_api=db_session, username=username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    ticket = user.report_issue(issue=issue)
    return {"ticket_id": ticket.id}

@ticket_router.get('/tickets/view-tickets')
async def view_tickets(status: str) -> list[dict]:
    db_session = get_db_session()
    tickets = MicroservicesAPI.view_tickets(db_api=db_session, status=status)
    return [{"id": t.id, "user_id": t.user_id, "issue": t.issue, "status": t.status} for t in tickets]

@ticket_router.put('/tickets/modify-ticket-status')
async def modify_ticket_status(ticket_id: int, new_status: str) -> dict:
    db_session = get_db_session()
    success = MicroservicesAPI.change_ticket_status(db_api=db_session, ticket_id=ticket_id, new_status=new_status)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to update ticket status")
    return {"message": "Ticket status updated successfully"}

# Register routers for FastAPI
def register_fastapi_routers(fastapi_app: FastAPI):
    fastapi_app.include_router(user_router, prefix="/users")
    fastapi_app.include_router(ticket_router, prefix="/tickets")

# Register routes for Flask application
def register_flask_routes(flask_app: Flask):
    @flask_app.route('/users/login', methods=['POST'])
    def login_route():
        data = request.get_json()
        username = data.get('username')
        password_hash = data.get('password_hash')
        return jsonify(login(username, password_hash))

    @flask_app.route('/tickets/report-issue', methods=['POST'])
    def report_issue_route():
        data = request.get_json()
        username = data.get('username')
        issue = data.get('issue')
        return jsonify(report_issue(username, issue))

    @flask_app.route('/tickets/view-tickets', methods=['GET'])
    def view_tickets_route():
        status = request.args.get('status')
        return jsonify(view_tickets(status=status))

    @flask_app.route('/tickets/modify-ticket-status', methods=['PUT'])
    def modify_ticket_status_route():
        data = request.get_json()
        ticket_id = data.get('ticket_id')
        new_status = data.get('new_status')
        return jsonify(modify_ticket_status(ticket_id=ticket_id, new_status=new_status))
