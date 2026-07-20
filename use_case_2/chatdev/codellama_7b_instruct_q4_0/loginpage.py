import tkinter as tk
from tkinter import ttk
import user_management
class LoginPage(tk.Frame):
    def __init__(self, parent):
        # Set up the GUI layout
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        # Add widgets to the GUI
        self.username_label = ttk.Label(self, text="Username:")
        self.username_entry = ttk.Entry(self)
        self.password_label = ttk.Label(self, text="Password:")
        self.password_entry = ttk.Entry(self)
        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.username_label.grid(column=0, row=0)
        self.username_entry.grid(column=1, row=0)
        self.password_label.grid(column=0, row=1)
        self.password_entry.grid(column=1, row=1)
        self.login_button.grid(column=1, row=2)
    def login(self):
        # Log in the user and display the ticket page
        username = self.username_entry.get()
        password = self.password_entry.get()
        if user_management.authenticate_user(username, password):
            tk.Tk().withdraw()  # To avoid error message pop-up
            self.parent.show_ticket_page()
        else:
            print("Invalid username or password")