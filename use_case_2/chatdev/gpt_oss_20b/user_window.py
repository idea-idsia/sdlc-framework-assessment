'''
Main window for ticket creation and management.
'''
import tkinter as tk
from tkinter import messagebox
import uuid
from ticket import Ticket
from detail_window import DetailWindow
class UserWindow:
    """
    Main window for ticket creation and management.
    """
    def __init__(self, master):
        self.master = master
        self.master.title("Ticket Manager")
        self.master.geometry("500x400")
        self.tickets = self._load_tickets()
        self._create_widgets()
    # --------------------------------------------------------------
    def _load_tickets(self):
        """Load tickets from the database handler."""
        from database import DatabaseHandler
        db = DatabaseHandler()
        return db.get_all_tickets()
    # --------------------------------------------------------------
    def _create_widgets(self):
        """Create UI elements."""
        self.ticket_listbox = tk.Listbox(self.master)
        self.ticket_listbox.pack(fill="both", expand=True)
        for ticket in self.tickets:
            self.ticket_listbox.insert(tk.END, f"#{ticket.id}: {ticket.description}")
        tk.Button(self.master, text="Create Ticket", command=self._create_ticket).pack(pady=5)
    # --------------------------------------------------------------
    def _create_ticket(self):
        """Handle ticket creation from user input."""
        # No requirement to select a ticket type; create a simple placeholder ticket.
        ticket_id = uuid.uuid4().int >> 64
        ticket = Ticket(
            id=ticket_id,
            description="Example ticket",
            category="facility",
            status="open",
        )
        db = DatabaseHandler()
        db.tickets.append(
            {
                "ticket_id": ticket.id,
                "description": ticket.description,
                "category": ticket.category,
                "status": ticket.status,
                "opened": ticket.open_date,
                "closed": ticket.close_date,
            }
        )
        db._save()
        messagebox.showinfo("Success", f"Ticket #{ticket_id} created.")
        DetailWindow(self.master, ticket_id)  # Open detail window without nested mainloop