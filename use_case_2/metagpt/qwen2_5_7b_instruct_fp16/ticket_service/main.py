## main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import Optional
import models  # Assuming models are defined in the models.py file
from database import get_db  # Importing session creation function from database module
from routes.users import user_router
from routes.tickets import ticket_router
from routes.messages import message_router

app = FastAPI()

# Include routers for different functionalities
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(ticket_router, prefix="/tickets", tags=["tickets"])
app.include_router(message_router, prefix="/messages", tags=["messages"])

@app.get("/")
def read_root():
    return {"message": "Ticket Management System API"}

# Dependency to get the database session
def get_db_session() -> Session:
    db: Optional[Session] = None
    try:
        db = next(get_db())
        yield db
    finally:
        if db:
            db.close()

@app.on_event("shutdown")
def shutdown_event():
    # Ensure all resources are closed on shutdown
    pass

# Example of a simple health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}
