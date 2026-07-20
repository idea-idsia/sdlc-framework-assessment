'''
The TicketManagementSystem class that represents the main window of the application.
'''
import tkinter as tk
from database import Database
class TicketManagementSystem:
    def __init__(self, root):
        self.root = root
        self.db = Database("application.db")
        self.label = tk.Label(self.root, text="Description:")
        self.label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.category_label = tk.Label(self.root, text="Category:")
        self.category_label.pack()
        self.category_entry = tk.Entry(self.root)
        self.category_entry.pack()
        self.button = tk.Button(self.root, text="Create Ticket", command=self.create_ticket)
        self.button.pack()
    def create_ticket(self):
        description = self.entry.get()
        category = self.category_entry.get()
        data = (description, category, 'open')
        self.db.insert_data("tickets", data)
    def run(self):
        self.root.mainloop()