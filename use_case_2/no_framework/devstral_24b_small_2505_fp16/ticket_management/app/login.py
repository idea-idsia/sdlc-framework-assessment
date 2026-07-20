# app/login.py

import tkinter as tk
from tkinter import messagebox
from ticket_management import UserApp, HelpdeskApp

def open_user_app():
    root.destroy()
    UserApp().run()

def open_helpdesk_app():
    root.destroy()
    HelpdeskApp().run()

root = tk.Tk()
root.title("Login")

tk.Label(root, text="Choose your role:").pack(pady=20)

user_button = tk.Button(root, text="User", command=open_user_app)
user_button.pack(side=tk.LEFT, padx=10)

helpdesk_button = tk.Button(root, text="Helpdesk", command=open_helpdesk_app)
helpdesk_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()