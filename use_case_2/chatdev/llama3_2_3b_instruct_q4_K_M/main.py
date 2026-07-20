from user import UserClass as User  # Import and alias User class
from ticket import Ticket
from database import Database, UserClass as UserClass
from microservices import Microservices
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    # ... rest of the code ...
if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()