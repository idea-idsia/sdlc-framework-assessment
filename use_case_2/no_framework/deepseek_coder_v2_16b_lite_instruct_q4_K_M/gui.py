import tkinter as tk
from tkinter import messagebox, scrolledtext


class App(tk.Tk):
    def __init__(self, user=None):
        super().__init__()
        self.user = user
        self.title("Ticket Management System")
        # Create login or main window based on the user type
        if not user:
            self.create_login_window()
        else:
            self.main_window(self.user)

    def create_login_window(self):
        tk.Label(self, text="Username:").pack()
        self.username = tk.Entry(self)
        self.username.pack()
        tk.Button(self, text="Login", command=self.validate_user).pack()

    def validate_user(self):
        username = self.username.get()
        # Simple validation; in a real application, use database checks
        if username:
            user = User.query.filter_by(username=username).first()
            if not user:
                user = User(username=username)
                db.session.add(user)
                db.session.commit()
            self.main_window(user)

    def main_window(self, user):
        self.title("Welcome " + user.username)
        tk.Button(self, text="Create Ticket", command=self.create_ticket).pack()
        tk.Button(self, text="View Tickets", command=self.view_tickets).pack()
        if user.is_helpdesk:
            self.add_helpdesk_buttons()

    def create_ticket(self):
        # Popup for creating a ticket
        pass

    def view_tickets(self):
        # Display tickets in a listbox or similar widget
        pass

    def add_helpdesk_buttons(self):
        tk.Button(self, text="View All Tickets", command=self.view_all_tickets).pack()

    def view_all_tickets(self):
        # Fetch and display all tickets for helpdesk users
        pass