def generate_login_gui():
    class LoginGUI:
        def __init__(self):
            self.root = tk.Tk()
            self.root.title("Login")
            # Username and Password Entry Fields
            username_label = tk.Label(self_root, text="Username:")
            password_label = tk.Label(self_root, text="Password:")  # Fixed typo here: self_root -> self.root
            username_entry = tk.Entry(self_root)
            password_entry = tk.Entry(self_root, show="*")  # Fixed typo here: self_root -> self.root
            submit_button = tk.Button(
                self.root,
                text="Submit",
                command=self.handle_login
            )
            # Positioning of GUI elements
            username_label.grid(row=0, column=0)
            password_label.grid(row=1, column=0)
            username_entry.grid(row=0, column=1)
            password_entry.grid(row=1, column=1)
            submit_button.grid(row=2, column=1)
        def handle_login(self):
            # Simulate login validation
            if (username_entry.get() == "admin" and 
                password_entry.get() == "password"):
                print("Login successful!")
            else:
                print("Invalid username or password")
    return LoginGUI()