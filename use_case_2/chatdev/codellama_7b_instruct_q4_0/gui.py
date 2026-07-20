import tkinter as tk
from tkinter import ttk
import user_management
import ticket_management
import helpdesk_staff_page
class Gui(tk.Frame):
    def __init__(self, parent):
        # Set up the GUI layout
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        # Add widgets to the GUI
        user_management.UserManagement(self)
        ticket_management.TicketManagement(self)
        helpdesk_staff_page.HelpDeskStaffPage(self)
    def setup(self):
        # Set up the GUI elements
        self.title("My Application")
        self.geometry("800x600")
        self.resizable(False, False)
    def start(self):
        try:
            # Start the application
            self.mainloop()
        except Exception as e:
            print(f"Error occurred while starting the application: {e}")