import sqlite3

conn = sqlite3.connect("tickets.db")
cursor = conn.cursor()

# Create a table for tickets
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY,
        status TEXT NOT NULL,
        description TEXT NOT NULL,
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
""")

# Insert some sample data
cursor.execute("INSERT INTO tickets (status, description) VALUES (?, ?)", ("open", "Ticket 1"))
conn.commit()

if __name__ == "__main__":
    conn.close()