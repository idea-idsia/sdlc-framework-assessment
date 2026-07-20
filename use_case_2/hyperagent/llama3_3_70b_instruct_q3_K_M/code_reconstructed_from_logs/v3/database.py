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

# Create a table for messages exchanged under each ticket
cursor.execute("""
    CREATE TABLE messages (
        id INT PRIMARY KEY,
        ticket_id INT,
        message TEXT,
        sender VARCHAR(50),
        sent_at DATETIME,
        FOREIGN KEY (ticket_id) REFERENCES tickets(id)
    );
""")