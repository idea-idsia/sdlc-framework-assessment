from tkinter import Tk, Label, Entry, Button, StringVar

class LoginPage:
    def __init__(self, master):
        self.master = master
        master.title("Ticket Management Application Login")

        # User type selection (Helpdesk Staff or Simple User)
        self.user_type_var = StringVar()
        user_type_label = Label(master, text="User Type:")
        user_type_label.pack()

        helpdesk_radio = Button(master, text="Helpdesk Staff", command=self.login_as_helpdesk)
        helpdesk_radio.pack()

        simple_user_radio = Button(master, text="Simple User", command=self.login_as_simple_user)
        simple_user_radio.pack()

    def login_as_helpdesk(self):
        print("Logging in as Helpdesk Staff")

    def login_as_simple_user(self):
        print("Logging in as Simple User")

if __name__ == "__main__":
    root = Tk()
    app = LoginPage(root)
    root.mainloop()