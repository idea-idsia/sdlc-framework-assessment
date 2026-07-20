CREATE TABLE tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    category TEXT CHECK(category IN ('facility_management', 'technical_it', 'services_complaints')) NOT NULL,
    status TEXT CHECK(status IN ('open', 'active', 'closed')) NOT NULL DEFAULT 'open',
    opening_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_modification_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    closing_date DATETIME
);

CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id INTEGER NOT NULL,
    message TEXT NOT NULL,
    user_type TEXT CHECK(user_type IN ('helpdesk', 'simple')) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ticket_id) REFERENCES tickets (id)
);