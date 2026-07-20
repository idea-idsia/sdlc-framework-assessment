import logging
from .database_manager import DatabaseManager
logging.basicConfig(level=logging.DEBUG)
def main():
    db = DatabaseManager()
    while True:
        print("1. Add new ticket")
        print("2. Update ticket status")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            category = input("Enter ticket category: ")
            description = input("Enter ticket description: ")
            db.insert_ticket({"category": category, "description": description})
            print("Ticket added successfully.")
        elif choice == "2":
            id_ = int(input("Enter the ID of the ticket to update: "))
            new_status = input("Enter the new status (resolved/closed): ")
            db.update_ticket_status(id_, new_status)
            print("Ticket status updated successfully.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()