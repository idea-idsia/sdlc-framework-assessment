import tkinter as tk
from tkinter import ttk
class TicketManagement(tk.Frame):
    def __init__(self, parent):
        # Set up the GUI layout
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        # Add widgets to the GUI
        self.ticket_label = ttk.Label(self, text="Ticket:")
        self.ticket_entry = ttk.Entry(self)
        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.ticket_label.grid(row=0, column=0)
        self.ticket_entry.grid(row=0, column=1)
        self.submit_button.grid(row=1, column=0)
    def submit(self):
        # Submit the ticket and display the helpdesk staff page
        ticket = self.ticket_entry.get()
        if ticket != "":
            self.parent.show_helpdesk_staff_page()
        else:
            print("Invalid ticket")