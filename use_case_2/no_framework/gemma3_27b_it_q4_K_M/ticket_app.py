import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import datetime
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import io
from PIL import Image, ImageTk


# Database Setup
def create_table():
    conn = sqlite3.connect('ticket_db.db')
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tickets
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       status
                       TEXT
                       DEFAULT
                       'open',
                       description
                       TEXT,
                       category
                       TEXT,
                       opening_date
                       TEXT,
                       last_modification_date
                       TEXT,
                       closing_date
                       TEXT
                   )
                   """)
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS messages
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       ticket_id
                       INTEGER,
                       user_role
                       TEXT,
                       message
                       TEXT,
                       timestamp
                       TEXT,
                       FOREIGN
                       KEY
                   (
                       ticket_id
                   ) REFERENCES tickets
                   (
                       id
                   )
                       )
                   """)
    conn.commit()
    conn.close()


create_table()


# --- Microservices ---
def get_open_tickets_in_period(hours):
    conn = sqlite3.connect('ticket_db.db')
    cursor = conn.cursor()
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(hours=hours)
    cursor.execute("SELECT COUNT(*) FROM tickets WHERE opening_date BETWEEN ? AND ? AND status != 'closed'",
                   (start_date.isoformat(), end_date.isoformat()))
    count = cursor.fetchone()[0]
    conn.close()
    return count


