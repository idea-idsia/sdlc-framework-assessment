'''
Main entry point of the ticket management application.
Initializes the GUI.
'''
import tkinter as tk
from ticket_gui import TicketGUI
import traceback
def main():
    try:
        root = tk.Tk()
        root.title("Ticket Management System")
        gui = TicketGUI(root)
        gui.pack(fill=tk.BOTH, expand=True)  # Fill and expand for better layout
        root.mainloop()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        traceback.print_exc()  # Print the full traceback for debugging
if __name__ == "__main__":
    main()