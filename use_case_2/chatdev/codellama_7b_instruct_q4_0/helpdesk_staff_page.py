import tkinter as tk
from tkinter import ttk
class HelpDeskStaffPage(tk.Frame):
    def __init__(self, parent):
        # Set up the GUI layout
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        # Add widgets to the GUI
        self.staff_label = ttk.Label(self, text="Helpdesk Staff:")
        self.staff_entry = ttk.Entry(self)
        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.staff_label.grid(row=0, column=0)
        self.staff_entry.grid(row=0, column=1)
        self.submit_button.grid(row=1, column=0)
    def submit(self):
        # Submit the helpdesk staff and display the final page
        staff = self.staff_entry.get()
        if staff != "":
            self.parent.show_final_page()
        else:
            print("Invalid helpdesk staff")