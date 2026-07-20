'''
Module for graphical user interface components.
Contains classes to manage the display of tickets and provide a login functionality.
'''
import tkinter as tk
from database import DatabaseManager
class LoginGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.login_button = tk.Button(self)
        self.login_button["text"] = "Login as User"
        self.login_button["command"] = self.user_login
        self.login_button.pack(side="top")
        self.admin_button = tk.Button(self)
        self.admin_button["text"] = "Login as Admin"
        self.admin_button["command"] = self.admin_login
        self.admin_button.pack(side="top")
    def user_login(self):
        print("User Login")
        # Placeholder for actual user login logic
        root = tk.Toplevel(self.master)
        TicketGUI(root, 'user')
    def admin_login(self):
        print("Admin Login")
        # Placeholder for actual admin login logic
        root = tk.Toplevel(self.master)
        TicketGUI(root, 'admin')
class TicketGUI(tk.Frame):
    def __init__(self, master=None, user_type='user'):
        super().__init__(master)
        self.master = master
        self.user_type = user_type
        self.database_manager = DatabaseManager()
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        """Creates widgets for ticket management."""
        tk.Label(self, text="User Interface" if self.user_type == 'user' else "Admin Interface").pack(side='top')
        # Ticket listbox
        self.ticket_listbox = tk.Listbox(self)
        self.load_tickets()
        self.ticket_listbox.pack()
        if self.user_type == 'user':
            add_button = tk.Button(self, text="Add Ticket", command=self.add_ticket_form)
            add_button.pack(side='bottom')
        # Admin specific buttons here
        elif self.user_type == 'admin':
            update_status_button = tk.Button(self, text="Update Status", command=self.update_ticket_status)
            update_status_button.pack(side='bottom')
    def load_tickets(self):
        """Loads tickets from the database and updates UI."""
        tickets = self.database_manager.query_all()
        for ticket in tickets:
            status_filter = 'open' if self.user_type == 'user' else None
            if not status_filter or ticket['status'] in status_filter:
                self.ticket_listbox.insert(tk.END, f"ID: {ticket['id']}, Status: {ticket['status']}")
    def add_ticket_form(self):
        """Displays a form to create a new ticket."""
        top = tk.Toplevel()
        top.title("Add Ticket")
        description_label = tk.Label(top, text="Description:")
        description_entry = tk.Entry(top)
        category_label = tk.Label(top, text="Category (facility, it, services):")
        category_entry = tk.Entry(top)
        def submit_form():
            ticket_details = {
                'status': 'open',
                'description': description_entry.get(),
                'category': category_entry.get()
            }
            self.database_manager.add_ticket(ticket_details)
            top.destroy()  # Close the form
            self.load_tickets()
        submit_button = tk.Button(top, text="Submit", command=submit_form)
        description_label.pack(side='top')
        description_entry.pack(side='top')
        category_label.pack(side='top')
        category_entry.pack(side='top')
        submit_button.pack(side='bottom')
    def update_ticket_status(self):
        """Updates the status of a selected ticket."""
        # Placeholder for actual logic to select and change ticket status
        pass
# Note: This is a simplified example. Actual implementation will require more detailed UI design and error handling.