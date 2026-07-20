# user_management.py
import tkinter as tk
import database
class UserManagement(tk.Frame):
    def __init__(self, parent):
        # Set up the GUI layout
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        # Add widgets to the GUI
        self.user_label = ttk.Label(self, text="User:")
        self.user_entry = ttk.Entry(self)
        self.password_label = ttk.Label(self, text="Password:")
        self.password_entry = ttk.Entry(self)
        self.register_button = ttk.Button(self, text="Register", command=self.register)
        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.user_label.grid(column=0, row=0)
        self.user_entry.grid(column=1, row=0)
        self.password_label.grid(column=0, row=1)
        self.password_entry.grid(column=1, row=1)
        self.register_button.grid(column=2, row=2)
        self.login_button.grid(column=3, row=2)
    def register(self):
        # Register a new user and display the ticket page
        username = self.user_entry.get()
        password = self.password_entry.get()
        if not database.authenticate_user(username, password):
            tk.Tk().withdraw()  # To avoid error message pop-up
            self.parent.show_ticket_page()
        else:
            print("User already exists")
    def login(self):
        # Log in the user and display the ticket page
        username = self.user_entry.get()
        password = self.password_entry.get()
        if database.authenticate_user(username, password):
            tk.Tk().withdraw()  # To avoid error message pop-up
            self.parent.show_ticket_page()
        else:
            print("Invalid username or password")