def get_average_resolution_time():
    conn = sqlite3.connect('ticket_db.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT strftime('%Y-%m', opening_date) as month, AVG(JULIANDAY(closing_date) - JULIANDAY(opening_date)) AS avg_resolution_time FROM tickets WHERE closing_date IS NOT NULL GROUP BY month")
    data = cursor.fetchall()
    conn.close()
    return data


def cluster_tickets_by_category():
    conn = sqlite3.connect('ticket_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT category, status FROM tickets WHERE status = 'active'")
    data = cursor.fetchall()
    conn.close()

    categories = list(set([item[0] for item in data]))

    category_indices = {category: i for i, category in enumerate(categories)}

    X = [[category_indices[item[0]] for item in data]]

    kmeans = KMeans(n_clusters=3, random_state=0, n_init=10)
    kmeans.fit(X)

    category_counts = defaultdict(int)
    for item in data:
        category = item[0]
        cluster = kmeans.labels_[data.index(item)]
        category_counts[(category, cluster)] += 1

    return category_counts


# --- GUI ---
class TicketManagementApp:
    def __init__(self, master):
        self.master = master
        master.title("University Ticket Management System")

        self.user_role = tk.StringVar(value="user")  # "user" or "helpdesk"
        self.setup_login_page()

    def setup_login_page(self):
        tk.Label(self.master, text="Select User Role:").pack()
        ttk.Radiobutton(self.master, text="User", variable=self.user_role, value="user").pack()
        ttk.Radiobutton(self.master, text="Helpdesk", variable=self.user_role, value="helpdesk").pack()
        ttk.Button(self.master, text="Login", command=self.setup_main_page).pack()

    def setup_main_page(self):
        self.login_frame.destroy()  # Destroy the login frame
        self.login_frame = tk.Frame(self.master)
        self.login_frame.pack()

        # Ticket List
        self.ticket_list = ttk.Treeview(self.login_frame,
                                        columns=("ID", "Status", "Category", "Opening Date", "Last Modified Date"),
                                        show="headings")
        self.ticket_list.heading("ID", text="ID")
        self.ticket_list.heading("Status", text="Status")
        self.ticket_list.heading("Category", text="Category")
        self.ticket_list.heading("Opening Date", text="Opening Date")
        self.ticket_list.heading("Last Modified Date", text="Last Modified Date")
        self.ticket_list.pack()

        self.load_tickets()

        # Buttons
        if self.user_role.get() == "user":
            self.add_ticket_button = ttk.Button(self.login_frame, text="Add Ticket", command=self.add_ticket)
            self.add_ticket_button.pack()
            self.modify_ticket_button = ttk.Button(self.login_frame, text="Modify Ticket", command=self.modify_ticket)
            self.modify_ticket_button.pack()

        else:  # helpdesk
            self.change_status_button = ttk.Button(self.login_frame, text="Change Status", command=self.change_status)
            self.change_status_button.pack()
            self.view_messages_button = ttk.Button(self.login_frame, text="View Messages", command=self.view_messages)
            self.view_messages_button.pack()

        # Microservices buttons
        self.microservice1_button = ttk.Button(self.login_frame, text="Tickets Opened in Last 24 Hours",
                                               command=lambda: self.show_microservice_result(1,
                                                                                             "Tickets Opened in Last 24 Hours"))
        self.microservice1_button.pack()
        self.microservice2_button = ttk.Button(self.login_frame, text="Average Resolution Time by Month",
                                               command=lambda: self.show_microservice_result(2,
                                                                                             "Average Resolution Time by Month"))
        self.microservice2_button.pack()
        self.microservice3_button = ttk.Button(self.login_frame, text="Active Tickets by Category",
                                               command=lambda: self.show_microservice_result(3,
                                                                                             "Active Tickets by Category"))
        self.microservice3_button.pack()

    def load_tickets(self):
        conn = sqlite3.connect('ticket_db.db')
        cursor = conn.cursor()
        if self.user_role.get() == "helpdesk":
            cursor.execute("SELECT * FROM tickets")
        else:
            cursor.execute("SELECT * FROM tickets WHERE status IN ('open', 'active')")
        tickets = cursor.fetchall()

        for ticket in tickets:
            self.ticket_list.insert("", "end", values=ticket)

        conn.close()

    def add_ticket(self):
        self.add_ticket_window = tk.Toplevel(self.master)
        self.add_ticket_window.title("Add Ticket")

        tk.Label(self.add_ticket_window, text="Description:").grid(row=0, column=0)
        self.description_entry = tk.Entry(self.add_ticket_window)
        self.description_entry.grid(row=0, column=1)

        tk.Label(self.add_ticket_window, text="Category (facility, it, service):").grid(row=1, column=0)
        self.category_entry = tk.Entry(self.add_ticket_window)
        self.category_entry.grid(row=1, column=1)

        add_button = ttk.Button(self.add_ticket_window, text="Add", command=self.insert_ticket)
        add_button.grid(row=2, column=0, columnspan=2)

    def insert_ticket(self):
        description = self.description_entry.get()
        category = self.category_entry.get()

        conn = sqlite3.connect('ticket_db.db')
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tickets (description, category, opening_date, last_modification_date) VALUES (?, ?, ?, ?)",
            (description, category, datetime.datetime.now().isoformat(), datetime.datetime.now().isoformat()))

        conn.commit()
        conn.close()

        self.load_tickets()
        self.add_ticket_window.destroy()

    def modify_ticket(self):
        selected_item = self.ticket_list.selection()
        if not selected_item:
            messagebox.showinfo("Info", "Please select a ticket to modify.")
            return

        ticket_id = self.ticket_list.item(selected_item[0])['values'][0]

        self.modify_ticket_window = tk.Toplevel(self.master)
        self.modify_ticket_window.title("Modify Ticket")

        tk.Label(self.modify_ticket_window, text="Description:").grid(row=0, column=0)
        self.description_entry = tk.Entry(self.modify_ticket_window)
        self.description_entry.grid(row=0, column=1)

        modify_button = ttk.Button(self.modify_ticket_window, text="Modify",
                                   command=lambda: self.update_ticket(ticket_id))
        modify_button.grid(row=1, column=0, columnspan=2)

        # Load current description
        conn = sqlite3.connect('ticket_db.db')
        cursor = conn.cursor()
        cursor.execute("SELECT description FROM tickets WHERE id = ?", (ticket_id,))
        description = cursor.fetchone()[0]
        self.description_entry.insert(0, description)
        conn.close()

    def update_ticket(self, ticket_id):
        new_description = self.description_entry.get()
        conn = sqlite3.connect('ticket_db.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE tickets SET description = ? WHERE id = ?", (new_description, ticket_id))
        conn.commit()
        conn.close()
        self.load_tickets()
        self.modify_ticket_window.destroy()

    def change_status(self):
        selected_item = self.ticket_list.selection()
        if not selected_item:
            messagebox.showinfo("Info", "Please select a ticket to change status.")
            return

        ticket_id = self.ticket_list.item(selected_item[0])['values'][0]
        current_status = self.ticket_list.item(selected_item[0])['values'][1]

        if current_status == "open":
            new_status = "active"
        elif current_status == "active":
            new_status = "closed"
        else:
            messagebox.showinfo("Info", "Cannot change status from closed.")
            return

        conn = sqlite3.connect('ticket_db.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE tickets SET status = ? WHERE id = ?", (new_status, ticket_id))
        conn.commit()
        conn.close()
        self.load_tickets()

    def view_messages(self):
        selected_item = self.ticket_list.selection()
        if not selected_item:
            messagebox.showinfo("Info", "Please select a ticket to view messages.")
            return

        ticket_id = self.ticket_list.item(selected_item[0])['values'][0]

        self.messages_window = tk.Toplevel(self.master)
        self.messages_window.title("Ticket Messages")

        self.messages_list = tk.Listbox(self.messages_window, width=50, height=10)
        self.messages_list.pack()

        conn = sqlite3.connect('ticket_db.db')
        cursor = conn.cursor()
        cursor.execute("SELECT user_role, message, timestamp FROM messages WHERE ticket_id = ?", (ticket_id,))
        messages = cursor.fetchall()
        for message in messages:
            self.messages_list.insert(tk.END, f"{message[0]}: {message[1]} ({message[2]})")

        # Add message entry
        self.message_entry = tk.Entry(self.messages_window, width=50)
        self.message_entry.pack()
        send_button = ttk.Button(self.messages_window, text="Send Message",
                                 command=lambda: self.send_message(ticket_id))
        send_button.pack()

        conn.close()

    def send_message(self, ticket_id):
        message = self.message_entry.get()
        user_role = "helpdesk" if self.user_role.get() == "helpdesk" else "user"
        timestamp = datetime.datetime.now().isoformat()
        conn = sqlite3.connect('ticket_db.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (ticket_id, user_role, message, timestamp) VALUES (?, ?, ?, ?)",
                       (ticket_id, user_role, message, timestamp))
        conn.commit()
        conn.close()
        self.view_messages()  # Refresh the message list
        self.message_entry.delete(0, tk.END)

    def show_microservice_result(self, service_number, title):
        if service_number == 1:
            result = get_open_tickets_in_period(24)
            messagebox.showinfo(title, f"Number of tickets opened in the last 24 hours: {result}")
        elif service_number == 2:
            data = get_average_resolution_time()
            messagebox.showinfo(title, f"Average resolution time by month: {data}")
        elif service_number == 3:
            category_counts = cluster_tickets_by_category()
            messagebox.showinfo(title, f"Active tickets by category: {category_counts}")
        else:
            messagebox.showinfo("Error", "Invalid service number.")


# --- Main ---
if __name__ == "__main__":
    root = tk.Tk()
    app = TicketManagementApp(root)
    root.mainloop()