'''
A very small in‑memory persistence layer.
'''
import uuid
from datetime import datetime
from typing import List, Dict, Optional
import os
from ticket import Ticket  # Reuse the single Ticket definition
class DatabaseHandler:
    """
    Provides CRUD operations for tickets and messages.
    Data is stored in a JSON file in the user's home directory.
    """
    def __init__(self, filename: Optional[str] = None):
        if filename is None:
            home = os.path.expanduser("~")
            filename = os.path.join(home, ".ticket_db.json")
        self.filename = filename
        self.tickets: List[Dict] = []
        self.messages: List[Dict] = []
        self._load()
    # --------------------------------------------------------------
    def _load(self):
        """Load tickets and messages from the JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                data = f.read()
                if data:
                    import json
                    data_dict = json.loads(data)
                    self.tickets = data_dict.get("tickets", [])
                    self.messages = data_dict.get("messages", [])
        else:
            self.tickets = []
            self.messages = []
    # --------------------------------------------------------------
    def _save(self):
        """Persist tickets and messages to the JSON file."""
        import json
        data = {"tickets": self.tickets, "messages": self.messages}
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(json.dumps(data, indent=2))
    # --------------------------------------------------------------
    def get_all_tickets(self) -> List[Ticket]:
        """Return a list of Ticket dataclass instances."""
        tickets = []
        for t in self.tickets:
            tickets.append(
                Ticket(
                    id=t["ticket_id"],
                    description=t["description"],
                    category=t["category"],
                    status=t["status"],
                    open_date=t["opened"],
                    last_mod_date=t["opened"],
                    close_date=t.get("closed"),
                    messages=[],
                )
            )
        return tickets
    # --------------------------------------------------------------
    def get_ticket_by_id(self, ticket_id: int) -> Optional[Ticket]:
        """Retrieve a single ticket by its ID."""
        for t in self.tickets:
            if t["ticket_id"] == ticket_id:
                return Ticket(
                    id=t["ticket_id"],
                    description=t["description"],
                    category=t["category"],
                    status=t["status"],
                    open_date=t["opened"],
                    last_mod_date=t["opened"],
                    close_date=t.get("closed"),
                    messages=[],
                )
        return None
    # --------------------------------------------------------------
    def create_ticket(self, ticket: Ticket) -> None:
        """Create a new ticket record."""
        ticket_dict = {
            "ticket_id": ticket.id if ticket.id is not None else uuid.uuid4().int >> 64,
            "description": ticket.description,
            "category": ticket.category,
            "status": ticket.status,
            "opened": ticket.open_date,
            "closed": ticket.close_date,
        }
        self.tickets.append(ticket_dict)
        self._save()
    # --------------------------------------------------------------
    def add_message(self, ticket_id: int, message: str) -> None:
        """Add a message to a ticket."""
        self.messages.append(
            {
                "ticket_id": ticket_id,
                "message": message,
                "timestamp": datetime.utcnow().isoformat(),
            }
        )
        self._save()
    # --------------------------------------------------------------
    def update_ticket_status(self, ticket_id: int, status: str) -> None:
        """Update the status of a ticket."""
        for t in self.tickets:
            if t["ticket_id"] == ticket_id:
                t["status"] = status
                if status == "closed":
                    t["closed"] = datetime.utcnow().isoformat()
                else:
                    t["closed"] = None
                self._save()
                break