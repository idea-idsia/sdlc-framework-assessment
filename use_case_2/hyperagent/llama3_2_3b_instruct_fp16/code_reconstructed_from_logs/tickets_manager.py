import tkinter as tk
from tkinter import messagebox

class TicketManagementApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ticket Management App")

        # Create a frame for the main menu
        self.main_menu_frame = tk.Frame(self.root)
        self.main_menu_frame.pack()

        # Create buttons for simple users and helpdesk users
        self.simple_user_button = tk.Button(self.main_menu_frame, text="Simple User", command=self.simple_user_menu)
        self.simple_user_button.pack(side=tk.LEFT)

        self.helpdesk_user_button = tk.Button(self.main_menu_frame, text="Helpdesk User", command=self.helpdesk_user_menu)
        self.helpdesk_user_button.pack(side=tk.LEFT)

    def simple_user_menu(self):
        # Create a new instance of SimpleUserMenu
        self.simple_user_menu_instance = SimpleUserMenu()
        self.simple_user_menu_instance.run()

    def helpdesk_user_menu(self):
        # Create a new instance of HelpdeskUserMenu
        self.helpdesk_user_menu_instance = HelpdeskUserMenu()
        self.helpdesk_user_menu_instance.run()

    def run(self):
        self.root.mainloop()

class SimpleUserMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple User Menu")

        # Create a frame for the ticket list
        self.ticket_list_frame = tk.Frame(self.root)
        self.ticket_list_frame.pack()

        # Create a button to insert new tickets
        self.insert_ticket_button = tk.Button(self.root, text="Insert New Ticket", command=self.insert_new_ticket)
        self.insert_ticket_button.pack()

    def insert_new_ticket(self):
        # Insert a new ticket into the database
        # TO DO: Implement insertion logic

        # Create a new window to display the inserted ticket
        self.new_ticket_window = tk.Toplevel(self.root)
        self.new_ticket_window.title("New Ticket")

        # Display the inserted ticket in the new window
        # TO DO: Implement display logic

    def run(self):
        self.root.mainloop()

class HelpdeskUserMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Helpdesk User Menu")

        # Create a frame for the ticket list
        self.ticket_list_frame = tk.Frame(self.root)
        self.ticket_list_frame.pack()

        # Create buttons to view and modify tickets
        self.view_ticket_button = tk.Button(self.root, text="View Tickets", command=self.view_tickets)
        self.view_ticket_button.pack()

        self.modify_ticket_button = tk.Button(self.root, text="Modify Ticket", command=self.modify_ticket)
        self.modify_ticket_button.pack()

    def view_tickets(self):
        # View all open and active tickets
        # TO DO: Implement view logic

    def modify_ticket(self):
        # Modify an existing ticket
        # TO DO: Implement modification logic

    def run(self):
        self.root.mainloop()