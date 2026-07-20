## routes/users.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
import models  # Assuming models are defined in the models.py file
from database import get_db  # Importing session creation function from database module
from schemas.users import UserCreate, UserLogin

router = APIRouter()

@router.post("/login", response_model=bool)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    """
    User login.
    
    :param user_data: UserLogin object containing username and password
    :param db: Database session
    :return: Success flag indicating if the login was successful
    """
    user = models.User.get_user_by_username(db, user_data.username)
    if not user or not user.login():
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return True

@router.post("/report_ticket", response_model=models.Ticket, status_code=status.HTTP_201_CREATED)
def report_ticket(ticket_data: models.TicketCreate, db: Session = Depends(get_db)):
    """
    Report a new ticket.
    
    :param ticket_data: TicketCreate object containing title and description
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

@router.put("/modify_ticket/{ticket_id}", response_model=bool)
def modify_ticket(ticket_id: int, status_update: models.TicketUpdate, db: Session = Depends(get_db)):
    """
    Update the status of a ticket.
    
    :param ticket_id: ID of the ticket
    :param status_update: TicketUpdate object containing new status
    :param db: Database session
    :return: Success flag indicating if the update was successful
    """
    ticket = models.Ticket.get_ticket_by_id(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    ticket.update_status(status_update.status)
    db.commit()
    return True

@router.put("/modify_user/{user_id}", response_model=bool)
def modify_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Modify user details.
    
    :param user_data: UserCreate object containing updated username and password
    :param db: Database session
    :return: Success flag indicating if the update was successful
    """
    user = models.User.get_user_by_id(db, user_data.id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.username = user_data.username
    user.password_hash = user_data.password_hash
    db.commit()
    return True
