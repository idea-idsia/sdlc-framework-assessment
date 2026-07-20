import tkinter as tk
from tkinter import messagebox


def handle_login():
    selected_user_type = user_type_var.get()

    if not selected_user_type:
        messagebox.showerror("Error", "Please select a user type.")
        return

    if selected_user_type == "Helpdesk Staff":
        # Handle helpdesk staff login logic here
        print("Helpdesk Staff logged in")
    elif selected_user_type == "Simple User":
        # Handle simple user login logic here
        print("Simple User logged in")


# Create the main window
root = tk.Tk()
root.title("Login Application")

# Create a label for user type selection
user_type_label = tk.Label(root, text="User Type:")
user_type_label.pack()

# Define variable to hold selected user type
user_type_var = tk.StringVar(value="Simple User")

# Create radio buttons for user type selection
helpdesk_radio = tk.Radiobutton(root, text="Helpdesk Staff", variable=user_type_var, value="Helpdesk Staff")
simple_user_radio = tk.Radiobutton(root, text="Simple User", variable=user_type_var, value="Simple User")

helpdesk_radio.pack()
simple_user_radio.pack()

# Create a login button
login_button = tk.Button(root, text="Login", command=handle_login)
login_button.pack()

# Start the main event loop
root.mainloop()