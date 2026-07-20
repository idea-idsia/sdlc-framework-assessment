import tkinter as tk
from tkinter import messagebox


def login():
    username = entry_username.get()
    password = entry_password.get()

    # Simple validation, ideally use a database to check credentials
    if username == "user" and password == "pass":
        root.withdraw()
        open_main_window("user")  # Open main window as user
    elif username == "helpdesk" and password == "pass":
        root.withdraw()
        open_main_window("helpdesk")  # Open main window as helpdesk
    else:
        messagebox.showerror("Login Error", "Invalid credentials")


def open_main_window(role):
    main_window = tk.Toplevel(root)
    if role == 'user':
        # Add user-specific GUI elements
        pass
    elif role == 'helpdesk':
        # Add helpdesk-specific GUI elements
        pass


root = tk.Tk()
label_username = tk.Label(root, text="Username")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()
label_password = tk.Label(root, text="Password")
label_password.pack()
entry_password = tk.Entry(root, show='*')
entry_password.pack()
button_login = tk.Button(root, text="Login", command=login)
button_login.pack()
root.mainloop()