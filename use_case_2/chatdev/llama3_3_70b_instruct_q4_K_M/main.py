Python
'''
This is the main file for the ticket management system.
It initializes the database and provides a menu-driven interface for users to interact with the system.
'''
import sqlite3
from database import Database
from helpdesk import HelpDesk
from microservices import Microservices
def main():
    # Initialize the database
    db = Database()
    # Create a HelpDesk object
    help_desk = HelpDesk(db)
    # Create a Microservices object
    microservices = Microservices()
    while True:
        print("1. Insert ticket")
        print("2. Get tickets")
        print("3. Change ticket status")
        print("4. Get tickets by period")
        print("5. Average ticket resolution time")
        print("6. Cluster tickets by category")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            # Insert a new ticket
            description = input("Enter ticket description: ")
            status = input("Enter ticket status: ")
            opening_date = input("Enter ticket opening date: ")
            last_modification_date = input("Enter ticket last modification date: ")
            closing_date = input("Enter ticket closing date: ")
            category = input("Enter ticket category: ")
            help_desk.insert_ticket(description, status, opening_date, last_modification_date, closing_date, category)
        elif choice == "2":
            # Get all tickets
            tickets = db.get_tickets()
            for ticket in tickets:
                print(ticket)
        elif choice == "3":
            # Change the status of a ticket
            ticket_id = input("Enter ticket ID: ")
            new_status = input("Enter new status: ")
            help_desk.change_ticket_status(ticket_id, new_status)
        elif choice == "4":
            # Get tickets by period
            microservices.get_tickets_by_period()
        elif choice == "5":
            # Calculate the average ticket resolution time
            microservices.average_ticket_resolution_time()
        elif choice == "6":
            # Cluster tickets by category
            microservices.cluster_tickets_by_category()
        elif choice == "7":
            break
if __name__ == "__main__":
    main()