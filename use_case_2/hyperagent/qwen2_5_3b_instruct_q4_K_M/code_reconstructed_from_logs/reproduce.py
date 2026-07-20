import tkinter as tk;
from tkinter import messagebox, ttk; class App(tk.Tk):


def __init__(self):
    super().__init__()
    self.title('Login Page')

    # Username Label and Entry
    self.label_username = tk.Label(self, text='Username:')
    self.label_username.grid(row=0, column=0)
    self.entry_username = tk.Entry(self)
    self.entry_username.grid(row=0, column=1)

    # Password Label and Entry
    self.label_password = tk.Label(self, text='Password:')
    self.label_password.grid(row=1, column=0)
    self.entry_password = tk.Entry(self, show="*")
    self.entry_password.grid(row=1, column=1)

    # User Type Radio Buttons
    self.helpdesk_radio_label = tk.Label(self, text='User Type:')
    self.helpdesk_radio_label.grid(row=2, column=0)
    self.radio_var_helpdesk = tk.IntVar()
    self.helpdesk_radio_button = tk.Radiobutton(self, text='Helpdesk Staff', variable=self.radio_var_helpdesk, value=1)
    self.helpdesk_radio_button.grid(row=3, column=0)

    simple_user_radio_label = tk.Label(self, text='')
    simple_user_radio_label.grid(row=2, column=1)
    self.radio_var_simple_user = tk.IntVar()
    self.simple_user_radio_button = tk.Radiobutton(self, text='Simple User', variable=self.radio_var_simple_user,
                                                   value=2)
    self.simple_user_radio_button.grid(row=3, column=1)

    # Login Button
    self.login_button = tk.Button(self, text='Login', command=lambda: on_login())
    self.login_button.grid(row=4, columnspan=2)

    def on_login():
        username = self.entry_username.get()
        password = self.entry_password.get()

        if self.radio_var_helpdesk.get() == 1:
            if username == "helpdesk" and password == "password123":
                label_status.config(text='Login successful for helpdesk staff')
            else:
                label_status.config(text='Invalid credentials - Helpdesk Staff')
        elif self.radio_var_simple_user.get() == 2:
            if username == "user" and password == "password456":
                label_status.config(text='Login successful for user')
            else:
                label_status.config(text='Invalid credentials - Simple User')


root = App()
root.mainloop()