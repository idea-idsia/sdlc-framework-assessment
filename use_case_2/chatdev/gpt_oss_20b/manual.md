# Ticket‑Management Web Application  
*PowerPoint Manual (Markdown format)*  

---  

## 1. Overview  

This project implements a **ticket‑management** web application for a university campus.  
It is split into three logical layers:  

| Layer | Purpose | Implementation | Main Features |
|-------|---------|----------------|---------------|
| **Client UI** | Users (students, staff) & Helpdesk staff interact with tickets | `login_window.py`, `user_window.py`, `helpdesk_window.py`, `detail_window.py` | Create, view, edit tickets; exchange messages; change ticket status |
| **Persistence** | Stores tickets and messages | `database.py` (JSON based) | CRUD operations; simple in‑memory persistence |
| **Analytics Micro‑service** | Provides data‑visualisation & analysis for helpdesk staff | `microservice_server.py` (Flask) or `microservice.py` (FastAPI) | • Open‑ticket counter<br>• Average resolution time<br>• Active tickets per category |

> **NOTE** – The UI and persistence layers are completely independent of the analytics micro‑service.  
> The micro‑service reads the **SQLite** database (`tickets.db`) while the UI writes to a JSON file (`~/.ticket_db.json`).  
> If you need the analytics features you must run the micro‑service **after** migrating the data from JSON to SQLite (see *Data Migration* below).

---

## 2. Prerequisites  

| Item | Minimum Version | Install Instructions |
|------|-----------------|----------------------|
| Python | 3.9+ | `python3 -m ensurepip --upgrade` |
| pip | – | Already bundled with Python |
| Virtual environment (recommended) | – | `python -m venv venv` |
| Packages | See `requirements.txt` | `pip install -r requirements.txt` |

> **Tip** – Always activate the virtual environment before running any commands:  
> ```bash
> source venv/bin/activate   # Linux / macOS
> venv\Scripts\activate.bat  # Windows
> ```

---

## 3. Project Structure  

```
ticket-app/
├── database.py            # In‑memory persistence (JSON)
├── detail_window.py       # Ticket detail view
├── helpdesk_window.py     # Helpdesk helper window
├── login_window.py        # Role selection (login mock)
├── main.py                # Application entry point
├── microservice_server.py # Flask analytics micro‑service
├── microservice.py        # FastAPI analytics micro‑service
├── ticket.py              # Ticket data model
├── user_window.py         # User‑side ticket UI
└── requirements.txt       # Dependencies
```

---

## 4. Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-org/ticket-app.git
   cd ticket-app
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate.bat
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Install the analytics micro‑service**  
   - **Flask** (default)  
     ```bash
     pip install Flask
     ```
   - **FastAPI** (alternative)  
     ```bash
     pip install fastapi uvicorn
     ```

---

## 5. Running the Application  

### 5.1. Start the Analytics Micro‑service  

> **Flask (default)**  
> ```bash
> python microservice_server.py
> ```
> *The service listens on http://127.0.0.1:5000.*

> **FastAPI (alternative)**  
> ```bash
> uvicorn microservice:app --reload
> ```
> *The service listens on http://127.0.0.1:8000.*

> **Important** – The micro‑service expects a SQLite database named `tickets.db`.  
> If you plan to use analytics, **create and populate** this database (see *Data Migration*).

### 5.2. Launch the Ticket‑Management UI  

```bash
python main.py
```

A small *Login* window pops up.  

| Role | What you can do | UI components |
|------|-----------------|---------------|
| **Customer** | • Create a new ticket<br>• View / edit own *open* or *active* tickets | `UserWindow` – ticket list, *Create Ticket* button |
| **Helpdesk** | • View all tickets (open, active, closed)<br>• Change ticket status (open→active→closed)<br>• Post messages | `HelpDeskWindow` – ticket ID entry, comment box, *Post* button |

> **Tip** – The *Helpdesk* window is a simple popup that can be opened from the main UI by clicking *Post* (or you can launch it manually with `HelpDeskWindow`).

