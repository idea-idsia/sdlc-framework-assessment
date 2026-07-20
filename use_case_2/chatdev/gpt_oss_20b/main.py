'''
Entry point that runs the application and starts the FastAPI service.
'''
import tkinter as tk
from database import DatabaseHandler
from user_window import UserWindow
def launch_role(role):
    """
    Dispatch role strings to the appropriate UI component.
    """
    if role == 'customer':
        UserWindow(tk.Tk())
    elif role == 'helpdesk':
        # The helpdesk UI remains unchanged
        pass
    else:
        raise ValueError(f"Unrecognized role: {role}")