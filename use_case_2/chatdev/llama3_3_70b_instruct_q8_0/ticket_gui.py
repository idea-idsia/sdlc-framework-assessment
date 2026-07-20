# Import necessary libraries
import tkinter as tk
from main import MainApp
'''
Ticket GUI class.
It creates a ticket form and handles the ticket creation process.
'''
class TicketGUI:
    def __init__(self, root, main_app):
        self.root = root
        self.main_app = main_app
        # Create ticket form
        self.ticket_form = tk.Frame(self.root)
        self.ticket_form.pack()
        self.description_label = tk.Label(self.ticket_form, text="Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(self.ticket_form)
        self.description_entry.pack()
        self.category_label = tk.Label(self.ticket_form, text="Category:")
        self.category_label.pack()
        self.category_var = tk.StringVar()
        self.category_var.set("facility")
        self.category_option = tk.OptionMenu(self.ticket_form, self.category_var, "facility", "technical", "services")
        self.category_option.pack()
        self.create_button = tk.Button(self.ticket_form, text="Create Ticket", command=self.create_ticket)
        self.create_button.pack()
        # Create ticket list
        self.ticket_list = tk.Listbox(self.root)
        self.ticket_list.pack()
    def create_ticket(self):
        description = self.description_entry.get()
        category = self.category_var.get()
        ticket = self.main_app.ticket_manager.create_ticket(description, category)
        self.ticket_list.insert(tk.END, ticket.description)
    def run(self):
        self.root.mainloop()