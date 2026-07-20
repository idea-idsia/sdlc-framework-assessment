import sqlite3

# Create a new SQLite database or connect to an existing one
conn = sqlite3.connect('tickets.db')

# Create a cursor object
cursor = conn.cursor()

# Create table for tickets
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY,
        description TEXT NOT NULL,
        category TEXT NOT NULL CHECK(category IN ('facility management', 'technical IT', 'services complaints')),
        status TEXT NOT NULL CHECK(status IN ('open', 'active', 'closed')),
        opening_date DATE NOT NULL DEFAULT CURRENT_DATE,
        last_modification_date DATE NOT NULL DEFAULT CURRENT_DATE,
        closing_date DATE
    )
''')

# Create table for users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        role TEXT NOT NULL CHECK(role IN ('helpdesk', 'user'))
    )
''')

# Create table for messages
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        ticket_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        message TEXT NOT NULL,
        date DATE NOT NULL DEFAULT CURRENT_DATE,
        FOREIGN KEY (ticket_id) REFERENCES tickets (id),
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()