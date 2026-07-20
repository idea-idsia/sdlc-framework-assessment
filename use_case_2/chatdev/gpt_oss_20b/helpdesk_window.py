'''
helpdesk_window.py: A very small stub that represents the Help‑Desk UI.
'''
import tkinter as tk
from tkinter import ttk
from detail_window import DetailWindow
class HelpDeskWindow:
    """
    Simple Tkinter window for creating tickets from user input.
    """
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(self.master)
        self.window.title("HelpDesk")
        self.window.geometry("300x200")
        self._create_widgets()
    # --------------------------------------------------------------
    def _create_widgets(self):
        """Create UI elements."""
        self.ticket_id_label = tk.Label(self.window, text="Ticket ID:")
        self.ticket_id_label.pack()
        self.ticket_id_entry = tk.Entry(self.window)
        self.ticket_id_entry.pack()
        self.comment_label = tk.Label(self.window, text="Comment:")
        self.comment_label.pack()
        self.comment_entry = tk.Entry(self.window)
        self.comment_entry.pack()
        self.post_button = ttk.Button(self.window, text="Post", command=self._post_comment)
        self.post_button.pack()
    # --------------------------------------------------------------
    def _post_comment(self):
        """Post a comment to the ticket."""
        try:
            ticket_id = int(self.ticket_id_entry.get())
        except ValueError:
            ticket_id = None
        if ticket_id:
            from database import DatabaseHandler
            db_handler = DatabaseHandler()
            db_handler.add_message(ticket_id, self.comment_entry.get())
            self.comment_entry.delete(0, tk.END)
            # Open the detail window for the ticket
            DetailWindow(self.window, ticket_id)