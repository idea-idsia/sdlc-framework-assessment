# Create API endpoints for interacting with the database
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Ticket(BaseModel):
    id: int
    status: str
    description: str
    category: str
    opening_date: str
    last_modification_date: str
    closing_date: str

@app.post("/tickets")
def create_ticket(ticket: Ticket):
    # Implement the logic to insert a new ticket into the database
    cursor.execute("""
        INSERT INTO tickets (id, status, description, category, opening_date, last_modification_date, closing_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (ticket.id, ticket.status, ticket.description, ticket.category, ticket.opening_date, ticket.last_modification_date, ticket.closing_date))
    cnx.commit()
    return {"message": "Ticket created successfully"}

@app.get("/tickets")
def get_tickets():
    # Implement the logic to retrieve all tickets from the database
    cursor.execute("SELECT * FROM tickets;")
    tickets = cursor.fetchall()
    return {"tickets": tickets}

@app.put("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, ticket: Ticket):
    # Implement the logic to update an existing ticket in the database
    cursor.execute("""
        UPDATE tickets SET status = %s, description = %s, category = %s, last_modification_date = %s WHERE id = %s;
    """, (ticket.status, ticket.description, ticket.category, ticket.last_modification_date, ticket_id))
    cnx.commit()
    return {"message": "Ticket updated successfully"}

@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    # Implement the logic to delete a ticket from the database
    cursor.execute("DELETE FROM tickets WHERE id = %s;", (ticket_id,))
    cnx.commit()
    return {"message": "Ticket deleted successfully"}