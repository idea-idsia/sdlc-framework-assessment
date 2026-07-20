# Import required libraries
import mysql.connector

# Establish a connection to the database
cnx = mysql.connector.connect(
    user='username',
    password='password',
    host='localhost',
    database='tickets'
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# Define the database schema
cursor.execute("""
    CREATE TABLE tickets (
        id INT PRIMARY KEY,
        status VARCHAR(50),
        description TEXT,
        category VARCHAR(50),
        opening_date DATETIME,
        last_modification_date DATETIME,
        closing_date DATETIME
    );
""")

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

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)