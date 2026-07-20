'''
User interface module for the ticket management application.
'''
import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import logging
logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
class UserInterface:
    def __init__(self, master, db):
        self.master = master
        self.db = db
        master.title("Ticket Management System")
        self.style = ttk.Style()
        self.style.configure("TButton", padding=5)
        self.style.configure("TLabel", padding=5)
        self.create_widgets()
    def create_widgets(self):
        self.tickets_frame = ttk.Frame(self.master, padding=10)
        self.tickets_frame.pack(fill=tk.BOTH, expand=True)
        self.tickets_list = tk.Listbox(self.tickets_frame, width=80, height=15)
        self.tickets_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar = ttk.Scrollbar(self.tickets_frame, orient=tk.VERTICAL, command=self.tickets_list.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tickets_list['yscrollcommand'] = self.scrollbar.set
        self.refresh_tickets()
        self.button_frame = ttk.Frame(self.master, padding=10)
        self.button_frame.pack()
        self.create_button = ttk.Button(self.button_frame, text="Create Ticket", command=self.create_ticket)
        self.create_button.pack(side=tk.LEFT, padx=5)
        self.change_status_button = ttk.Button(self.button_frame, text="Change Status", command=self.change_ticket_status)
        self.change_status_button.pack(side=tk.LEFT, padx=5)
        self.delete_button = ttk.Button(self.button_frame, text="Delete Ticket", command=self.delete_ticket)
        self.delete_button.pack(side=tk.LEFT, padx=5)
    def refresh_tickets(self):
        self.tickets_list.delete(0, tk.END)
        tickets = self.db.get_tickets()
        for ticket in tickets:
            self.tickets_list.insert(tk.END, f"ID: {ticket[0]}, Status: {ticket[1]}, Description: {ticket[2]}, Category: {ticket[3]}, Opening Date: {ticket[4]}, Last Modified: {ticket[5]}, Closing Date: {ticket[6]}")
    def change_ticket_status(self):
        try:
            selected_index = self.tickets_list.curselection()[0]
            ticket_data = self.tickets_list.get(selected_index).split(', ')
            ticket_id = int(ticket_data[0].split(': ')[1])
            new_status = tk.simpledialog.askstring("Change Status", "Enter new status (open, active, closed):")
            if new_status and new_status.lower() in ("open", "active", "closed"):
                if self.db.update_ticket_status(ticket_id, new_status.lower()):
                    self.refresh_tickets()
                else:
                    messagebox.showerror("Error", "Failed to update ticket status.")
            else:
                messagebox.showerror("Error", "Invalid status. Please enter 'open', 'active', or 'closed'.")
        except IndexError:
            messagebox.showerror("Error", "Please select a ticket to change the status.")
        except Exception as e:
            logging.error(f"Error changing ticket status: {e}")
            messagebox.showerror("Error", f"An error occurred: {e}")
    def delete_ticket(self):
        try:
            selected_index = self.tickets_list.curselection()[0]
            ticket_data = self.tickets_list.get(selected_index).split(', ')
            ticket_id = int(ticket_data[0].split(': ')[1])
            if messagebox.askyesno("Delete Ticket", "Are you sure you want to delete this ticket?"):
                if self.db.delete_ticket(ticket_id):
                    self.refresh_tickets()
                else:
                    messagebox.showerror("Error", "Failed to delete ticket.")
        except IndexError:
            messagebox.showerror("Error", "Please select a ticket to delete.")
        except Exception as e:
            logging.error(f"Error deleting ticket: {e}")
            messagebox.showerror("Error", f"An error occurred: {e}")
    def create_ticket(self):
        try:
            status = tk.simpledialog.askstring("Create Ticket", "Enter status:")
            description = tk.simpledialog.askstring("Create Ticket", "Enter description:")
            category = tk.simpledialog.askstring("Create Ticket", "Enter category:")
            opening_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            last_modification_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            closing_date = ""
            if status and description:
                if self.db.insert_ticket(status, description, category, opening_date, last_modification_date, closing_date):
                    self.refresh_tickets()
                else:
                    messagebox.showerror("Error", "Failed to create ticket.")
            else:
                messagebox.showerror("Error", "Status and description are required.")
        except Exception as e:
            logging.error(f"Error creating ticket: {e}")
            messagebox.showerror("Error", f"An error occurred: {e}")
    def run(self):
        self.master.mainloop()