'''
FastAPI micro‑service that exposes analysis endpoints.
'''
from fastapi import FastAPI
import sqlite3
app = FastAPI()
def _db_connect():
    return sqlite3.connect('tickets.db')
@app.get("/open_tickets")
def open_tickets(period: str, value: int):
    """
    Return count of tickets still open within the given period (days/hours).
    """
    conn = _db_connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT COUNT(*)
        FROM tickets
        WHERE status IN ('open', 'active')
        AND open_date >= date('now', f'-{value} {period}')
    """)
    cnt = cur.fetchone()[0]
    conn.close()
    return {"count": cnt}
@app.get("/avg_resolution")
def avg_resolution():
    """
    Return average resolution time by month (in hours).
    """
    conn = _db_connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT strftime('%Y-%m', open_date) as month, AVG(julianday(close_date)-julianday(open_date))*24 as avg_hours
        FROM tickets
        WHERE status='closed'
        GROUP BY month
    """)
    rows = cur.fetchall()
    result = {row[0]: row[1] for row in rows}
    conn.close()
    return {"monthly": result}
@app.get("/active_by_category")
def active_by_category():
    """
    Return number of active tickets per category.
    """
    conn = _db_connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT category, COUNT(*) as cnt
        FROM tickets
        WHERE status='active'
        GROUP BY category
    """)
    rows = cur.fetchall()
    result = {row[0]: row[1] for row in rows}
    conn.close()
    return {"active_by_category": result}