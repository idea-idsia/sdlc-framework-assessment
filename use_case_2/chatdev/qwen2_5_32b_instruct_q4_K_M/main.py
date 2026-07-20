'''
Main execution file which initializes the application.
Initializes GUI and sets up necessary components for ticket management system.
'''
import tkinter as tk
from gui import LoginGUI
def main():
    root = tk.Tk()
    login_gui = LoginGUI(root)
    login_gui.pack(side="top", fill="both", expand=True)
    root.mainloop()
if __name__ == "__main__":
    main()