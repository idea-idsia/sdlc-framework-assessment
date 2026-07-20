import tkinter as tk
from tkinter import ttk
from database import Database
from models import Ticket, Message

class TicketAppGUI:
    def __init__(self, master):
        self.master = master
        master.title("Ticket Management System")

        self.db = Database()

        self.user_type = tk.StringVar(value="user")  # "user" or "helpdesk"
        self.user_type.set("user")

        # User Type Selection
        ttk.Label(master, text="Select User Type:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Radiobutton(master, text="User", variable=self.user_type, value="user").grid(row=0, column=1, padx=5, pady=5)
        ttk.Radiobutton(master, text="Helpdesk", variable=self.user_type, value="helpdesk").grid(row=0, column=2, padx=5, pady=5)

        # Ticket List
        self.ticket_list = tk.Listbox(master, width=80)
        self.ticket_list.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        self.refresh_ticket_list()

        # Ticket Details
        self.ticket_details_label = ttk.Label(master, text="Ticket Details:")
        self.ticket_details_label.grid(row=2, column=0, padx=5, pady=5)
        self.ticket_details_text = tk.Text(master, width=80, height=10)
        self.ticket_details_text.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        # Message Area
        self.message_label = ttk.Label(master, text="Messages:")
        self.message_label.grid(row=4, column=0, padx=5, pady=5)
        self.message_list = tk.Listbox(master, width=80, height=5)
        self.message_list.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

        # Message Entry
        self.message_entry = ttk.Entry(master, width=70)
        self.message_entry.grid(row=6, column=0, padx=5, pady=5)
        self.send_button = ttk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=6, column=1, padx=5, pady=5)

        # Buttons
        self.create_ticket_button = ttk.Button(master, text="Create Ticket", command=self.create_ticket)
        self.create_ticket_button.grid(row=7, column=0, padx=5, pady=5)

        if self.user_type.get() == "helpdesk":
            self.update_status_button = ttk.Button(master, text="Update Status", command=self.update_status)
            self.update_status_button.grid(row=7, column=1, padx=5, pady=5)

        # Ticket Selection Event
        self.ticket_list.bind("<<ListboxSelect>>", self.display_ticket_details)

    def refresh_ticket_list(self):
        self.ticket_list.delete(0, tk.END)
        if self.user_type.get() == "helpdesk":
            tickets = self.db.get_tickets()
        else:
            tickets = self.db.get_tickets(status="open") #Only show open tickets for users
        for ticket in tickets:
            self.ticket_list.insert(tk.END, f"{ticket.id} - {ticket.description} ({ticket.status})")

    def display_ticket_details(self, event):
        selected_index = self.ticket_list.curselection()
        if selected_index:
            selected_ticket_id = int(self.ticket_list.get(selected_index[0]).split(" - ")[0])
            ticket = next((t for t in self.db.get_tickets() if t.id == selected_ticket_id), None)

            if ticket:
                self.ticket_details_text.delete("1.0", tk.END)
                self.ticket_details_text.insert("1.0", f"ID: {ticket.id}\nDescription: {ticket.description}\nCategory: {ticket.category}\nStatus: {ticket.status}\nOpening Date: {ticket.opening_date}\nLast Modification Date: {ticket.last_modification_date}")
                self.display_messages(ticket.id)

    def display_messages(self, ticket_id):
        self.message_list.delete(0, tk.END)
        messages = self.db.get_messages_by_ticket_id(ticket_id)
        for message in messages:
            self.message_list.insert(tk.END, f"{message.sender} ({message.timestamp}): {message.content}")

    def create_ticket(self):
        # Implement ticket creation logic (e.g., using a dialog)
        description = "New Ticket Description"  # Replace with user input
        category = "facility management"  # Replace with user input
        ticket = Ticket(description, category)
        ticket_id = self.db.insert_ticket(ticket)
        self.refresh_ticket_list()
        self.ticket_list.selection_set(ticket_id - 1) # Select the new ticket
        self.display_ticket_details(None)

    def update_status(self):
        selected_index = self.ticket_list.curselection()
        if selected_index:
            selected_ticket_id = int(self.ticket_list.get(selected_index[0]).split(" - ")[0])
            new_status = "active"  # Or "closed"
            self.db.update_ticket_status(selected_ticket_id, new_status)
            self.refresh_ticket_list()

    def send_message(self):
        selected_index = self.ticket_list.curselection()
        if selected_index:
            selected_ticket_id = int(self.ticket_list.get(selected_index[0]).split(" - ")[0])
            message_content = self.message_entry.get()
            message = Message(selected_ticket_id, "user", message_content)
            self.db.insert_message(message)
            self.message_entry.delete(0, tk.END)
            self.display_messages(selected_ticket_id)

# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    gui = TicketAppGUI(root)
    root.mainloop()