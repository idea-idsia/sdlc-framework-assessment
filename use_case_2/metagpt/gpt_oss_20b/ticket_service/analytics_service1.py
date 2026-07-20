## analytics_service1.py
"""
Analytics Service 1 – Count open tickets in a date range.

This module implements a small Flask application that exposes a single
endpoint `/open_tickets`.  The endpoint accepts two query parameters,
`start` and `end`, both in ISO‑8601 date format (`YYYY-MM-DD`).  It
returns the number of tickets whose status is ``open`` and whose
creation timestamp falls within the inclusive range.

The service uses :class:`TicketRepository` from ``db.py`` to fetch
tickets from the SQLite database.  No changes to the public API of
`TicketRepository` are required; the service simply filters the
tickets returned by :meth:`TicketRepository.list` in memory.

Typical usage:
    $ python analytics_service1.py
    * Running on http://0.0.0.0:5001/open_tickets?start=2023-01-01&end=2023-01-31
"""

from __future__ import annotations

import datetime
from datetime import date, datetime as dt
from typing import Any, Dict

from flask import Flask, jsonify, request, Response
from db import TicketRepository, Ticket  # Import domain entities and repository

# --------------------------------------------------------------------------- #
# Flask application
# --------------------------------------------------------------------------- #
app: Flask = Flask(__name__)

# --------------------------------------------------------------------------- #
# Helper functions
# --------------------------------------------------------------------------- #
def _parse_date(value: str) -> date:
    """
    Parse an ISO‑8601 date string into a :class:`datetime.date` object.

    Parameters
    ----------
    value : str
        Date string in the format `YYYY-MM-DD`.

    Returns
    -------
    datetime.date
        Parsed date.

    Raises
    ------
    ValueError
        If the string does not match the expected format.
    """
    try:
        parsed: date = datetime.datetime.strptime(value, "%Y-%m-%d").date()
    except Exception as exc:  # pragma: no cover
        raise ValueError(f"Invalid date format for '{value}'. Expected YYYY-MM-DD.") from exc
    return parsed

def _count_open_tickets(start: date, end: date) -> int:
    """
    Count tickets with status ``open`` whose creation timestamp is
    between *start* and *end* (inclusive).

    Parameters
    ----------
    start : datetime.date
        Lower bound of the date range.
    end : datetime.date
        Upper bound of the date range.

    Returns
    -------
    int
        Number of matching tickets.
    """
    # Ensure start <= end
    if start > end:
        raise ValueError("Start date must be on or before end date.")

    repo: TicketRepository = TicketRepository()  # default path `./data/tickets.db`
    # Retrieve all open tickets; filtering by date is done in Python
    open_tickets: list[Ticket] = repo.list(filters={"status": "open"})

    # Convert date bounds to datetime objects at midnight for comparison
    start_dt: dt = dt.combine(start, dt.min.time())
    end_dt: dt = dt.combine(end, dt.max.time())

    # Count tickets whose created_at falls within the inclusive range
    count: int = sum(
        1
        for ticket in open_tickets
        if start_dt <= ticket.created_at <= end_dt
    )
    return count

# --------------------------------------------------------------------------- #
# Flask route
# --------------------------------------------------------------------------- #
@app.route("/open_tickets", methods=["GET"])
def open_tickets_endpoint() -> Response:
    """
    HTTP GET endpoint that returns the number of open tickets between
    two dates.

    Query Parameters
    ----------------
    start : str
        Start date in ISO format (YYYY-MM-DD).
    end : str
        End date in ISO format (YYYY-MM-DD).

    Returns
    -------
    Response
        JSON payload ``{"count": <int>}`` on success or a 400 error
        with an ``error`` field on failure.
    """
    # Retrieve query parameters
    start_str: str | None = request.args.get("start")
    end_str: str | None = request.args.get("end")

    # Validate presence
    if start_str is None or end_str is None:
        error_msg: str = "Both 'start' and 'end' query parameters are required."
        return jsonify({"error": error_msg}), 400

    # Parse dates
    try:
        start_date: date = _parse_date(start_str)
        end_date: date = _parse_date(end_str)
    except ValueError as exc:  # pragma: no cover
        return jsonify({"error": str(exc)}), 400

    # Compute count
    try:
        count: int = _count_open_tickets(start_date, end_date)
    except Exception as exc:  # pragma: no cover
        # Unexpected error – return 500 with a generic message
        return jsonify({"error": "Internal server error."}), 500

    return jsonify({"count": count}), 200

# --------------------------------------------------------------------------- #
# Application entry point
# --------------------------------------------------------------------------- #
if __name__ == "__main__":  # pragma: no cover
    # Default host and port for the service
    DEFAULT_HOST: str = "0.0.0.0"
    DEFAULT_PORT: int = 5001
    app.run(host=DEFAULT_HOST, port=DEFAULT_PORT)
