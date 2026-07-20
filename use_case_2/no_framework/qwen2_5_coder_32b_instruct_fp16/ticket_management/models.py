import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'open',
            opening_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            last_modification_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            closing_date DATETIME
        )
    ''')
    conn.commit()
    conn.close()