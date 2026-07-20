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
        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.user_label.grid(row=0, column=0)
        self.user_entry.grid(row=0, column=1)
        self.password_label.grid(row=1, column=0)
        self.password_entry.grid(row=1, column=1)
        self.register_button.grid(row=2, column=0)
        self.login_button.grid(row=2, column=1)
    def register(self):
        # Register a new user and display the ticket page
        username = self.user_entry.get()
        password = self.password_entry.get()
        if not database.is_username_taken(username):
            database.add_new_user(username, password)
            self.parent.show_ticket_page()
        else:
            print("Username already taken")
    def login(self):
        # Log in an existing user and display the ticket page
        username = self.user_entry.get()
        password = self.password_entry.get()
        if database.is_username_taken(username) and database.check_password(username, password):
            self.parent.show_ticket_page()
        else:
            print("Invalid username or password")