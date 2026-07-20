from tkinter import *
import tkinter.messagebox

def on_radio_click():
    if radio_var.get() == 1:
        tkinter.messagebox.showinfo("User Type", "Helpdesk Staff")
    else:
        tkinter.messagebox.showinfo("User Type", "Simple User")

root = Tk()
root.title("Login Page")

radio_var = IntVar()

helpdesk_staff_radio = Radiobutton(root, text="Helpdesk Staff", variable=radio_var, value=1)
simple_user_radio = Radiobutton(root, text="Simple User", variable=radio_var, value=2)

helpdesk_staff_radio.grid(row=0, column=0)
simple_user_radio.grid(row=0, column=1)

login_button = Button(root, text="Login", command=lambda: on_radio_click())
login_button.grid(row=1, columnspan=2)

root.mainloop()