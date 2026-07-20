## db.py
"""
Database layer for the help‑desk ticketing system.

This module defines the domain entities (`Ticket`, `Message`) and their
repositories (`TicketRepository`, `MessageRepository`).  All database
operations are performed against a single SQLite file located at
``./data/tickets.db`` by default.  The implementation focuses on correctness,
type safety, and minimal side‑effects.

Key improvements over the original version:

* **Single‑connection inserts** – `create` and `add` now use the same
  connection that performs the INSERT, retrieving the primary key via
  ``cursor.lastrowid``.  This guarantees the correct ID is returned.
* **Mutable default avoidance** – ``TicketRepository.list`` accepts
  ``filters: Optional[Dict[str, object]] = None`` and normalises it to an
  empty dict internally.
* **Explicit context management** – All database interactions are wrapped
  in ``with sqlite3.connect(...)`` blocks to ensure proper cleanup.
* **Consistent row factory** – ``sqlite3.Row`` is set for every connection
  that fetches data, enabling dictionary‑style access to columns.
* **Type‑annotated public API** – All public methods expose clear type
  hints, improving IDE support and static analysis.

The module is self‑contained and requires only the standard library.
"""

from __future__ import annotations

import os
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional

# --------------------------------------------------------------------------- #
# Domain entities
# --------------------------------------------------------------------------- #

class Ticket:
    """
    Represents a support ticket.

    Parameters
    ----------
    title : str
        Ticket title.
    description : str
        Full description.
    category : str
        Ticket category.
    id : Optional[int], default None
        Database primary key.
    status : str, default "open"
        Current status.
    created_at : Optional[datetime], default now
        Creation timestamp.
    updated_at : Optional[datetime], default now
        Last update timestamp.
    closed_at : Optional[datetime], default None
        Closure timestamp if closed.
    """

    def __init__(
        self,
        title: str,
        description: str,
        category: str,
        *,
        id: Optional[int] = None,
        status: str = "open",
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        closed_at: Optional[datetime] = None,
    ) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.status = status
        now = datetime.utcnow()
        self.created_at = created_at or now
        self.updated_at = updated_at or now
        self.closed_at = closed_at

    def to_dict(self) -> Dict[str, object]:
        """Return a JSON‑serialisable dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "closed_at": self.closed_at.isoformat() if self.closed_at else None,
        }

    def __repr__(self) -> str:  # pragma: no cover
        return f"<Ticket id={self.id!r} title={self.title!r} status={self.status!r}>"

class Message:
    """
    Represents a message attached to a ticket.

    Parameters
    ----------
    ticket_id : int
        Owning ticket ID.
    author_role : str
        Role of the author.
    content : str
        Message body.
    id : Optional[int], default None
        Database primary key.
    timestamp : Optional[datetime], default now
        Creation timestamp.
    """

    def __init__(
        self,
        ticket_id: int,
        author_role: str,
        content: str,
        *,
        id: Optional[int] = None,
        timestamp: Optional[datetime] = None,
    ) -> None:
        self.id = id
        self.ticket_id = ticket_id
        self.author_role = author_role
        self.content = content
        self.timestamp = timestamp or datetime.utcnow()

    def to_dict(self) -> Dict[str, object]:
        """Return a JSON‑serialisable dictionary representation."""
        return {
            "id": self.id,
            "ticket_id": self.ticket_id,
            "author_role": self.author_role,
            "content": self.content,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
        }

    def __repr__(self) -> str:  # pragma: no cover
        return f"<Message id={self.id!r} ticket_id={self.ticket_id!r} author={self.author_role!r}>"

# --------------------------------------------------------------------------- #
# Repository implementations
# --------------------------------------------------------------------------- #

class TicketRepository:
    """
    Repository for CRUD operations on tickets.

    Parameters
    ----------
    db_path : str, optional
        Path to the SQLite database file.  Defaults to ``./data/tickets.db``.
    """

    def __init__(self, db_path: str = "./data/tickets.db") -> None:
        self._db_path = Path(db_path).expanduser().resolve()
        self._ensure_db()

    # --------------------------------------------------------------------- #
    # Internal helpers
    # --------------------------------------------------------------------- #

    def _ensure_db(self) -> None:
        """Create database file and tables if they do not exist."""
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(self._db_path)
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS tickets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    category TEXT NOT NULL,
                    status TEXT NOT NULL CHECK(status IN ('open','active','closed')),
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    closed_at TEXT
                )
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ticket_id INTEGER NOT NULL,
                    author_role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
                )
                """
            )
            conn.commit()
        finally:
            conn.close()

    def _execute(
        self,
        query: str,
        params: Iterable[object] = (),
        fetchone: bool = False,
        fetchall: bool = False,
    ) -> Optional[sqlite3.Row]:
        """Execute a query and return results if requested."""
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        try:
            cur = conn.cursor()
            cur.execute(query, params)
            if fetchone:
                return cur.fetchone()
            if fetchall:
                return cur.fetchall()
            return None
        finally:
            conn.close()

    # --------------------------------------------------------------------- #
    # Public API
    # --------------------------------------------------------------------- #

    def create(self, ticket: Ticket) -> int:
        """Persist a new ticket and return its database ID."""
        if ticket.id is not None:
            raise ValueError("Ticket already has an ID; cannot create.")
        with sqlite3.connect(self._db_path) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO tickets
                (title, description, category, status, created_at, updated_at, closed_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    ticket.title,
                    ticket.description,
                    ticket.category,
                    ticket.status,
                    ticket.created_at.isoformat(),
                    ticket.updated_at.isoformat(),
                    ticket.closed_at.isoformat() if ticket.closed_at else None,
                ),
            )
            conn.commit()
            ticket_id = cur.lastrowid
        ticket.id = ticket_id
        return ticket_id

    def get_by_id(self, ticket_id: int) -> Optional[Ticket]:
        """Retrieve a ticket by its primary key."""
        row = self._execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,), fetchone=True)
        return self._row_to_ticket(row) if row else None

    def update(self, ticket: Ticket) -> None:
        """Update an existing ticket."""
        if ticket.id is None:
            raise ValueError("Ticket must have an ID to be updated.")
        # Ensure closed_at is set appropriately
        if ticket.status == "closed" and ticket.closed_at is None:
            ticket.closed_at = datetime.utcnow()
        elif ticket.status != "closed":
            ticket.closed_at = None
        ticket.updated_at = datetime.utcnow()
        with sqlite3.connect(self._db_path) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(
                """
                UPDATE tickets
                SET title = ?, description = ?, category = ?, status = ?, updated_at = ?, closed_at = ?
                WHERE id = ?
                """,
                (
                    ticket.title,
                    ticket.description,
                    ticket.category,
                    ticket.status,
                    ticket.updated_at.isoformat(),
                    ticket.closed_at.isoformat() if ticket.closed_at else None,
                    ticket.id,
                ),
            )
            conn.commit()

    def list(self, filters: Optional[Dict[str, object]] = None) -> List[Ticket]:
        """
        List tickets applying optional filters.

        Supported filter keys:
            - status: List[str] of statuses to include
            - category: str
            - author_role: str (not used here but kept for compatibility)
        """
        filters = filters or {}
        base = "SELECT * FROM tickets"
        clauses: List[str] = []
        params: List[object] = []

        status_filter = filters.get("status")
        if status_filter:
            if isinstance(status_filter, Iterable) and not isinstance(status_filter, str):
                placeholders = ", ".join("?" for _ in status_filter)
                clauses.append(f"status IN ({placeholders})")
                params.extend(status_filter)
            else:
                clauses.append("status = ?")
                params.append(status_filter)

        category_filter = filters.get("category")
        if category_filter:
            clauses.append("category = ?")
            params.append(category_filter)

        if clauses:
            base += " WHERE " + " AND ".join(clauses)

        base += " ORDER BY created_at DESC"

        rows = self._execute(base, tuple(params), fetchall=True)
        return [self._row_to_ticket(row) for row in rows] if rows else []

    # --------------------------------------------------------------------- #
    # Private helpers
    # --------------------------------------------------------------------- #

    @staticmethod
    def _row_to_ticket(row: sqlite3.Row) -> Ticket:
        """Convert a sqlite3.Row to a Ticket instance."""
        return Ticket(
            id=row["id"],
            title=row["title"],
            description=row["description"],
            category=row["category"],
            status=row["status"],
            created_at=datetime.fromisoformat(row["created_at"]),
            updated_at=datetime.fromisoformat(row["updated_at"]),
            closed_at=datetime.fromisoformat(row["closed_at"]) if row["closed_at"] else None,
        )

