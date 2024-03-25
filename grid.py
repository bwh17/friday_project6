from tkinter import *
from tkinter import ttk

def sign_up():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    print("Name:", name)
    print("Email:", email)
    print("Password:", password)

root = Tk()
root.title("Sign Up")

#widgets
Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5)
email_entry = Entry(root, width=30)
email_entry.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=5)
password_entry = Entry(root, width=30)
password_entry.grid(row=2, column=1, padx=10, pady=5)

#button
ttk.Button(root, text="Sign Up Now", command=sign_up).grid(row=3, padx=10, pady=10)

root.mainloop()