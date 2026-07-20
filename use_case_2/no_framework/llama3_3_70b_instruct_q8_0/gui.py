import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class TicketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket Management System")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        # Login Frame
        self.login_frame = tk.Frame(self.notebook)
        self.notebook.add(self.login_frame, text="Login")

        # Ticket Frame
        self.ticket_frame = tk.Frame(self.notebook)
        self.notebook.add(self.ticket_frame, text="Tickets")

        # Message Frame
        self.message_frame = tk.Frame(self.notebook)
        self.notebook.add(self.message_frame, text="Messages")

        # Login Widgets
        tk.Label(self.login_frame, text="Select Role:").pack()
        self.role_var = tk.StringVar()
        self.role_var.set("user")
        tk.Radiobutton(self.login_frame, text="User", variable=self.role_var, value="user").pack()
        tk.Radiobutton(self.login_frame, text="Helpdesk", variable=self.role_var, value="helpdesk").pack()
        tk.Button(self.login_frame, text="Login", command=self.login).pack()

        # Ticket Widgets
        self.ticket_widgets()

        # Message Widgets
        self.message_widgets()

    def login(self):
        role = self.role_var.get()
        if role == "user":
            self.user_tickets()
        elif role == "helpdesk":
            self.helpdesk_tickets()

    def ticket_widgets(self):
        tk.Label(self.ticket_frame, text="Description:").pack()
        self.description_entry = tk.Text(self.ticket_frame, height=5)
        self.description_entry.pack()
        tk.Label(self.ticket_frame, text="Category:").pack()
        self.category_var = tk.StringVar()
        self.category_var.set("facility")
        tk.OptionMenu(self.ticket_frame, self.category_var, "facility", "it", "services").pack()
        tk.Button(self.ticket_frame, text="Create Ticket", command=self.create_ticket).pack()

    def message_widgets(self):
        tk.Label(self.message_frame, text="Message:").pack()
        self.message_entry = tk.Text(self.message_frame, height=5)
        self.message_entry.pack()
        tk.Button(self.message_frame, text="Send Message", command=self.send_message).pack()

    def user_tickets(self):
        # Display open and active tickets
        conn = sqlite3.connect("tickets.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tickets WHERE status IN ('open', 'active')")
        tickets = cursor.fetchall()
        for ticket in tickets:
            print(ticket)
        conn.close()

    def helpdesk_tickets(self):
        # Display all tickets
        conn = sqlite3.connect("tickets.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tickets")
        tickets = cursor.fetchall()
        for ticket in tickets:
            print(ticket)
        conn.close()

    def create_ticket(self):
        description = self.description_entry.get(1.0, tk.END)
        category = self.category_var.get()
        conn = sqlite3.connect("tickets.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tickets (description, category, status) VALUES (?, ?, 'open')", (description, category))
        conn.commit()
        conn.close()

    def send_message(self):
        message = self.message_entry.get(1.0, tk.END)
        # Get ticket id from user input
        ticket_id = 1  # Replace with actual ticket id
        conn = sqlite3.connect("tickets.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (ticket_id, message, sender) VALUES (?, ?, 'user')", (ticket_id, message))
        conn.commit()
        conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicketApp(root)
    root.mainloop()