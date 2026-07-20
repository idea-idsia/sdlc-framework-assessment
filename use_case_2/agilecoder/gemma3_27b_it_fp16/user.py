'''
This module defines the user interface for the ticket management application.
'''
import tkinter as tk
from database import Database
import tkinter.messagebox
import logging
# Configure logging
logging.basicConfig(filename='ticket_management.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')
def handle_exception(e):
    """Logs an exception and displays a user-friendly error message."""
    logging.error(f"An unexpected error occurred: {e}", exc_info=True)
    tkinter.messagebox.showerror("Error", "An unexpected error occurred. Please check the logs for details.")
class TicketUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket Management")
        try:
            self.db = Database('tickets.db')  # Initialize Database instance
            if not self.db.connect():
                raise Exception("Failed to connect to the database.")
            if not self.db.create_table():
                raise Exception("Failed to create table.")
        except Exception as e:
            handle_exception(e)
            return
        self.ticket_list = tk.Listbox(root, width=80)
        self.ticket_list.pack(pady=10)
        self.refresh_tickets()
        self.create_button = tk.Button(root, text="Create Ticket", command=self.create_ticket)
        self.create_button.pack()
        self.delete_button = tk.Button(root, text="Delete Ticket", command=self.delete_ticket)
        self.delete_button.pack()
    def refresh_tickets(self):
        self.ticket_list.delete(0, tk.END)
        try:
            tickets = self.db.get_tickets()
            for ticket in tickets:
                self.ticket_list.insert(tk.END, f"ID: {ticket[0]}, Status: {ticket[1]}, Description: {ticket[2]}, Category: {ticket[3]}")
        except Exception as e:
            handle_exception(e)
    def create_ticket(self):
        try:
            description = tk.simpledialog.askstring("Create Ticket", "Enter description:")
            category = tk.simpledialog.askstring("Create Ticket", "Enter category:")
            if description and category:
                if self.db.insert_ticket(description, category):
                    self.refresh_tickets()
                else:
                    tk.messagebox.showerror("Error", "Failed to create ticket.")
            else:
                tk.messagebox.showwarning("Warning", "Description and category are required.")
        except Exception as e:
            handle_exception(e)
    def delete_ticket(self):
        try:
            selected_index = self.ticket_list.curselection()[0]
            ticket_data = self.ticket_list.get(selected_index).split(', ')
            ticket_id = int(ticket_data[0].split(': ')[1])
            if tk.messagebox.askyesno("Delete Ticket", "Are you sure you want to delete this ticket?"):
                if self.db.delete_ticket(ticket_id):
                    self.refresh_tickets()
                else:
                    tk.messagebox.showerror("Error", "Failed to delete ticket.")
        except IndexError:
            tk.messagebox.showwarning("Warning", "Please select a ticket to delete.")
        except Exception as e:
            handle_exception(e)