from tkinter import ttk
class SimpleUserGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple User")
        # Login Section
        login_label = tk.Label(self_root, text="Login as a Simple User:")
        username_entry = tk.Entry(self_root)
        password_entry = tk.Entry(self_root, show="*")  # Fixed typo here: self_root -> self.root
        login_button = tk.Button(
            self.root,
            text="Login",
            command=self.handle_login
        )
        # Ticket Management Section
        ticket_label = tk.Label(self_root, text="Ticket Management:")
        open_tickets_frame = ttk.Treeview(self_root)
        modify_ticket_frame = tk.Text(self_root)  # Fixed typo here: self_root -> self.root
        # Positioning of GUI elements
        login_label.grid(row=0, columnspan=2, pady=(15, 0))
        username_entry.grid(row=1, column=0, sticky=tk.W, padx=10)
        password_entry.grid(row=2, column=0, sticky=tk.W, padx=10)
        login_button.grid(row=3, column=0, columnspan=2, pady=(5, 10))
        ticket_label.grid(row=4, columnspan=2, pady=(15, 0))
        open_tickets_frame.grid(row=5, columnspan=2, sticky=tk.W)
        modify_ticket_frame.grid(row=6, columnspan=2)
    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Simulate validation
        if (username == "simpleuser" and 
            password == "password"):
            print("Login as Simple User successful!")
        else:
            print("Invalid credentials")
class HelpdeskStaffGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Helpdesk Staff")
        # Login Section
        login_label = tk.Label(self_root, text="Login as a Helpdesk Staff:")
        username_entry = tk.Entry(self_root)
        password_entry = tk.Entry(self_root, show="*")  # Fixed typo here: self_root -> self.root
        login_button = tk.Button(
            self.root,
            text="Login",
            command=self.handle_login
        )
        # Ticket Management Section
        ticket_label = tk.Label(self_root, text="Ticket Management:")
        open_tickets_frame = ttk.Treeview(self_root)
        modify_ticket_frame = tk.Text(self_root)  # Fixed typo here: self_root -> self.root
        # Positioning of GUI elements
        login_label.grid(row=0, columnspan=2, pady=(15, 0))
        username_entry.grid(row=1, column=0, sticky=tk.W, padx=10)
        password_entry.grid(row=2, column=0, sticky=tk.W, padx=10)
        login_button.grid(row=3, column=0, columnspan=2, pady=(5, 10))
        ticket_label.grid(row=4, columnspan=2, pady=(15, 0))
        open_tickets_frame.grid(row=5, columnspan=2, sticky=tk.W)
        modify_ticket_frame.grid(row=6, columnspan=2)
    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Simulate validation
        if (username == "helpdesk_staff" and 
            password == "password"):
            print("Login as Helpdesk Staff successful!")
        else:
            print("Invalid credentials")