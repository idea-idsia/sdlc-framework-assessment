from fastapi import FastAPI, HTTPException, Query
import uvicorn
from datetime import datetime, timedelta
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

from db import init_db, get_cursor
from models import (
    TicketCreate, TicketResponse, TicketInDB,
    MessageCreate, MessageInDB
)

app = FastAPI(title="Campus Ticket System")

init_db()

# ---------- Utility helpers ----------
def _row_to_ticket(row) -> TicketInDB:
    return TicketInDB(
        id=row[0], user_id=row[1], category=row[2], description=row[3],
        status=row[4], open_ts=row[5], last_mod_ts=row[6], close_ts=row[7]
    )

def _row_to_message(row) -> MessageInDB:
    return MessageInDB(
        id=row[0], ticket_id=row[1], sender_id=row[2], content=row[3], ts=row[4]
    )

# ---------- CRUD ----------
@app.post("/tickets/", response_model=TicketResponse)
def create_ticket(ticket: TicketCreate):
    with get_cursor() as cur:
        cur.execute(
            "INSERT INTO tickets (user_id, category, description) VALUES (?,?,?)",
            (ticket.user_id, ticket.category, ticket.description)
        )
        ticket_id = cur.lastrowid
        cur.execute("SELECT * FROM tickets WHERE id=?", (ticket_id,))
        t_row = cur.fetchone()
    return TicketResponse(**_row_to_ticket(t_row)._dict, messages=[])

@app.get("/tickets/{ticket_id}/", response_model=TicketResponse)
def get_ticket(ticket_id: int):
    with get_cursor() as cur:
        cur.execute("SELECT * FROM tickets WHERE id=?", (ticket_id,))
        t_row = cur.fetchone()
        if not t_row:
            raise HTTPException(404, "Ticket not found")
        cur.execute("SELECT * FROM messages WHERE ticket_id=?", (ticket_id,))
        messages = [_row_to_message(m) for m in cur.fetchall()]
    return TicketResponse(**_row_to_ticket(t_row)._dict, messages=messages)

@app.put("/tickets/{ticket_id}/status/")
def change_status(ticket_id: int, status: str = Query(...)):
    if status not in ("open","active","closed"):
        raise HTTPException(400, "Invalid status")
    with get_cursor() as cur:
        cur.execute("SELECT status FROM tickets WHERE id=?", (ticket_id,))
        old = cur.fetchone()
        if not old:
            raise HTTPException(404, "Ticket not found")
        cur.execute(
            "UPDATE tickets SET status=?, last_mod_ts=CURRENT_TIMESTAMP, close_ts=CASE WHEN ?='closed' THEN CURRENT_TIMESTAMP ELSE close_ts END WHERE id=?",
            (status, status, ticket_id)
        )
    return {"message": f"Ticket {ticket_id} status changed to {status}"}

@app.post("/messages/", response_model=MessageInDB)
def add_message(msg: MessageCreate):
    with get_cursor() as cur:
        cur.execute(
            "INSERT INTO messages (ticket_id, sender_id, content) VALUES (?,?,?)",
            (msg.ticket_id, msg.sender_id, msg.content)
        )
        msg_id = cur.lastrowid
        cur.execute("SELECT * FROM messages WHERE id=?", (msg_id,))
        row = cur.fetchone()
    # update ticket's last_mod_ts
    with get_cursor() as cur2:
        cur2.execute("UPDATE tickets SET last_mod_ts=CURRENT_TIMESTAMP WHERE id=?", (msg.ticket_id,))
    return _row_to_message(row)

# ---------- Analytics Micro‑services ----------
@app.get("/analytics/open-unclosed/{days:int}")
def open_unclosed(days: int):
    """# of tickets opened in the last X days that are still not closed."""
    since = datetime.utcnow() - timedelta(days=days)
    with get_cursor() as cur:
        cur.execute(
            "SELECT COUNT(*) FROM tickets WHERE open_ts >= ? AND status != 'closed'",
            (since.strftime("%Y-%m-%d %H:%M:%S"),)
        )
        count = cur.fetchone()[0]
    return {"days": days, "open_unclosed": count}

@app.get("/analytics/avg-resolution")
def avg_resolution():
    """Average resolution time per opening month."""
    df = pd.read_sql_query(
        "SELECT open_ts, close_ts FROM tickets WHERE status='closed'",
        f"sqlite:///{DB_PATH}"
    )
    df['open_ts'] = pd.to_datetime(df['open_ts'])
    df['close_ts'] = pd.to_datetime(df['close_ts'])
    df['month'] = df['open_ts'].dt.to_period('M')
    df['resolution'] = (df['close_ts'] - df['open_ts']).dt.total_seconds() / 3600
    res = df.groupby('month')['resolution'].mean().reset_index()
    return res.to_dict(orient="records")

@app.get("/analytics/active-cluster")
def active_cluster():
    """Cluster active tickets by category."""
    with get_cursor() as cur:
        cur.execute(
            "SELECT id, category FROM tickets WHERE status='active'"
        )
        rows = cur.fetchall()
    if not rows:
        return {"message": "No active tickets"}
    ids, categories = zip(*rows)
    # Encode categories numerically
    cat_to_int = {cat:i for i,cat in enumerate(set(categories))}
    cat_nums = np.array([cat_to_int[c] for c in categories]).reshape(-1,1)
    # KMeans (k=3 or fewer)
    k = min(3, len(set(categories)))
    km = KMeans(n_clusters=k, random_state=0).fit(cat_nums)
    clusters = km.labels_
    # Count per cluster
    cluster_counts = {f"cluster_{i}": int(clusters.tolist().count(i)) for i in range(k)}
    return cluster_counts