class MessageRepository:
    """
    Repository for CRUD operations on messages.

    Parameters
    ----------
    db_path : str, optional
        Path to the SQLite database file.  Defaults to ``./data/tickets.db``.
    """

    def __init__(self, db_path: str = "./data/tickets.db") -> None:
        self._db_path = Path(db_path).expanduser().resolve()
        # Ensure the database exists; reuse TicketRepository's logic
        TicketRepository(db_path)

    # --------------------------------------------------------------------- #
    # Internal helpers
    # --------------------------------------------------------------------- #

    def _execute(
        self,
        query: str,
        params: Iterable[object] = (),
        fetchone: bool = False,
        fetchall: bool = False,
    ) -> Optional[sqlite3.Row]:
        """Execute a query and return results if requested."""
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        try:
            cur = conn.cursor()
            cur.execute(query, params)
            conn.commit()
            if fetchone:
                return cur.fetchone()
            if fetchall:
                return cur.fetchall()
            return None
        finally:
            conn.close()

    # --------------------------------------------------------------------- #
    # Public API
    # --------------------------------------------------------------------- #

    def add(self, message: Message) -> int:
        """Persist a new message and return its database ID."""
        if message.id is not None:
            raise ValueError("Message already has an ID; cannot add.")
        with sqlite3.connect(self._db_path) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO messages
                (ticket_id, author_role, content, timestamp)
                VALUES (?, ?, ?, ?)
                """,
                (
                    message.ticket_id,
                    message.author_role,
                    message.content,
                    message.timestamp.isoformat(),
                ),
            )
            conn.commit()
            message_id = cur.lastrowid
        message.id = message_id
        return message_id

    def list_by_ticket(self, ticket_id: int) -> List[Message]:
        """Return all messages belonging to a specific ticket."""
        query = """
            SELECT * FROM messages
            WHERE ticket_id = ?
            ORDER BY timestamp ASC
        """
        rows = self._execute(query, (ticket_id,), fetchall=True)
        return [self._row_to_message(row) for row in rows] if rows else []

    # --------------------------------------------------------------------- #
    # Private helpers
    # --------------------------------------------------------------------- #

    @staticmethod
    def _row_to_message(row: sqlite3.Row) -> Message:
        """Convert a sqlite3.Row to a Message instance."""
        return Message(
            id=row["id"],
            ticket_id=row["ticket_id"],
            author_role=row["author_role"],
            content=row["content"],
            timestamp=datetime.fromisoformat(row["timestamp"]),
        )

# --------------------------------------------------------------------------- #
# Public API
# --------------------------------------------------------------------------- #

__all__ = [
    "Ticket",
    "Message",
    "TicketRepository",
    "MessageRepository",
]
