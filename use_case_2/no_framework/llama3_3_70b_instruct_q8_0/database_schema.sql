CREATE TABLE tickets (
    id INTEGER PRIMARY KEY,
    description TEXT NOT NULL,
    category TEXT NOT NULL CHECK(category IN ('facility', 'it', 'services')),
    status TEXT NOT NULL CHECK(status IN ('open', 'active', 'closed')),
    opening_date DATE NOT NULL DEFAULT CURRENT_DATE,
    last_modification_date DATE NOT NULL DEFAULT CURRENT_DATE,
    closing_date DATE
);

CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    ticket_id INTEGER NOT NULL,
    message TEXT NOT NULL,
    sender TEXT NOT NULL CHECK(sender IN ('user', 'helpdesk')),
    date DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (ticket_id) REFERENCES tickets (id)
);