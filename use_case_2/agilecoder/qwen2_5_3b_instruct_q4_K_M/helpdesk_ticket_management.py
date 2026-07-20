import tkinter as tk
from tkinter import ttk, messagebox
class TicketManager:
    def __init__(self, root, ticket_data):
        self.root = root
        self.data = ticket_data
        self.selected_ticket_id = None
        # Initialize UI components
        label_title = tk.Label(root, text="Ticket Management")
        label_title.pack()
        tree = ttk.Treeview(root)
        columns = ("Status", "Category", "Description", "Opened Date", "Last Modified Date", "Closed Date")
        headers = {"Status": 0, "Category": 1, "Description": 2, "Opened Date": 3, "Last Modified Date": 4, "Closed Date": 5}
        tree["columns"] = columns
        for col in columns:
            tree.heading(col, text=col.title(), anchor='w')
            tree.column(col, width=100)
        self.data_added(tree)
    def data_added(self, tree):
        # Add sample ticket to show functionality
        tree.insert("", tk.END, values=("Active", "Facility Management", "", "N/A", "2023-04-05", ""))
    def show_tickets(self):
        if not self.selected_ticket_id:
            self.clear_display()
            for ticket in self.data:
                self.add_ticket_to_tree(ticket)
        else:
            ticket = next((t for t in self.data if str(t["id"]) == str(self.selected_ticket_id)), None)
            self.display_ticket(ticket)
    def add_ticket_to_tree(self, ticket):
        tree.insert("", tk.END, values=tuple(ticket.values()))
    def display_ticket(self, ticket):
        # Create labels and grid them to the frame
        for col in ("Status", "Category", "Description", "Opened Date", "Last Modified Date", "Closed Date"):
            label = ttk.Label(self.root, text=f"{col}: {ticket[col]}")
            label.grid(row=2 if col == "Status" else 3)
    def update_ticket_status(self):
        pass
    def change_status(self):
        pass
root = tk.Tk()
helpdesk_manager = TicketManager(root, tickets_data)
helpdesk_manager.show_tickets()
tk.mainloop()