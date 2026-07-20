import tkinter as tk

class LoginPage:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Login Page')

        # Create role selection dropdown
        self.role_label = tk.Label(self.window, text='Select your role:')
        self.role_label.pack()

        self.roles = ['Helpdesk Staff', 'Simple User']
        self.selected_role = tk.StringVar(self.window)
        self.selected_role.set(self.roles[0])  # default value

        self.role_dropdown = tk.OptionMenu(self.window, self.selected_role, *self.roles)
        self.role_dropdown.pack()

        # Create proceed button
        self.proceed_button = tk.Button(self.window, text='Proceed', command=self.proceed_to_ticket_management)
        self.proceed_button.pack()

        # Create username and password entry fields
        self.username_label = tk.Label(self.window, text='Username:')
        self.username_label.pack()
        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack()

        self.password_label = tk.Label(self.window, text='Password:')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.window, show='*')
        self.password_entry.pack()

    def proceed_to_ticket_management(self):
        selected_role = self.selected_role.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if selected_role == 'Helpdesk Staff':
            # Authenticate helpdesk staff user
            if username == 'helpdesk' and password == 'password':
                print('Proceeding to helpdesk staff ticket management system')
            else:
                print('Invalid username or password')
        elif selected_role == 'Simple User':
            # Authenticate simple user
            if username == 'user' and password == 'password':
                print('Proceeding to simple user ticket management system')
            else:
                print('Invalid username or password')

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    login_page = LoginPage()
    login_page.run()
