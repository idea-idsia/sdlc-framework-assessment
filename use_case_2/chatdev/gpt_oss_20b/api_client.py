"""
Minimal client for communicating with the Flask microservice.
The client is not exercised by the tests, but it is kept simple
to avoid unnecessary dependencies.
"""
import requests
from typing import Any, Dict
class APIClient:
    """Very small wrapper around `requests` to talk to the microservice."""
    def __init__(self, base_url: str = "http://127.0.0.1:5000"):
        self.base_url = base_url
    # ------------------------------------------------------------------
    def get_open_tickets(self) -> Dict[str, Any]:
        """Return the number of open tickets from the microservice."""
        url = f"{self.base_url}/open_tickets"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    # ------------------------------------------------------------------
    def get_average_resolution_time(self) -> Dict[str, Any]:
        """Return the average resolution time (hours) from the microservice."""
        url = f"{self.base_url}/average_resolution_time"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    # ------------------------------------------------------------------
    def get_active_tickets_by_category(self) -> Dict[str, Any]:
        """Return a dictionary of active tickets per category."""
        url = f"{self.base_url}/active_tickets_by_category"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()