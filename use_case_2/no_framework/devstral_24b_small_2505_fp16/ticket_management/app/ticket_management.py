# app/ticket_management.py

import tkinter as tk
from database import insert_ticket, get_tickets, update_ticket, insert_message, get_messages

class UserApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("User Ticket Management")

        # Tickets frame
        self.tickets_frame = tk.Frame(self.root)
        self.tickets_frame.pack(side=tk.LEFT)

        # Messages frame
        self.messages_frame = tk.Frame(self.root)
        self.messages_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.ticket_listbox = tk.Listbox(self.tickets_frame)
        self.ticket_listbox.bind('<<ListboxSelect>>', self.show_ticket_messages)
        self.ticket_listbox.pack(fill=tk.BOTH, expand=True)

        self.message_textarea = tk.Text(self.messages_frame)
        self.message_textarea.pack(fill=tk.BOTH, expand=True)

        # Create new ticket button
        self.create_button = tk.Button(self.root, text="Create New Ticket", command=self.create_ticket)
        self.create_button.pack(side=tk.BOTTOM)

    def run(self):
        self.refresh_tickets()
        self.root.mainloop()

    def refresh_tickets(self):
        self.ticket_listbox.delete(0, tk.END)
        tickets = get_tickets(status='open')
        for ticket in tickets:
            self.ticket_listbox.insert(tk.END, f"ID: {ticket[0]} - Status: {ticket[3]}")

    def show_ticket_messages(self, event):
        selection = self.ticket_listbox.curselection()
        if not selection:
            return

        ticket_id = self.ticket_listbox.get(selection[0]).split()[1]
        messages = get_messages(ticket_id)

        self.message_textarea.delete(1.0, tk.END)
        for message in messages:
            self.message_textarea.insert(tk.END, f"{message[3]}: {message[2]}\n")

    def create_ticket(self):
        description = "Sample ticket description"
        category = "facility management"  # Replace with actual input
        insert_ticket(description, category)
        self.refresh_tickets()

class HelpdeskApp(UserApp):  # Inherit from UserApp to reuse functionality
    def __init__(self):
        super().__init__()
        self.root.title("Helpdesk Ticket Management")

    def refresh_tickets(self):
        self.ticket_listbox.delete(0, tk.END)
        tickets = get_tickets()
        for ticket in tickets:
            self.ticket_listbox.insert(tk.END, f"ID: {ticket[0]} - Status: {ticket[3]}")