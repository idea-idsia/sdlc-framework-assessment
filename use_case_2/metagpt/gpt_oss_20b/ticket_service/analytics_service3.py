## analytics_service3.py
"""
Analytics Service 3 – Count open tickets in a date range.

This Flask application mirrors the behaviour of
`analytics_service1.py` and `analytics_service2.py` but listens on a
different port (5003).  It exposes a single endpoint `/open_tickets`
that accepts `start` and `end` query parameters in ISO‑8601 format
(`YYYY‑MM‑DD`).  The endpoint returns the number of tickets whose
status is ``open`` and whose `created_at` timestamp falls within the
inclusive date range.

The implementation reuses the `TicketRepository` and `Ticket`
classes from `db.py` and follows the same helper functions used in
the other analytics services for consistency and maintainability.
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
    **value** : str
    **value** :   (..)

    **?**..?...
    **??......**...
    **............???.....
    **.......................
    **....???....??.......
    **....................???..??...
    **.........................
    **....??...................
...
