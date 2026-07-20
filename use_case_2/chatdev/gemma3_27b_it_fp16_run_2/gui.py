'''
GUI class for the ticket management application.
Handles user interface elements and event handling.
'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ticket_manager import TicketManager
class GUI:
    def __init__(self, master, db_manager):
        """
        Initializes the GUI with the master window and database manager.
        """
        self.master = master
        self.db_manager = db_manager
        self.ticket_manager = TicketManager(db_manager)
        self.user_type = tk.StringVar(value="simple_user")  # Initialize with simple_user
        self.create_widgets()
    def create_widgets(self):
        """
        Creates the GUI widgets.
        """
        # User Type Selection
        def toggle_user_type():
            if self.user_type.get() == "simple_user":
                self.user_type.set("helpdesk")
            else:
                self.user_type.set("simple_user")
            self.refresh_ticket_list()  # Refresh on change
        user_type_button = tk.Button(self.master, text="Toggle Helpdesk Mode", command=toggle_user_type)
        user_type_button.pack(pady=5)
        # Notebook for tabs
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(pady=10, padx=10, fill="both", expand=True)
        # Ticket List Tab
        self.ticket_list_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.ticket_list_tab, text="Tickets")
        self.create_ticket_list_tab()
        # New Ticket Tab
        self.new_ticket_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.new_ticket_tab, text="New Ticket")
        self.create_new_ticket_tab()
    def create_ticket_list_tab(self):
        """
        Creates the widgets for the ticket list tab.
        """
        self.ticket_tree = ttk.Treeview(self.ticket_list_tab, columns=("ID", "Status", "Category", "Description", "Opening Date", "Last Modified Date"), show="headings")
        self.ticket_tree.heading("ID", text="ID")
        self.ticket_tree.heading("Status", text="Status")
        self.ticket_tree.heading("Category", text="Category")
        self.ticket_tree.heading("Description", text="Description")
        self.ticket_tree.heading("Opening Date", text="Opening Date")
        self.ticket_tree.heading("Last Modified Date", text="Last Modified Date")
        self.ticket_tree.pack(pady=10, padx=10, fill="both", expand=True)
        self.refresh_ticket_list()
        #Buttons
        if self.user_type.get() == "helpdesk":
            modify_button = tk.Button(self.ticket_list_tab, text="Modify Status", command=self.modify_ticket_status)
            modify_button.pack(pady=5)
            view_details_button = tk.Button(self.ticket_list_tab, text="View Details", command=self.view_ticket_details)
            view_details_button.pack(pady=5)
    def create_new_ticket_tab(self):
        """
        Creates the widgets for the new ticket tab.
        """
        tk.Label(self.new_ticket_tab, text="Description:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.description_entry = tk.Entry(self.new_ticket_tab, width=50)
        self.description_entry.grid(row=0, column=1, padx=5, pady=5)
        category_label = tk.Label(self.new_ticket_tab, text="Category:")
        category_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.category_combobox = ttk.Combobox(self.new_ticket_tab, values=["facility management", "technical IT", "services complaints"])
        self.category_combobox.grid(row=1, column=1, padx=5, pady=5)
        self.category_combobox.set("facility management")
        submit_button = tk.Button(self.new_ticket_tab, text="Submit", command=self.submit_new_ticket)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)
    def submit_new_ticket(self):
        """
        Submits a new ticket to the database.
        """
        description = self.description_entry.get()
        category = self.category_combobox.get()
        if not description:
            messagebox.showerror("Error", "Description cannot be empty.")
            return
        ticket_id = self.ticket_manager.create_ticket(description, category)
        if ticket_id is None:
            messagebox.showerror("Error", "Failed to create ticket. Check database connection.")
            return
        self.refresh_ticket_list()
        messagebox.showinfo("Success", "Ticket submitted successfully.")
    def refresh_ticket_list(self):
        """
        Refreshes the ticket list in the treeview.
        """
        for item in self.ticket_tree.get_children():
            self.ticket_tree.delete(item)
        try:
            tickets = self.db_manager.get_tickets(user_type=self.user_type.get())
        except Exception as e:
            messagebox.showerror("Error", f"Error retrieving tickets: {e}")
            return
        for ticket in tickets:
            self.ticket_tree.insert("", "end", values=(ticket['id'], ticket['status'], ticket['category'], ticket['description'], ticket['opening_date'], ticket['last_modified_date']))
    def modify_ticket_status(self):
        """
        Modifies the status of the selected ticket.
        """
        selected_item = self.ticket_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a ticket.")
            return
        ticket_id = self.ticket_tree.item(selected_item[0])['values'][0]
        try:
            ticket = self.db_manager.get_ticket_by_id(ticket_id)
            if ticket is None:
                messagebox.showerror("Error", "Ticket not found.")
                return
            current_status = ticket['status']
        except Exception as e:
            messagebox.showerror("Error", f"Error retrieving ticket: {e}")
            return
        if current_status == "open":
            new_status = "active"
        elif current_status == "active":
            new_status = "closed"
        else:
            messagebox.showinfo("Info", "This ticket is already closed.")
            return
        try:
            self.ticket_manager.update_ticket_status(ticket_id, new_status)
        except Exception as e:
            messagebox.showerror("Error", f"Error updating ticket status: {e}")
            return
        self.refresh_ticket_list()
        messagebox.showinfo("Success", "Ticket status updated successfully.")
    def view_ticket_details(self):
        """
        Opens a new window to display ticket details and messages.
        """
        selected_item = self.ticket_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a ticket.")
            return
        ticket_id = self.ticket_tree.item(selected_item[0])['values'][0]
        try:
            ticket = self.db_manager.get_ticket_by_id(ticket_id)
            if ticket is None:
                messagebox.showerror("Error", "Ticket not found.")
                return
            messages = self.db_manager.get_messages_by_ticket_id(ticket_id)
        except Exception as e:
            messagebox.showerror("Error", f"Error retrieving ticket details: {e}")
            return
        details_window = tk.Toplevel(self.master)
        details_window.title(f"Ticket Details - ID: {ticket_id}")
        tk.Label(details_window, text=f"ID: {ticket['id']}").pack()
        tk.Label(details_window, text=f"Status: {ticket['status']}").pack()
        tk.Label(details_window, text=f"Category: {ticket['category']}").pack()
        tk.Label(details_window, text=f"Description: {ticket['description']}").pack()
        tk.Label(details_window, text=f"Opening Date: {ticket['opening_date']}").pack()
        tk.Label(details_window, text=f"Last Modified Date: {ticket['last_modified_date']}").pack()
        message_listbox = tk.Listbox(details_window, width=60)
        # Clear existing messages before repopulating
        message_listbox.delete(0, tk.END)
        for message in messages:
            message_listbox.insert(tk.END, f"{message['sender']}: {message['content']} ({message['timestamp']})")
        message_listbox.pack()
        message_entry = tk.Entry(details_window, width=50)
        message_entry.pack()
        send_button = tk.Button(details_window, text="Send Message", command=lambda: self.send_message(ticket_id, message_entry.get()))
        send_button.pack()
    def send_message(self, ticket_id, content):
        """
        Sends a new message for the given ticket.
        """
        if not content:
            messagebox.showwarning("Warning", "Message cannot be empty.")
            return
        try:
            self.ticket_manager.add_message(ticket_id, content, self.user_type.get())  # Assuming user_type is available
        except Exception as e:
            messagebox.showerror("Error", f"Error sending message: {e}")
            return
        self.refresh_ticket_list()
        #Refresh the message listbox in the details window
        messages = self.db_manager.get_messages_by_ticket_id(ticket_id)
        self.update_message_listbox(ticket_id, messages)
        messagebox.showinfo("Success", "Message sent successfully.")
    def update_message_listbox(self, ticket_id, messages):
      """
      Updates the message listbox in the details window with the latest messages.
      """
      for window in self.master.toplevels():
          if window.title.startswith("Ticket Details"):
              message_listbox = None
              for widget in window.winfo_children():
                  if isinstance(widget, tk.Listbox):
                      message_listbox = widget
                      break
              if message_listbox:
                  message_listbox.delete(0, tk.END)
                  for message in messages:
                      message_listbox.insert(tk.END, f"{message['sender']}: {message['content']} ({message['timestamp']})")