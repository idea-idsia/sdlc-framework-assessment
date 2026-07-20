'''
GUI modules – role selection, dashboards, and ticket interactions.
'''
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from models import Ticket
class RoleSelectionWindow(tk.Tk):
    """A small window that lets the user pick a role and opens the corresponding dashboard."""
    def __init__(self):
        super().__init__()
        self.title("Select Role")
        self.geometry("300x150")
        ttk.Label(self, text="Choose your role:").pack(pady=10)
        ttk.Button(self, text="Helpdesk Staff",
                   command=lambda: self._open_dashboard("helpdesk")).pack(fill=tk.X, padx=20, pady=5)
        ttk.Button(self, text="Simple User",
                   command=lambda: self._open_dashboard("user")).pack(fill=tk.X, padx=20, pady=5)
    def _open_dashboard(self, role: str):
        self.destroy()
        if role == "helpdesk":
            HelpdeskDashboard(role).mainloop()
        else:
            UserDashboard(role).mainloop()
class BaseDashboard(tk.Tk):
    def __init__(self, role: str):
        super().__init__()
        self.role = role
        self.title(f"Ticket System – {role.title()}")
        self.geometry("700x500")
class UserDashboard(BaseDashboard):
    """Dashboard for simple users – create and view tickets."""
    def __init__(self, role: str):
        super().__init__(role)
        ttk.Button(self, text="Create Ticket", command=self.create_ticket).pack(pady=5)
        self.create_tree()
    def create_tree(self):
        self.tree = ttk.Treeview(self, columns=('id', 'description', 'status'), show='headings')
        for col in ('id', 'description', 'status'):
            self.tree.heading(col, text=col.title())
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.refresh_tickets()
    def refresh_tickets(self):
        tickets = Ticket.fetch_by_role_and_status(self.role, [Ticket.STATUS_OPEN, Ticket.STATUS_ACTIVE, Ticket.STATUS_CLOSED])
        self.tree.delete(*self.tree.get_children())
        for t in tickets:
            self.tree.insert('', tk.END, values=(t.id, t.description, t.status))
    def create_ticket(self):
        description = simpledialog.askstring("Ticket Description", "Enter ticket description:")
        if not description:
            return
        category = simpledialog.askstring("Ticket Category",
                                          f"Enter category ({', '.join(Ticket.CATEGORIES)}):")
        if category not in Ticket.CATEGORIES:
            messagebox.showerror("Invalid Category", "Please enter a valid category.")
            return
        Ticket.create(description=description, category=category, created_by_role=self.role)
        self.refresh_tickets()
class HelpdeskDashboard(BaseDashboard):
    """Dashboard for helpdesk staff – activate, close, and view tickets."""
    def __init__(self, role: str):
        super().__init__(role)
        self.create_widgets()
        self.refresh_tickets()
    def create_widgets(self):
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)
        self.activate_btn = ttk.Button(btn_frame, text='Activate', command=self.activate_ticket)
        self.activate_btn.pack(side=tk.LEFT, padx=5)
        self.close_btn = ttk.Button(btn_frame, text='Close', command=self.close_ticket)
        self.close_btn.pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text='Refresh', command=self.refresh_tickets).pack(side=tk.RIGHT, padx=5)
        self.tree = ttk.Treeview(self, columns=('id', 'description', 'status'), show='headings')
        for col in ('id', 'description', 'status'):
            self.tree.heading(col, text=col.title())
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    def refresh_tickets(self):
        tickets = Ticket.fetch_by_status(Ticket.STATUS_OPEN) + Ticket.fetch_by_status(Ticket.STATUS_ACTIVE) + Ticket.fetch_by_status(Ticket.STATUS_CLOSED)
        self.tree.delete(*self.tree.get_children())
        for t in tickets:
            self.tree.insert('', tk.END, values=(t.id, t.description, t.status))
    def activate_ticket(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning('Select Ticket', 'Please select a ticket')
            return
        ticket_id = int(self.tree.item(selected[0])['values'][0])
        ticket = Ticket.fetch_by_id(ticket_id)
        if ticket and ticket.status == Ticket.STATUS_OPEN:
            ticket.change_status(Ticket.STATUS_ACTIVE, self.role)
            self.refresh_tickets()
        else:
            messagebox.showinfo('Info', 'Only open tickets can be activated.')
    def close_ticket(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning('Select Ticket', 'Please select a ticket')
            return
        ticket_id = int(self.tree.item(selected[0])['values'][0])
        ticket = Ticket.fetch_by_id(ticket_id)
        if ticket and ticket.status == Ticket.STATUS_ACTIVE:
            ticket.change_status(Ticket.STATUS_CLOSED, self.role)
            self.refresh_tickets()
        else:
            messagebox.showinfo('Info', 'Only active tickets can be closed.')