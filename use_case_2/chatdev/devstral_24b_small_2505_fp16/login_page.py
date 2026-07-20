'''
Login Page for user type selection.
'''
from tkinter import Tk, Label, Button
class LoginPage:
    def __init__(self, root, open_dashboard_callback):
        self.root = root
        self.open_dashboard_callback = open_dashboard_callback
        self.setup_ui()
    def setup_ui(self):
        label = Label(self.root, text="Select User Type")
        label.pack()
        user_button = Button(self.root, text="User", command=lambda: self.open_user_dashboard())
        user_button.pack()
        helpdesk_button = Button(self.root, text="Helpdesk", command=lambda: self.open_helpdesk_dashboard())
        helpdesk_button.pack()
    def open_user_dashboard(self):
        self.root.destroy()  # Close login window
        self.open_dashboard_callback("simple_user")
    def open_helpdesk_dashboard(self):
        self.root.destroy()  # Close login window
        self.open_dashboard_callback("helpdesk")