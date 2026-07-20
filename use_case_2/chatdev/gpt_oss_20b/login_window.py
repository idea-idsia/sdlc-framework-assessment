'''
Login window for selecting the application role.
'''
import tkinter as tk
from tkinter import messagebox
class LoginWindow(tk.Tk):
    """
    A window that allows the user to select the application role.
    """
    def __init__(self, on_role_selected=None):
        super().__init__()
        self.on_role_selected = on_role_selected  # Store callback
        self.title("Login")
        self.geometry("300x150")
        self.role_var = tk.StringVar(value="customer")
        tk.Label(self, text="Select role:").pack(pady=5)
        tk.Radiobutton(self, text="Customer", variable=self.role_var, value="customer").pack()
        tk.Radiobutton(self, text="Helpdesk", variable=self.role_var, value="helpdesk").pack()
        tk.Button(self, text="Login", command=self._proceed).pack(pady=10)
    # ----------------------------------------------------------------------
    def _proceed(self):
        """Invoke the role selection callback and close the window."""
        role = self.role_var.get()
        if self.on_role_selected:
            self.on_role_selected(role)  # Pass selected role to callback
        self.destroy()