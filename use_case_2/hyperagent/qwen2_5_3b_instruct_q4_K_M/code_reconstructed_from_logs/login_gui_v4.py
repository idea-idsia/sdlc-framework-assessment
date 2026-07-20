import tkinter as tk

def on_login():
    username = entry_username.get()
    password = entry_password.get()

    if radio_var_helpdesk.get() == 1: # Check helpdesk staff role
        if username == "helpdesk" and password == "password123":
            label_status.config(text="Login successful for helpdesk staff")
        else:
            label_status.config(text="Invalid credentials - Helpdesk Staff")
    elif radio_var_simple_user.get() == 2: # Check simple user role
        if username == "user" and password == "password456":
            label_status.config(text="Login successful for user")
        else:
            label_status.config(text="Invalid credentials - Simple User")

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

# Login Button
login_button = tk.Button(root, text="Login", command=lambda: on_login())
login_button.grid(row=4, columnspan=2)

root.mainloop()