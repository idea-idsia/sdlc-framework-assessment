import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class TicketManagementApp:
    def __init__(self, root):
        self.root = root
        self.conn = sqlite3.connect('tickets.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

        # Login page
        self.login_page()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                category TEXT CHECK(category IN ('facility_management', 'technical_it', 'services_complaints')) NOT NULL,
                status TEXT CHECK(status IN ('open', 'active', 'closed')) NOT NULL DEFAULT 'open',
                opening_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                last_modification_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                closing_date DATETIME
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticket_id INTEGER NOT NULL,
                message TEXT NOT NULL,
                user_type TEXT CHECK(user_type IN ('helpdesk', 'simple')) NOT NULL,
                created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (ticket_id) REFERENCES tickets (id)
            );
        """)
        self.conn.commit()

    def login_page(self):
        self.clear_frame()
        tk.Label(self.root, text="Login Page").pack()
        tk.Label(self.root, text="User Type:").pack()
        user_type_var = tk.StringVar()
        user_type_menu = ttk.Combobox(self.root, textvariable=user_type_var)
        user_type_menu['values'] = ('helpdesk', 'simple')
        user_type_menu.pack()
        tk.Button(self.root, text="Login", command=lambda: self.ticket_management_page(user_type_var.get())).pack()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def ticket_management_page(self, user_type):
        self.clear_frame()
        if user_type == 'helpdesk':
            self.helpdesk_ticket_management_page()
        else:
            self.simple_user_ticket_management_page()

    def helpdesk_ticket_management_page(self):
        tk.Label(self.root, text="Helpdesk Ticket Management Page").pack()
        tk.Button(self.root, text="View All Tickets", command=self.view_all_tickets).pack()
        tk.Button(self.root, text="Insert New Ticket", command=self.insert_new_ticket).pack()

    def simple_user_ticket_management_page(self):
        tk.Label(self.root, text="Simple User Ticket Management Page").pack()
        tk.Button(self.root, text="View Open Tickets", command=self.view_open_tickets).pack()
        tk.Button(self.root, text="Insert New Ticket", command=self.insert_new_ticket).pack()

    def view_all_tickets(self):
        self.clear_frame()
        tk.Label(self.root, text="All Tickets").pack()
        tickets = self.cursor.execute("SELECT * FROM tickets").fetchall()
        for ticket in tickets:
            tk.Label(self.root, text=f"Ticket {ticket[0]} - {ticket[3]}").pack()
            tk.Button(self.root, text="View Ticket", command=lambda ticket_id=ticket[0]: self.view_ticket(ticket_id)).pack()

    def view_open_tickets(self):
        self.clear_frame()
        tk.Label(self.root, text="Open Tickets").pack()
        tickets = self.cursor.execute("SELECT * FROM tickets WHERE status='open'").fetchall()
        for ticket in tickets:
            tk.Label(self.root, text=f"Ticket {ticket[0]} - {ticket[3]}").pack()
            tk.Button(self.root, text="View Ticket", command=lambda ticket_id=ticket[0]: self.view_ticket(ticket_id)).pack()

    def insert_new_ticket(self):
        self.clear_frame()
        tk.Label(self.root, text="Insert New Ticket").pack()
        description_var = tk.StringVar()
        category_var = tk.StringVar()
        tk.Entry(self.root, textvariable=description_var).pack()
        category_menu = ttk.Combobox(self.root, textvariable=category_var)
        category_menu['values'] = ('facility_management', 'technical_it', 'services_complaints')
        category_menu.pack()
        tk.Button(self.root, text="Insert", command=lambda: self.insert_ticket(description_var.get(), category_var.get())).pack()

    def insert_ticket(self, description, category):
        self.cursor.execute("INSERT INTO tickets (description, category) VALUES (?, ?)", (description, category))
        self.conn.commit()
        messagebox.showinfo("Success", "Ticket inserted successfully")

    def view_ticket(self, ticket_id):
        self.clear_frame()
        tk.Label(self.root, text=f"Ticket {ticket_id}").pack()
        ticket = self.cursor.execute("SELECT * FROM tickets WHERE id=?", (ticket_id,)).fetchone()
        tk.Label(self.root, text=f"Description: {ticket[1]}").pack()
        tk.Label(self.root, text=f"Category: {ticket[2]}").pack()
        tk.Label(self.root, text=f"Status: {ticket[3]}").pack()
        messages = self.cursor.execute("SELECT * FROM messages WHERE ticket_id=?", (ticket_id,)).fetchall()
        for message in messages:
            tk.Label(self.root, text=f"{message[3]}: {message[2]}").pack()
        message_var = tk.StringVar()
        tk.Entry(self.root, textvariable=message_var).pack()
        tk.Button(self.root, text="Add Message", command=lambda: self.add_message(ticket_id, message_var.get())).pack()

    def add_message(self, ticket_id, message):
        self.cursor.execute("INSERT INTO messages (ticket_id, message, user_type) VALUES (?, ?, 'helpdesk')", (ticket_id, message))
        self.conn.commit()
        messagebox.showinfo("Success", "Message added successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicketManagementApp(root)
    root.mainloop()