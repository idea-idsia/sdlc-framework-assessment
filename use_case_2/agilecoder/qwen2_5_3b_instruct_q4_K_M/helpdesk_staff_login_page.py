# helpdesk_staff_login_page.py
'''
Tkinter-based login page for Helpdesk Staff.
'''
import tkinter as tk
from tkinter import ttk
class HelpdeskStaffLoginPage:
    def __init__(self, root):
        self.root = root
        self.username_entry = tk.Entry(root)
        self.password_entry = tk.Entry(root, show="*")
        # Layout design (grid system) for the login page
        username_label = tk.Label(root, text="Username:")
        password_label = tk.Label(root, text="Password:")
        username_label.grid(row=0, column=0, sticky=tk.W, pady=(15, 0))
        password_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 15))
        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)
        # Radio buttons for user type selection: Simple User or Helpdesk Staff
        simple_user_radio = tk.Radiobutton(root, text="Simple User", variable=tk.IntVar(), value=0)
        helpdesk_staff_radio = tk.Radiobutton(root, text="Helpdesk Staff", variable=tk.IntVar(), value=1)
        simple_user_radio.grid(row=2, column=0, sticky=tk.W, pady=(5, 0))
        helpdesk_staff_radio.grid(row=2, column=1, sticky=tk.W, pady=(5, 0))
        login_button = tk.Button(root, text="Login", command=self.login)
        login_button.grid(row=3, column=1, padx=10, pady=10)
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "helpdesk_staff" and password == "password":
            print("Helpdesk Staff Logged In")