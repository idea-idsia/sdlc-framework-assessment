'''
$DOCSTRING
'''
import os
import sys
import tkinter as tk
from PIL import Image, ImageTk
class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        # Add a label to the frame
        self.lbl_icon = tk.Label(self, text="Icon")
        self.lbl_icon.grid(row=0, column=0)
        # Add an entry field to the frame
        self.ent_filepath = tk.Entry(self)
        self.ent_filepath.grid(row=1, column=0)
        # Add a button to the frame
        self.btn_browse = tk.Button(self, text="Browse", command=self.select_icon)
        self.btn_browse.grid(row=2, column=0)
        # Add a label to the frame
        self.lbl_output = tk.Label(self, text="")
        self.lbl_output.grid(row=3, column=0)
    def select_icon(self):
        filepath = tk.filedialog.askopenfilename()
        if filepath:
            try:
                img = Image.open(filepath)
                img = ImageTk.PhotoImage(img)
                self.lbl_output["text"] = "Icon loaded successfully!"
                self.lbl_icon.configure(image=img)
            except Exception as e:
                self.lbl_output["text"] = str(e)
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(master=root)
    app.mainloop()