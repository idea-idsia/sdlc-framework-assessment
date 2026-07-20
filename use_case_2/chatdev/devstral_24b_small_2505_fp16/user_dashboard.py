'''
User Dashboard for handling user interactions.
'''
from tkinter import Tk, Label, Entry, Button, Text, END
class UserDashboard:
    def __init__(self, root, db_manager):
        self.root = root
        self.db_manager = db_manager
        self.setup_ui()
    def setup_ui(self):
        label = Label(self.root, text="User Dashboard")
        label.pack()
        # Create Ticket Section
        create_label = Label(self.root, text="Create a New Ticket")
        create_label.pack()
        description_entry = Entry(self.root)
        description_entry.pack()
        category_entry = Entry(self.root)
        category_entry.pack()
        create_button = Button(self.root, text="Create Ticket", command=lambda: self.create_ticket(description_entry.get(), category_entry.get()))
        create_button.pack()
        # View Tickets Section
        view_label = Label(self.root, text="View Your Tickets")
        view_label.pack()
        view_button = Button(self.root, text="View Tickets", command=self.view_tickets)
        view_button.pack()
    def create_ticket(self, description, category):
        ticket_id = self.db_manager.add_ticket(description, category, 'open')
        print(f"Ticket Created with ID: {ticket_id}")
    def view_tickets(self):
        open_tickets = self.db_manager.get_tickets(status='open')
        active_tickets = self.db_manager.get_tickets(status='active')
        text_box = Text(self.root)
        text_box.pack()
        for ticket in open_tickets:
            text_box.insert(END, f"Open Ticket ID: {ticket[0]}, Description: {ticket[1]}\n")
        for ticket in active_tickets:
            text_box.insert(END, f"Active Ticket ID: {ticket[0]}, Description: {ticket[1]}\n")
    def update_ticket(self, ticket_id, description=None):
        success = self.db_manager.update_ticket(int(ticket_id), description=description)
        print(f"Ticket Updated: {success}")