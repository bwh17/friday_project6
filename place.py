from tkinter import *

root = Tk()
root.title("Login")

#widgets
Label(root, text="Username:").place(x=0, y=20)
username_entry = Entry(root, width=30)
username_entry.place(x=80, y=20)

Label(root, text="Password:").place(x=0, y=50)
password_entry = Entry(root, width=30)
password_entry.place(x=80, y=50)

#button
Button(root, text="Login").place(x=80, y=90)

root.mainloop()