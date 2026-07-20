# Import necessary libraries
import tkinter as tk
from ticket_manager import TicketManager
'''
Main GUI class.
It provides a graphical user interface for the main application window.
'''
class MainGUI:
    def __init__(self, master, ticket_manager):
        self.master = master
        self.ticket_manager = ticket_manager
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.label = tk.Label(self.frame, text="Tickets:")
        self.label.pack()
        self.listbox = tk.Listbox(self.frame)
        self.listbox.pack()
        self.button = tk.Button(self.frame, text="Create Ticket", command=self.create_ticket)
        self.button.pack()
    def create_ticket(self):
        # Create new ticket
        description = "New ticket"
        category = "Category"
        ticket = self.ticket_manager.create_ticket(description, category)
        # Add ticket to listbox
        self.listbox.insert(tk.END, ticket.description)