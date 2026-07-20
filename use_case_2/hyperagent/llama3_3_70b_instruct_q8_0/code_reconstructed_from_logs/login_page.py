import tkinter as tk

class LoginPage:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Ticket Management System")

        # Create role selection buttons
        self.role_label = tk.Label(self.window, text="Select your role:")
        self.role_label.pack()

        self.helpdesk_button = tk.Button(self.window, text="Helpdesk Staff", command=self.helpdesk_login)
        self.helpdesk_button.pack()

        self.user_button = tk.Button(self.window, text="Simple User", command=self.user_login)
        self.user_button.pack()

    def helpdesk_login(self):
        # Navigate to helpdesk dashboard
        self.window.destroy()
        import helpdesk_dashboard

    def user_login(self):
        # Navigate to user dashboard
        self.window.destroy()
        import user_dashboard

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    login_page = LoginPage()
    login_page.run()