# Main application
'''
This module represents the main application.
'''
import tkinter as tk
from database import Database
from ticket import Ticket
from helpdesk_user import HelpdeskUser
from simple_user import SimpleUser
from auth import Authenticator
class TicketManagementSystem:
    def __init__(self, root):
        self.root = root
        self.db = Database('tickets.db')
        self.authenticator = Authenticator()
        self.logged_in_user = None
        # Create login form
        self.login_form = tk.Frame(self.root)
        self.login_form.pack()
        self.username_label = tk.Label(self.login_form, text='Username:')
        self.username_label.pack()
        self.username_entry = tk.Entry(self.login_form)
        self.username_entry.pack()
        self.password_label = tk.Label(self.login_form, text='Password:')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.login_form, show='*')
        self.password_entry.pack()
        self.login_button = tk.Button(self.login_form, text='Login', command=self.login)
        self.login_button.pack()
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.authenticator.login(username, password)
        if role:
            self.logged_in_user = role
            self.login_form.destroy()
            if role == 'helpdesk':
                # Create helpdesk interface
                self.helpdesk_interface = tk.Frame(self.root)
                self.helpdesk_interface.pack()
                self.ticket_id_label = tk.Label(self.helpdesk_interface, text='Ticket ID:')
                self.ticket_id_label.pack()
                self.ticket_id_entry = tk.Entry(self.helpdesk_interface)
                self.ticket_id_entry.pack()
                self.new_status_label = tk.Label(self.helpdesk_interface, text='New Status:')
                self.new_status_label.pack()
                self.new_status_entry = tk.Entry(self.helpdesk_interface)
                self.new_status_entry.pack()
                self.update_button = tk.Button(self.helpdesk_interface, text='Update', command=self.update_ticket)
                self.update_button.pack()
            elif role == 'simple_user':
                # Create simple user interface
                self.simple_user_interface = tk.Frame(self.root)
                self.simple_user_interface.pack()
                self.description_label = tk.Label(self.simple_user_interface, text='Description:')
                self.description_label.pack()
                self.description_entry = tk.Entry(self.simple_user_interface)
                self.description_entry.pack()
                self.category_label = tk.Label(self.simple_user_interface, text='Category:')
                self.category_label.pack()
                self.category_entry = tk.Entry(self.simple_user_interface)
                self.category_entry.pack()
                self.create_button = tk.Button(self.simple_user_interface, text='Create', command=self.create_ticket)
                self.create_button.pack()
        else:
            print("Invalid credentials")
    def update_ticket(self):
        ticket_id = int(self.ticket_id_entry.get())
        new_status = self.new_status_entry.get()
        helpdesk_user = HelpdeskUser('Helpdesk User')
        helpdesk_user.update_ticket(self.db, ticket_id, new_status)
    def create_ticket(self):
        description = self.description_entry.get()
        category = self.category_entry.get()
        simple_user = SimpleUser('Simple User')
        simple_user.create_ticket(self.db, description, category)
if __name__ == '__main__':
    root = tk.Tk()
    app = TicketManagementSystem(root)
    root.mainloop()