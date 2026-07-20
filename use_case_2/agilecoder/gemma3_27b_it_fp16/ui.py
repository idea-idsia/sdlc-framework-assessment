'''
This module defines the user interface for the ticket management application.
'''
import tkinter as tk
import logging
from tkinter import messagebox
logging.basicConfig(filename='ticket_management.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')
def handle_event_error(func):
    """
    Decorator to handle exceptions in event handler functions.
    Logs the error and displays an error message to the user.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred in {func.__name__}. See log for details.")
            return None  # Or handle the error in a more appropriate way
    return wrapper
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
            self.handle_initialization_error(e)
            return  # Prevent further initialization if the database fails
        self.ticket_list = tk.Listbox(root, width=80)
        self.ticket_list.pack(pady=10)
        self.refresh_tickets()
        self.create_button = tk.Button(root, text="Create Ticket", command=self.create_ticket)
        self.create_button.pack()
        self.delete_button = tk.Button(root, text="Delete Ticket", command=self.delete_ticket)
        self.delete_button.pack()
    def handle_initialization_error(self, error):
        messagebox.showerror("Initialization Error", f"Failed to initialize the application. {error}")
        self.root.destroy()  # Close the window if initialization fails
    @handle_event_error
    def refresh_tickets(self):
        self.ticket_list.delete(0, tk.END)
        tickets = self.db.get_tickets()
        for ticket in tickets:
            self.ticket_list.insert(tk.END, f"ID: {ticket[0]}, Status: {ticket[1]}, Description: {ticket[2]}, Category: {ticket[3]}")
    @handle_event_error
    def create_ticket(self):
        description = tk.simpledialog.askstring("Create Ticket", "Enter description:")
        category = tk.simpledialog.askstring("Create Ticket", "Enter category:")
        if description and category:
            if self.db.insert_ticket(description, category):
                self.refresh_tickets()
            else:
                messagebox.showerror("Error", "Failed to create ticket.")
        else:
            messagebox.showwarning("Warning", "Description and category are required.")
    @handle_event_error
    def delete_ticket(self):
        try:
            selected_index = self.ticket_list.curselection()[0]
            ticket_data = self.ticket_list.get(selected_index).split(', ')
            ticket_id = int(ticket_data[0].split(': ')[1])
            if messagebox.askyesno("Delete Ticket", "Are you sure you want to delete this ticket?"):
                if self.db.delete_ticket(ticket_id):
                    self.refresh_tickets()
                else:
                    messagebox.showerror("Error", "Failed to delete ticket.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a ticket to delete.")
        except Exception as e:
            raise  # Let the decorator handle the exception