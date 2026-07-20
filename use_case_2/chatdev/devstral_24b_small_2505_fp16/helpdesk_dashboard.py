'''
Helpdesk Dashboard for handling helpdesk interactions.
'''
from tkinter import Tk, Label, Entry, Button, Text, END
class HelpdeskDashboard:
    def __init__(self, root, db_manager):
        self.root = root
        self.db_manager = db_manager
        self.setup_ui()
    def setup_ui(self):
        label = Label(self.root, text="Helpdesk Dashboard")
        label.pack()
        # Update Ticket Section
        update_label = Label(self.root, text="Update a Ticket")
        update_label.pack()
        ticket_id_entry = Entry(self.root)
        ticket_id_entry.pack()
        description_entry = Entry(self.root)
        description_entry.pack()
        category_entry = Entry(self.root)
        category_entry.pack()
        status_entry = Entry(self.root)
        status_entry.pack()
        update_button = Button(self.root, text="Update Ticket", command=lambda: self.update_ticket(ticket_id_entry.get(), description_entry.get(), category_entry.get(), status_entry.get()))
        update_button.pack()
        # View All Tickets Section
        view_label = Label(self.root, text="View All Tickets")
        view_label.pack()
        view_button = Button(self.root, text="View All Tickets", command=self.view_all_tickets)
        view_button.pack()
    def update_ticket(self, ticket_id, description=None, category=None, status=None):
        success = self.db_manager.update_ticket(int(ticket_id), description, category, status)
        print(f"Ticket Updated: {success}")
    def view_all_tickets(self):
        open_tickets = self.db_manager.get_tickets(status='open')
        active_tickets = self.db_manager.get_tickets(status='active')
        closed_tickets = self.db_manager.get_tickets(status='closed')
        text_box = Text(self.root)
        text_box.pack()
        for ticket in open_tickets:
            text_box.insert(END, f"Open Ticket ID: {ticket[0]}, Description: {ticket[1]}\n")
        for ticket in active_tickets:
            text_box.insert(END, f"Active Ticket ID: {ticket[0]}, Description: {ticket[1]}\n")
        for ticket in closed_tickets:
            text_box.insert(END, f"Closed Ticket ID: {ticket[0]}, Description: {ticket[1]}\n")
    def update_ticket_status(self, ticket_id, status):
        success = self.db_manager.update_ticket(int(ticket_id), status=status)
        print(f"Ticket Status Updated: {success}")