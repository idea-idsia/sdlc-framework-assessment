import tkinter as tk
from tkinter import messagebox, ttk


def add_ticket():
    ticket_entry = entry_ticket.get()
    category = radio_var_category.get()

    # Placeholder for database operations
    print(f"Adding Ticket: {ticket_entry} - Category: {category}")

    if not ticket_entry:
        messagebox.showerror("Invalid Input", "Please enter a ticket.")
        return


def update_ticket():
    old_ticket = entry_old_ticket.get().strip()  # Remove leading/trailing spaces
    new_category = radio_var_new_category.get()

    # Placeholder for database operations
    print(f"Updating Ticket: {old_ticket} - New Category: {new_category}")

    if not old_ticket:
        messagebox.showerror("Invalid Input", "Please enter an existing ticket.")
        return


def delete_ticket():
    old_ticket = entry_old_ticket.get().strip()  # Remove leading/trailing spaces

    # Placeholder for database operations
    print(f"Deleting Ticket: {old_ticket}")

    if not old_ticket:
        messagebox.showerror("Invalid Input", "Please enter an existing ticket.")
        return


def on_login():
    username = entry_username.get()
    password = entry_password.get()

    if radio_var_helpdesk.get() == 1:  # Check helpdesk staff role
        if username == "helpdesk" and password == "password123":
            label_status.config(text="Login successful for helpdesk staff")
        else:
            label_status.config(text="Invalid credentials - Helpdesk Staff")
    elif radio_var_simple_user.get() == 2:  # Check simple user role
        if username == "user" and password == "password456":
            label_status.config(text="Login successful for user")
        else:
            label_status.config(text="Invalid credentials - Simple User")


root = tk.Tk()
root.title("Ticket Management System")

# Username Label and Entry
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

# Password Label and Entry
label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

# User Type Radio Buttons
helpdesk_radio_label = tk.Label(root, text="User Type:")
helpdesk_radio_label.grid(row=2, column=0)
radio_var_helpdesk = tk.IntVar()
helpdesk_radio_button = tk.Radiobutton(root, text="Helpdesk Staff", variable=radio_var_helpdesk, value=1)
helpdesk_radio_button.grid(row=3, column=0)

simple_user_radio_label = tk.Label(root, text="")
simple_user_radio_label.grid(row=2, column=1)
radio_var_simple_user = tk.IntVar()
simple_user_radio_button = tk.Radiobutton(root, text="Simple User", variable=radio_var_simple_user, value=2)
simple_user_radio_button.grid(row=3, column=1)

# Ticket Entry and Category Radio Buttons
ticket_label = tk.Label(root, text="Enter Ticket:")
ticket_label.grid(row=4, column=0)
entry_ticket = tk.Entry(root)
entry_ticket.grid(row=4, column=1)

category_label = tk.Label(root, text="Category:")
category_label.grid(row=5, column=0)
radio_var_category = tk.IntVar()
radio_var_category.set(1)  # Set default category
radio_helpdesk = tk.Radiobutton(root, text="Helpdesk", variable=radio_var_category, value=1)
radio_helpdesk.grid(row=6, column=0)
radio_simple_user = tk.Radiobutton(root, text="Simple User", variable=radio_var_category, value=2)
radio_simple_user.grid(row=7, column=0)

# Actions Buttons
add_button = tk.Button(root, text="Add Ticket", command=add_ticket)
add_button.grid(row=8, columnspan=2)

update_button = tk.Button(root, text="Update Ticket", command=update_ticket)
update_button.grid(row=9, columnspan=2)

delete_button = tk.Button(root, text="Delete Ticket", command=delete_ticket)
delete_button.grid(row=10, columnspan=2)

login_button = tk.Button(root, text="Login", command=lambda: on_login())
login_button.grid(row=11, columnspan=2)

# Status Label
label_status = tk.Label(root, text="")
label_status.grid(row=12, columnspan=2)

root.mainloop()