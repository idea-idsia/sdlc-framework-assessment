from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class TicketBase(BaseModel):
    category: str
    description: str

class TicketCreate(TicketBase):
    user_id: int  # who reported

class TicketInDB(TicketBase):
    id: int
    user_id: int
    status: str
    open_ts: datetime
    last_mod_ts: datetime
    close_ts: Optional[datetime]

class TicketResponse(TicketInDB):
    messages: List["MessageInDB"] = []

class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
    ticket_id: int
    sender_id: int

class MessageInDB(MessageBase):
    id: int
    ticket_id: int
    sender_id: int
    ts: datetime