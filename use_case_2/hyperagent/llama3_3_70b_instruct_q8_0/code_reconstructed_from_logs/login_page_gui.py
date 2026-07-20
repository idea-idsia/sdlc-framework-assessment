import tkinter as tk

class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("300x200")

        # Create a label and dropdown menu for user role
        tk.Label(self, text="Select your role:").pack()
        roles = ['Helpdesk', 'User']
        variable = tk.StringVar(self)
        variable.set(roles[0])  # default value
        option_menu = tk.OptionMenu(self, variable, *roles)
        option_menu.pack()

        # Create a button to proceed to the ticket management system
        def proceed():
            role = variable.get()
            if role == 'Helpdesk':
                # Open helpdesk ticket management GUI
                HelpdeskTicketManagement().mainloop()
            else:
                # Open user ticket management GUI
                UserTicketManagement().mainloop()

        tk.Button(self, text="Proceed", command=proceed).pack()

class HelpdeskTicketManagement(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Helpdesk Ticket Management")
        self.geometry("800x600")

        # Create a label to display tickets
        tk.Label(self, text="Tickets:").pack()
        # TO DO: Implement ticket management GUI for helpdesk staff

class UserTicketManagement(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User Ticket Management")
        self.geometry("800x600")

        # Create a label to display tickets
        tk.Label(self, text="Tickets:").pack()
        # TO DO: Implement ticket management GUI for users

if __name__ == "__main__":
    LoginPage().mainloop()