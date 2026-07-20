import tkinter as tk
from gui import GUI
root = tk.Tk()
root.title("Snake Game")
gui = GUI(root)
gui.pack()
root.mainloop()