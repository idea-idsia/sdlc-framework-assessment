import tkinter as tk
from tkinter import messagebox

def login_as_user():
    # Simple callback, in a real app, this would trigger the user dashboard
    messagebox.showinfo("Login", "Logged in as User")

def login_as_helpdesk():
    # Callback for helpdesk login, similarly, this would open the helpdesk dashboard
    messagebox.showinfo("Login", "Logged in as Helpdesk")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Login as User", command=login_as_user).pack(side=tk.LEFT)
tk.Button(frame, text="Login as Helpdesk", command=login_as_helpdesk).pack(side=tk.RIGHT)

root.mainloop()