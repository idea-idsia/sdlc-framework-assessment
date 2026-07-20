import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
def show_login_page():
    root = tk.Tk()
    root.title("Login Page")
    # Set up the login page UI
    image_label = tk.Label(root)
    image_label.pack()
    image = Image.open("login.png")  # Assuming "login.png" is an image file for the login page
    photo = ImageTk.PhotoImage(image)
    image_label['image'] = photo
    image_label.image = photo
    label_user = tk.Label(root, text="Username")
    label_user.pack()
    entry_username = tk.Entry(root)
    entry_username.pack()
    label_password = tk.Label(root, text="Password")
    label_password.pack()
    entry_password = tk.Entry(root, show='*')
    entry_password.pack()
    def login():
        username = entry_username.get()
        password = entry_password.get()
        if username == "helpdesk" and password == "password":
            messagebox.showinfo("Login", "Welcome Help Desk Staff")
        elif username == "user1" and password == "user1":
            messagebox.showinfo("Login", "Welcome User")
        else:
            messagebox.showerror("Error", "Invalid Username or Password")
    login_button = tk.Button(root, text="Login", command=login)
    login_button.pack()
    root.mainloop()