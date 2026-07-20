import tkinter as tk
from tkinter import messagebox

class LoginPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login Page")

        self.username_label = tk.Label(self.root, text="Username")
        self.username_label.pack()

        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        # TO DO: Implement authentication logic
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "password":
            print("Login successful")
            # Create a new instance of TicketManagementApp
            self.root.destroy()
            TicketManagementApp()
        else:
            messagebox.showerror("Invalid credentials", "Please try again")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    login_page = LoginPage()
    login_page.run()