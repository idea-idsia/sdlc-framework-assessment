import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import date

class TicketManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket Management App")
        self.conn = sqlite3.connect('tickets.db')
        self.cursor = self.conn.cursor()
        self.user_type = None

        # Login page
        self.login_page()

    def login_page(self):
        self.clear_frame()
        tk.Label(self.root, text="Select User Type").pack()
        tk.Button(self.root, text="Helpdesk Staff", command=lambda: self.select_user_type("helpdesk")).pack()
        tk.Button(self.root, text="Simple User", command=lambda: self.select_user_type("simple")).pack()

    def select_user_type(self, user_type):
        self.user_type = user_type
        if user_type == "helpdesk":
            self.helpdesk_page()
        else:
            self.simple_user_page()

    def helpdesk_page(self):
        self.clear_frame()
        tk.Button(self.root, text="View Tickets", command=self.view_tickets).pack()

    def simple_user_page(self):
        self.clear_frame()
        tk.Button(self.root, text="Insert New Ticket", command=self.insert_new_ticket).pack()
        tk.Button(self.root, text="View and Modify Tickets", command=self.view_and_modify_tickets).pack()

    def view_tickets(self):
        self.clear_frame()
        tickets = self.cursor.execute("SELECT * FROM tickets").fetchall()
        for ticket in tickets:
            tk.Label(self.root, text=f"Ticket {ticket[0]}: {ticket[1]} - {ticket[2]} - {ticket[3]}").pack()

    def insert_new_ticket(self):
        self.clear_frame()
        category = tk.StringVar()
        description = tk.Text(self.root)
        tk.OptionMenu(self.root, category, "facility management", "technical IT", "services complaints").pack()
        description.pack()
        tk.Button(self.root, text="Insert Ticket", command=lambda: self.insert_ticket(category.get(), description.get("1.0", tk.END))).pack()

    def view_and_modify_tickets(self):
        self.clear_frame()
        tickets = self.cursor.execute("SELECT * FROM tickets WHERE status IN ('open', 'active')").fetchall()
        for ticket in tickets:
            tk.Label(self.root, text=f"Ticket {ticket[0]}: {ticket[1]} - {ticket[2]} - {ticket[3]}").pack()

    def insert_ticket(self, category, description):
        self.cursor.execute("INSERT INTO tickets (category, description) VALUES (?, ?)", (category, description))
        self.conn.commit()
        messagebox.showinfo("Ticket Inserted", "Ticket inserted successfully")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicketManagementApp(root)
    root.mainloop()