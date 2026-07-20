'''
Detail view for displaying and editing ticket information.
'''
import tkinter as tk
from tkinter import messagebox
from ticket import Ticket
class DetailWindow(tk.Toplevel):
    """
    A window to display ticket details and allow posting comments.
    """
    def __init__(self, master, ticket_id: int):
        super().__init__(master)
        self.ticket_id = ticket_id
        self.title(f"Ticket #{ticket_id}")
        self.geometry("400x300")
        self.ticket = self._load_ticket()
        self._create_widgets()
    # --------------------------------------------------------------
    def _load_ticket(self) -> Ticket:
        """
        Load the ticket data and attach any associated messages.
        """
        from database import DatabaseHandler
        db_handler = DatabaseHandler()
        # Load the base ticket information
        base_ticket = db_handler.get_ticket_by_id(self.ticket_id)
        if not base_ticket:
            messagebox.showerror("Error", f"Ticket with ID {self.ticket_id} not found.")
            self.destroy()
            return None
        # Attach any stored messages
        base_ticket.messages = [
            msg["message"] for msg in db_handler.messages if msg["ticket_id"] == self.ticket_id
        ]
        return base_ticket
    # --------------------------------------------------------------
    def _create_widgets(self):
        """Create UI elements for ticket details."""
        if not self.ticket:
            return
        tk.Label(self, text=f"Description: {self.ticket.description}").pack()
        tk.Label(self, text=f"Category: {self.ticket.category}").pack()
        tk.Label(self, text=f"Status: {self.ticket.status}").pack()
        self.comment_entry = tk.Entry(self, width=50)
        self.comment_entry.pack()
        tk.Button(self, text="Post Comment", command=self._post_comment).pack()
        self.comments_text = tk.Text(self, height=10)
        self.comments_text.pack()
        self._update_comments()
    # --------------------------------------------------------------
    def _post_comment(self):
        """Post a comment to the ticket."""
        comment = self.comment_entry.get()
        if comment:
            from database import DatabaseHandler
            db_handler = DatabaseHandler()
            db_handler.add_message(self.ticket_id, comment)
            self.ticket.messages.append(comment)
            self._update_comments()
            self.comment_entry.delete(0, tk.END)
    # --------------------------------------------------------------
    def _update_comments(self):
        """Update the comment list in the UI."""
        self.comments_text.delete("1.0", tk.END)
        for msg in self.ticket.messages:
            self.comments_text.insert(tk.END, msg + "\n")