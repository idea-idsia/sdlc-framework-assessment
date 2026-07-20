## routes/tickets.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import models  # Assuming models are defined in the models.py file
from database import get_db  # Importing session creation function from database module
from schemas.tickets import TicketCreate, TicketUpdate

router = APIRouter()

@router.post("/report", response_model=models.Ticket, status_code=status.HTTP_201_CREATED)
def report_ticket(ticket_data: TicketCreate, db: Session = Depends(get_db)):
    """
    Report a new ticket.
    
    :param ticket_data: TicketCreate
    :param db: Database session
    :return: Created ticket
    """
    user = models.User.get_user_by_username(db, ticket_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_ticket = models.Ticket(title=ticket_data.title, description=ticket_data.description)
    new_ticket.user_id = user.id
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

@router.put("/{ticket_id}/status", response_model=bool)
def update_ticket_status(ticket_id: int, status_update: TicketUpdate, db: Session = Depends(get_db)):
    """
    Update the status of a ticket.
    
    :param ticket_id: ID of the ticket
    :param status_update: TicketUpdate object containing new status
    :param db: Database session
    :return: Success flag
    """
    ticket = models.Ticket.get_ticket_by_id(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    ticket.update_status(status_update.status)
    db.commit()
    return True

@router.post("/{ticket_id}/messages", response_model=models.Message, status_code=status.HTTP_201_CREATED)
def send_message(ticket_id: int, message_data: models.MessageCreate, db: Session = Depends(get_db)):
    """
    Send a message for the ticket.
    
    :param ticket_id: ID of the ticket
    :param message_data: MessageCreate object containing message content
    :param db: Database session
    :return: Created message
    """
    ticket = models.Ticket.get_ticket_by_id(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    new_message = models.Message(content=message_data.content)
    new_message.ticket_id = ticket.id
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message
