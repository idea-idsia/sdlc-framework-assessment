## routes/messages.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
import models  # Assuming models are defined in the models.py file
from database import get_db  # Importing session creation function from database module
from schemas.messages import MessageCreate

router = APIRouter()

@router.post("/{ticket_id}/messages", response_model=models.Message, status_code=status.HTTP_201_CREATED)
def send_message(ticket_id: int, message_data: MessageCreate, db: Session = Depends(get_db)):
    """
    Send a message for the ticket.
    
    :param ticket_id: ID of the ticket
    :param message_data: MessageCreate object containing message content
    :param db: Database session
    :return: Created message
    """
    # Get the ticket by its ID
    ticket = models.Ticket.get_ticket_by_id(db, ticket_id)
    
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    # Create a new message with the provided content and associate it with the ticket
    new_message = models.Message(content=message_data.content)
    new_message.ticket_id = ticket.id
    
    # Add the new message to the database session and commit the changes
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    
    return new_message
