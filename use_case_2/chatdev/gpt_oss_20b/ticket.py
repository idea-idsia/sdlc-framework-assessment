'''
Defines the Ticket data model.
'''
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
@dataclass
class Ticket:
    """
    Data class that represents a support ticket.
    Attributes
    ----------
    id : int
        Auto‑generated unique identifier.
    description : str
        Description of the problem.
    category : str
        One of: 'facility', 'technical', 'services'.
    status : str
        Current status: 'open', 'active', or 'closed'.
    open_date : str
        ISO‑formatted timestamp when the ticket was created.
    last_mod_date : str
        ISO‑formatted timestamp of the last modification.
    close_date : Optional[str]
        ISO‑formatted timestamp when the ticket was closed, or None.
    messages : List[str]
        List of message texts attached to the ticket.
    """
    id: int = field(default=None)
    description: str = ""
    category: str = ""
    status: str = "open"
    open_date: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    last_mod_date: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    close_date: Optional[str] = None
    messages: List[str] = field(default_factory=list)