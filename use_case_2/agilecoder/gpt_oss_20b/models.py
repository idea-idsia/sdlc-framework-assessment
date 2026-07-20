'''
Data models for Ticket and Message with CRUD utilities.
'''
import datetime
from typing import List, Optional
from database import Database
class Ticket:
    STATUS_OPEN = 'open'
    STATUS_ACTIVE = 'active'
    STATUS_CLOSED = 'closed'
    CATEGORIES = [
        'facility management',
        'technical IT',
        'services complaints'
    ]
    def __init__(self, **kwargs):
        self.id: Optional[int] = kwargs.get('id')
        self.description: str = kwargs['description']
        self.category: str = kwargs['category']
        self.status: str = kwargs['status']
        self.opening_date: str = kwargs['opening_date']
        self.last_mod_date: str = kwargs['last_mod_date']
        self.closing_date: Optional[str] = kwargs.get('closing_date')
        self.created_by_role: str = kwargs['created_by_role']
    @classmethod
    def create(cls, description: str, category: str, created_by_role: str) -> 'Ticket':
        now = datetime.datetime.utcnow().isoformat()
        db = Database.instance()
        db.execute('''
            INSERT INTO tickets (description, category, status, opening_date,
                                 last_mod_date, created_by_role)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (description, category, cls.STATUS_OPEN, now, now, created_by_role))
        ticket_id = db.query('SELECT last_insert_rowid()')[0][0]
        return cls(id=ticket_id, description=description, category=category,
                   status=cls.STATUS_OPEN, opening_date=now,
                   last_mod_date=now, created_by_role=created_by_role)
    @classmethod
    def fetch_by_id(cls, ticket_id: int) -> Optional['Ticket']:
        rows = Database.instance().query(
            'SELECT * FROM tickets WHERE id = ?', (ticket_id,))
        if not rows:
            return None
        return cls(**rows[0])
    @classmethod
    def fetch_by_role_and_status(cls, role: str, statuses: List[str]) -> List['Ticket']:
        placeholders = ','.join('?' for _ in statuses)
        rows = Database.instance().query(f'''
            SELECT * FROM tickets
            WHERE created_by_role = ? AND status IN ({placeholders})
        ''', tuple([role] + statuses))
        return [cls(**row) for row in rows]
    @classmethod
    def fetch_by_status(cls, status: str) -> List['Ticket']:
        rows = Database.instance().query(
            'SELECT * FROM tickets WHERE status = ?', (status,))
        return [cls(**row) for row in rows]
    def refresh(self):
        fresh = Ticket.fetch_by_id(self.id)
        if fresh:
            self.__dict__.update(fresh.__dict__)
    def change_status(self, new_status: str, role: str = None):
        """
        Enforce role‑based permissions before changing ticket status.
        Only helpdesk staff may transition a ticket to CLOSED.
        """
        if new_status == Ticket.STATUS_CLOSED and role != 'helpdesk':
            raise PermissionError("Only helpdesk can close tickets")
        db = Database.instance()
        now = datetime.datetime.utcnow().isoformat()
        if new_status == Ticket.STATUS_CLOSED:
            db.execute('''
                UPDATE tickets SET status = ?, last_mod_date = ?, closing_date = ?
                WHERE id = ?
            ''', (new_status, now, now, self.id))
        else:
            db.execute('''
                UPDATE tickets SET status = ?, last_mod_date = ?
                WHERE id = ?
            ''', (new_status, now, self.id))
        self.status = new_status
        self.last_mod_date = now
        if new_status == Ticket.STATUS_CLOSED:
            self.closing_date = now
    def add_message(self, message: str, role: str):
        Message.create(ticket_id=self.id, role=role, message=message)
    def __repr__(self):
        return f"<Ticket {self.id}: {self.status}>"
class Message:
    def __init__(self, **kwargs):
        self.id: Optional[int] = kwargs.get('id')
        self.ticket_id: int = kwargs['ticket_id']
        self.role: str = kwargs['role']
        self.message: str = kwargs['message']
        self.timestamp: str = kwargs['timestamp']
    @classmethod
    def create(cls, ticket_id: int, role: str, message: str) -> 'Message':
        now = datetime.datetime.utcnow().isoformat()
        db = Database.instance()
        db.execute('''
            INSERT INTO messages (ticket_id, role, message, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (ticket_id, role, message, now))
        msg_id = db.query('SELECT last_insert_rowid()')[0][0]
        return cls(id=msg_id, ticket_id=ticket_id, role=role,
                   message=message, timestamp=now)
    @classmethod
    def fetch_by_ticket(cls, ticket_id: int) -> List['Message']:
        rows = Database.instance().query(
            'SELECT * FROM messages WHERE ticket_id = ?', (ticket_id,))
        return [cls(**row) for row in rows]