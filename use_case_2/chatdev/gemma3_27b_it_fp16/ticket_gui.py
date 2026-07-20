'''
GUI for the ticket management system.
Provides functionality to create, view, and manage tickets.
'''
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from ticket import Ticket  # Import the Ticket class
from database import Database  # Import the Database class
class TicketGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.db = Database("ticket_database.db")
        self.create_widgets()
        self.load_tickets()
    def create_widgets(self):
        # Create Ticket Frame
        create_frame = tk.Frame(self, borderwidth=2, relief="groove")
        create_frame.pack(pady=10, padx=10, fill=tk.X)
        tk.Label(create_frame, text="Description:").grid(row=0, column=0, sticky=tk.W)
        self.description_entry = tk.Entry(create_frame, width=40)
        self.description_entry.grid(row=0, column=1, padx=5)
        tk.Label(create_frame, text="Category:").grid(row=1, column=0, sticky=tk.W)
        self.category_entry = tk.Entry(create_frame, width=40)
        self.category_entry.grid(row=1, column=1, padx=5)
        create_button = tk.Button(create_frame, text="Create Ticket", command=self.create_ticket)
        create_button.grid(row=2, column=0, columnspan=2, pady=5)
        # Ticket List Frame
        list_frame = tk.Frame(self, borderwidth=2, relief="groove")
        list_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.ticket_list = tk.Listbox(list_frame, width=60, height=15)
        self.ticket_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.ticket_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.ticket_list.yview)
        self.ticket_list.bind("<<ListboxSelect>>", self.select_ticket)
        # Button Frame
        button_frame = tk.Frame(self)
        button_frame.pack(pady=5)
        self.close_button = tk.Button(button_frame, text="Close Ticket", command=self.close_ticket, state=tk.DISABLED)
        self.close_button.pack(side=tk.LEFT, padx=5)
    def load_tickets(self):
        self.ticket_list.delete(0, tk.END)
        tickets = self.db.get_all_tickets()
        for ticket in tickets:
            self.ticket_list.insert(tk.END, f"ID: {ticket.ticket_id}, Description: {ticket.description}, Category: {ticket.category}, Status: {ticket.status}")
    def create_ticket(self):
        description = self.description_entry.get()
        category = self.category_entry.get()
        # Input validation
        if not description or not category:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        if len(description) > 255:
            messagebox.showerror("Error", "Description is too long (max 255 characters).")
            return
        ALLOWED_CATEGORIES = ["facility management", "technical IT", "services complaints"]
        if category not in ALLOWED_CATEGORIES:
            messagebox.showerror("Error", "Invalid category.  Choose from: " + ", ".join(ALLOWED_CATEGORIES))
            return
        try:
            opening_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.db.create_ticket(description, category, opening_date)
            messagebox.showinfo("Success", "Ticket created successfully.")
            self.load_tickets()  # Refresh the ticket list
            self.description_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to create ticket: {e}")
    def select_ticket(self, event):
        try:
            index = self.ticket_list.curselection()[0]
            ticket_text = self.ticket_list.get(index)
            ticket_id = int(ticket_text.split(",")[0].split(":")[1].strip())
            self.selected_ticket_id = ticket_id
            self.close_button.config(state=tk.NORMAL)
        except IndexError:
            pass
    def close_ticket(self):
        if hasattr(self, 'selected_ticket_id'):
            try:
                self.db.close_ticket(self.selected_ticket_id)
                messagebox.showinfo("Success", "Ticket closed successfully.")
                self.load_tickets()
                self.close_button.config(state=tk.DISABLED)
            except Exception as e:
                messagebox.showerror("Database Error", f"Failed to close ticket: {e}")