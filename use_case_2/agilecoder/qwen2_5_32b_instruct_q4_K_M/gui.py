'''
Implements the GUI for creating and viewing tickets.
Differentiates between helpdesk staff and simple user roles.
'''
import tkinter as tk
from tkinter import messagebox, simpledialog
import ticket_manager
def login_screen(root, db):
    def on_login():
        role = "user" if role_var.get() == 1 else "helpdesk"
        view_tickets(role)
    role_var = tk.IntVar()
    user_radio = tk.Radiobutton(root, text="User", variable=role_var, value=1)
    helpdesk_radio = tk.Radiobutton(root, text="Helpdesk", variable=role_var, value=2)
    login_button = tk.Button(root, text="Login", command=on_login)
    user_radio.pack()
    helpdesk_radio.pack()
    login_button.pack()
def view_tickets(role):
    ticket_manager_obj = TicketManager(db)
    if role == "user":
        # Logic to display tickets for users
        pass
    elif role == "helpdesk":
        # Logic to display tickets for helpdesk staff
        pass
root = tk.Tk()
db = DatabaseHandler()
login_screen(root, db)
root.mainloop()