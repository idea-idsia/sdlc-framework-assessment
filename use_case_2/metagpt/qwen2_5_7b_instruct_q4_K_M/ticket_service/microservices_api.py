## microservices_api.py

from sqlalchemy.orm import Session
from .models import User, Ticket, DatabaseAPI  # Import data model definitions

class MicroservicesAPI:
    def __init__(self, db_api: DatabaseAPI):
        self.db_api = db_api

    def report_issue(self, username: str, issue: str) -> Ticket:
        user = self.db_api.get_user_by_username(username=username)
        if not user:
            raise ValueError("User not found")
        return user.report_issue(issue=issue)

    def modify_ticket(self, username: str, ticket_id: int, status: str) -> bool:
        user = self.db_api.get_user_by_username(username=username)
        if not user:
            raise ValueError("User not found")
        return user.modify_ticket(ticket_id=ticket_id, status=status)

    def view_tickets(self, status: str) -> list[Ticket]:
        # Placeholder for actual query logic
        return []

    def change_ticket_status(self, ticket_id: int, new_status: str) -> bool:
        # Placeholder for actual update logic
        return True

# Example usage of MicroservicesAPI (for testing purposes)
if __name__ == "__main__":
    db_api = DatabaseAPI()
    microservices_api = MicroservicesAPI(db_api=db_api)

    # Simulate reporting an issue
    ticket1 = microservices_api.report_issue(username="user1", issue="Network connectivity issue")
    print(f"Reported ticket ID: {ticket1.id}")

    # Simulate changing a ticket status
    success = microservices_api.change_ticket_status(ticket_id=ticket1.id, new_status="resolved")
    print(f"Ticket status updated: {success}")
