'''
Implements a GUI for ticket management and provides basic functionalities to interact with the database.
'''
from tkinter import ttk, messagebox
import tkinter as tk
from database import Database
class TicketManagementApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Ticket Management Web Application")
        self.geometry("800x600")
        # Create a container for the menu
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        # Create the menu bar
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Ticket", command=self.create_new_ticket)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit_app)
        menubar.add_cascade(label="File", menu=filemenu)
        # Create the help menu
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help", command=self.show_help)
        menubar.add_cascade(label="Help", menu=helpmenu)
        # Create the button for creating a new ticket
        create_ticket_button = tk.Button(container, text="New Ticket", command=self.create_new_ticket)
        create_ticket_button.pack()
        # Create the label and entry field for entering the ticket number
        ticket_number_label = ttk.Label(container, text="Ticket Number:")
        self.ticket_number_entry = tk.Entry(container, grid=False)
        ticket_number_label.grid(row=0, column=0)
        self.ticket_number_entry.grid(row=0, column=1)
        # Create the label and entry field for entering the description
        description_label = ttk.Label(container, text="Description:")
        self.description_entry = tk.Entry(container)
        description_label.grid(row=1, column=0)
        self.description_entry.grid(row=1, column=1)
        # Create the label and entry field for entering the category
        category_label = ttk.Label(container, text="Category:")
        self.category_entry = tk.Entry(container)
        category_label.grid(row=2, column=0)
        self.category_entry.grid(row=2, column=1)
        # Create the button for saving the current ticket
        save_button = tk.Button(container, text="Save Ticket", command=self.save_ticket)
        save_button.pack()
        # Create the button for deleting a ticket
        delete_button = tk.Button(container, text="Delete Ticket", command=self.delete_ticket)
        delete_button.pack()
        # Create the listbox for displaying tickets
        self.tickets_listbox = tk.Listbox(container)
        self.tickets_listbox.grid(row=3, column=0, columnspan=2)
        # Load all tickets from the database and display them in the listbox
        self.load_all_tickets()
    def create_new_ticket(self):
        """Creates a new ticket with the entered number, description, and category"""
        # Get the values from the entry fields
        if not self.ticket_number_entry.get():
            messagebox.showinfo("Error", "Please enter a ticket number")
            return
        number = self.ticket_number_entry.get()
        description = self.description_entry.get()
        category = self.category_entry.get()
        # Create a new ticket object with these values
        new_ticket = Ticket(number, description, category)
        # Save the ticket to the database
        self.database.save_ticket(new_ticket)
        # Load all tickets from the database and display them in the listbox
        self.load_all_tickets()
    def delete_ticket(self):
        """Deletes the selected ticket from the database"""
        # Get the index of the selected item in the listbox
        selection = self.tickets_listbox.curselection()
        if len(selection) > 0:
            # Delete the selected item from the database
            self.database.delete_ticket(selection[0])
            # Load all tickets from the database and display them in the listbox
            self.load_all_tickets()
    def load_all_tickets(self):
        """Loads all tickets from the database and displays them in the listbox"""
        for ticket in self.database.get_tickets():
            self.tickets_listbox.insert("end", str(ticket))