---

## 6. Using the Application  

1. **Login**  
   *Select a role* (Customer / Helpdesk) and click **Login**.  

2. **Customer Flow**  
   1. In the main window, click **Create Ticket**.  
      *A new ticket is created with a random UUID, category “facility”, and status “open”.*  
   2. Select the ticket from the list to open its **Detail Window**.  
   3. In the detail window, you can view the description, category, status, and post comments.  
   4. To *edit* the ticket, simply modify the comment field and click **Post Comment**.  

3. **Helpdesk Flow**  
   1. Use the **HelpDeskWindow** to post messages on any ticket (by entering its ID).  
   2. When a ticket is *active*, you can change its status:  
      - In the detail window, change the `status` field (not exposed in the UI – you’ll need to tweak `detail_window.py` or add a new button).  
      - The micro‑service will automatically pick up the change once the ticket is persisted.  

4. **Analytics (Optional)**  
   1. Open a browser or a REST client (Postman, curl, etc.).  
   2. Make GET requests to the endpoints:  
      - `GET http://127.0.0.1:5000/open_tickets`  
      - `GET http://127.0.0.1:5000/average_resolution_time`  
      - `GET http://127.0.0.1:5000/active_tickets_by_category`  
   3. The responses contain JSON objects that can be plotted in external tools (Excel, Grafana, etc.).

---

## 7. Data Migration (JSON → SQLite)  

If you want to use the analytics micro‑service, you need a SQLite DB.  

1. **Create the database schema**  
   ```sql
   CREATE TABLE tickets (
       ticket_id INTEGER PRIMARY KEY,
       description TEXT,
       category TEXT,
       status TEXT,
       opened TEXT,
       closed TEXT
   );
   CREATE TABLE messages (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       ticket_id INTEGER,
       message TEXT,
       timestamp TEXT,
       FOREIGN KEY(ticket_id) REFERENCES tickets(ticket_id)
   );
   ```
2. **Export JSON data**  
   ```bash
   python - <<'PY'
   from database import DatabaseHandler
   db = DatabaseHandler()
   with open('tickets.json', 'w') as f:
       import json, datetime
       json.dump({"tickets": db.tickets, "messages": db.messages}, f, indent=2)
   PY
   ```
3. **Import into SQLite**  
   ```bash
   sqlite3 tickets.db < import.sql
   ```
   *(Replace `import.sql` with a script that reads the JSON file and inserts rows.)*  

> *The migration script is not shipped with the repo; write a small Python routine that reads `tickets.json` and inserts into `tickets.db`.*

---

## 8. Extending the Application  

| Feature | How to Add |
|---------|------------|
| **Better UI** | Replace `tkinter` with PyQt or Kivy for richer graphics. |
| **Real Authentication** | Integrate Flask‑Login or FastAPI OAuth2. |
| **Persist to SQLite** | Refactor `database.py` to use SQLite directly. |
| **Message threading** | Add message timestamps and user IDs. |
| **Unit tests** | Use `unittest` or `pytest` to cover database CRUD and UI callbacks. |
| **Dockerization** | Create a Dockerfile that installs dependencies and runs `main.py`. |

---

## 9. Troubleshooting  

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| *Tkinter window freezes* | Blocking call in the main thread (e.g., long DB operation). | Run DB ops in a separate thread or use `after()` callbacks. |
| *Micro‑service returns 500* | Missing SQLite file or wrong table schema. | Verify `tickets.db` exists and matches the expected schema. |
| *Tickets not persisting* | File permissions on `~/.ticket_db.json`. | Ensure write permissions or change the file path in `database.py`. |
| *Python 3.10 error* | Incompatible `dataclasses` usage. | Use `pip install dataclasses` for older Python or update code. |

---

## 10. License & Credits  

- **License** – MIT (see `LICENSE` file).  
- **Dependencies** – See `requirements.txt`.  
- **Credits** – Inspired by typical campus help‑desk systems and open‑source ticket trackers.  

---  

**Enjoy building and expanding your campus ticket‑management system!**