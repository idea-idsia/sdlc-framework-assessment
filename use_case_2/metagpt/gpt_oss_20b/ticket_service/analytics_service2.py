## analytics_service2.py
"""
Analytics Service 2 – Count open tickets in a date range.

This Flask application mirrors the behaviour of
`analytics_service1.py` but listens on a different port
(5002).  It exposes a single endpoint `/open_tickets` that accepts
`start` and `end` query parameters in ISO‑8601 format
(`YYYY-MM-DD`).  The endpoint returns the number of tickets whose
status is ``open`` and whose `created_at` timestamp falls within the
inclusive date range.

The implementation reuses the `TicketRepository` and `Ticket`
classes from `db.py` and follows the same helper functions used in
`analytics_service1.py` for consistency and maintainability.
"""

from __future__ import annotations

import datetime
from datetime import date, datetime as dt
from typing import Any, Dict

from flask import Flask, jsonify, request, Response
from db import TicketRepository, Ticket  # Domain entities and repository

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
        raise ValueError(
            f"Invalid date format for '{value}'. Expected YYYY-MM-DD."
        ) from exc
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

    Raises
    ------
    ValueError
        If *start* is after *end*.
    """
    if start > end:
        raise ValueError("Start date must not be after end date.")

    repo = TicketRepository()
    # Convert dates to full datetime objects for inclusive comparison
    start_dt: dt = dt.combine(start, dt.min.time())
    end_dt: dt = dt.combine(end, dt.max.time())

    # Retrieve all open tickets once and count those within the range
    open_tickets: list[Ticket] = repo.get_tickets_by_status("open")
    return sum(
        1
        for ticket in open_tickets
        if start_dt <= ticket.created_at <= end_dt
    )


# --------------------------------------------------------------------------- #
# Route definitions
# --------------------------------------------------------------------------- #
@app.route("/open_tickets", methods=["GET"])
def open_tickets_endpoint() -> Response:
    """
    HTTP GET handler for `/open_tickets`.

    Expects `start` and `end` query parameters.  Returns a JSON
    payload of the form ``{"count": <int>}``.  Errors are reported
    with appropriate HTTP status codes and JSON error messages.
    """
    start_str: str | None = request.args.get("start")
    end_str: str | None = request.args.get("end")

    if not start_str or not end_str:
        return (
            jsonify({"error": "Missing 'start' or 'end' query parameter."}),
            400,
        )

    try:
        start_date: date = _parse_date(start_str)
        end_date: date = _parse_date(end_str)
    except ValueError as ve:  # pragma: no cover
        return jsonify({"error": str(ve)}), 400

    try:
        count: int = _count_open_tickets(start_date, end_date)
    except Exception as exc:  # pragma: no cover
        # Unexpected server error – log if desired, but keep response generic
        return jsonify({"error": "Internal server error."}), 500

    return jsonify({"count": count}), 200


# --------------------------------------------------------------------------- #
# Application entry point
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    # Default host and port for the containerised service
    DEFAULT_HOST: str = "0.0.0.0"
    DEFAULT_PORT: int = 5002

    # Run the Flask development server in a production‑friendly mode.
    # In a real deployment, a WSGI server (Gunicorn, uWSGI, etc.) would
    # be preferred, but this configuration is sufficient for the
    # containerised environment used by the project.
    app.run(
        host=DEFAULT_HOST,
        port=DEFAULT_PORT,
        debug=False,
        use_reloader=False,
        threaded=True,
    )
