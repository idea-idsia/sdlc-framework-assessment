import tkinter as tk

def on_login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "helpdesk" and password == "password123":
        label_status.config(text="Login successful for helpdesk staff")
    elif username == "user" and password == "password456":
        label_status.config(text="Login successful for user")
    else:
        label_status.config(text="Invalid credentials")

# Create the main window
root = tk.Tk()
root.title("Login Page")

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

# Login Button
button_login = tk.Button(root, text="Login", command=on_login)
button_login.grid(row=2, columnspan=2)

# Status Label
label_status = tk.Label(root, text="")
label_status.grid(row=3, columnspan=2)

root.mainloop()