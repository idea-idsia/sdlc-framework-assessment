from fastapi import FastAPI, HTTPException
from sqlalchemy import func, extract
from models.ticket import Ticket, engine, SessionLocal
import datetime

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/ticket_count")
async def get_ticket_count(hours: int = None, days: int = None):
    db = SessionLocal()
    try:
        end_time = datetime.datetime.utcnow()
        if hours is not None:
            start_time = end_time - datetime.timedelta(hours=hours)
        elif days is not None:
            start_time = end_time - datetime.timedelta(days=days)
        else:
            raise HTTPException(status_code=400, detail="Either hours or days must be provided")

        count = db.query(func.count(Ticket.id)).filter(
            Ticket.status == 'open',
            Ticket.opening_date >= start_time
        ).scalar()

        return {"count": count}
    finally:
        db.close()

@app.get("/api/average_resolution_time")
async def average_resolution_time(db: SessionLocal = Depends(get_db)):
    # Implement Service 2 logic...
    pass

@app.get("/api/category_counts")
async def category_counts(db: SessionLocal = Depends(get_db)):
    # Implement Service 3 logic...
    pass