'''
The LoginWindow class that handles user authentication.
'''
import tkinter as tk
from database import Database
class LoginWindow:
    def __init__(self, root, db, start_application):
        self.root = root
        self.db = db
        self.start_application = start_application
        self.label = tk.Label(self.root, text="Username:")
        self.label.pack()
        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack()
        self.label_password = tk.Label(self.root, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()
        self.button = tk.Button(self.root, text="Login", command=self.login)
        self.button.pack()
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        # Implement authentication logic here
        # For example, using a database:
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        if user:
            stored_password = user[2]  # Assuming the password is the third column
            # Using hashlib to hash the input password for comparison
            import hashlib
            if hashlib.sha256(password.encode()).hexdigest() == stored_password:
                self.start_application()
            else:
                print("Incorrect password")
        else:
            print("User not found")
    def run(self):
        self.root.mainloop()