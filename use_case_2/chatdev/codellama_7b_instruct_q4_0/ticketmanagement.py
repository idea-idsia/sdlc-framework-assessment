# ticket_management.py
import tkinter as tk
import database
class TicketManagement(tk.Frame):
    def __init__(self, parent):
        # Set up the widgets and layout of the frame
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        # Add widgets to the frame
        self.ticket_label = tk.Label(self, text="Ticket:")
        self.ticket_entry = tk.Entry(self)
        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
    def submit(self):
        # Submit the ticket and display the helpdesk staff page
        ticket = self.ticket_entry.get()
        if database.insert_ticket(ticket):
            helpdesk_staff_page.HelpDeskStaffPage(self.parent)