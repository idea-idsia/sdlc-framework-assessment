# Import necessary libraries
import tkinter as tk
from main import MainApp
from ticket_manager import TicketManager
'''
Login GUI class.
It provides a graphical user interface for logging in to the application.
'''
class LoginGUI:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.label = tk.Label(self.frame, text="Username:")
        self.label.pack()
        self.entry = tk.Entry(self.frame)
        self.entry.pack()
        self.button = tk.Button(self.frame, text="Login", command=self.login)
        self.button.pack()
    def login(self):
        username = self.entry.get()
        # Authenticate user
        if username:
            # Create ticket manager
            db_manager = DBManager()
            ticket_manager = TicketManager(db_manager)
            # Create main application window
            main_window = tk.Tk()
            main_app = MainApp(main_window, ticket_manager)
            main_app.run()