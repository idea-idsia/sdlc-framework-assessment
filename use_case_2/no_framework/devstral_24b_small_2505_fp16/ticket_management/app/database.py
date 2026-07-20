# app/database.py

import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()

    # Create tickets table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            category TEXT NOT NULL CHECK( category IN ('facility management', 'technical IT', 'services complaints') ),
            status TEXT NOT NULL DEFAULT 'open',
            opening_date TEXT NOT NULL,
            last_modification_date TEXT,
            closing_date TEXT
        )
    ''')

    # Create messages table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id INTEGER NOT NULL,
            message_text TEXT NOT NULL,
            sender TEXT NOT NULL CHECK( sender IN ('user', 'helpdesk') ),
            timestamp TEXT NOT NULL,
            FOREIGN KEY(ticket_id) REFERENCES tickets(id)
        )
    ''')

    conn.commit()
    conn.close()

def insert_ticket(description, category):
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO tickets (description, category, opening_date, last_modification_date)
        VALUES (?, ?, ?, ?)
    ''', (description, category, datetime.now().isoformat(), datetime.now().isoformat()))

    conn.commit()
    ticket_id = cursor.lastrowid
    conn.close()

    return ticket_id

def get_tickets(status=None):
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()

    if status:
        cursor.execute("SELECT * FROM tickets WHERE status=?", (status,))
    else:
        cursor.execute("SELECT * FROM tickets")

    tickets = cursor.fetchall()
    conn.close()

    return tickets

def update_ticket(ticket_id, description=None, category=None, status=None):
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()

    updates = []
    params = []

    if description:
        updates.append("description=?")
        params.append(description)
    if category:
        updates.append("category=?")
        params.append(category)
    if status:
        updates.append("status=?, last_modification_date=?")
        params.extend([status, datetime.now().isoformat()])
    else:
        updates.append("last_modification_date=?")
        params.append(datetime.now().isoformat())

    params.append(ticket_id)

    cursor.execute(f'UPDATE tickets SET {", ".join(updates)} WHERE id=?', params)
    conn.commit()
    conn.close()

def insert_message(ticket_id, message_text, sender):
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO messages (ticket_id, message_text, sender, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (ticket_id, message_text, sender, datetime.now().isoformat()))

    conn.commit()
    conn.close()

def get_messages(ticket_id):
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages WHERE ticket_id=?", (ticket_id,))
    messages = cursor.fetchall()
    conn.close()

    return messages

if __name__ == "__main__":
    init_db()