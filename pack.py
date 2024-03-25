from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Simple Calculator")

#widget to display the numbers and results
display = Entry(root, width=30)
display.pack(side=TOP)

#frame to contain the buttons
button_frame = Frame(root)
button_frame.pack(side=TOP)

#buttons
ttk.Button(button_frame, text="7", width=3).pack(side=LEFT, padx=2, pady=2)
ttk.Button(button_frame, text="8", width=3).pack(side=LEFT, padx=2, pady=2)
ttk.Button(button_frame, text="9", width=3).pack(side=LEFT, padx=2, pady=2)
ttk.Button(button_frame, text="/", width=3).pack(side=LEFT, padx=2, pady=2)

ttk.Button(button_frame, text="4", width=3).pack(side=LEFT, padx=2, pady=2)
ttk.Button(button_frame, text="5", width=3).pack(side=LEFT, padx=2, pady=2)
ttk.Button(button_frame, text="6", width=3).pack(side=LEFT, padx=2, pady=2)
ttk.Button(button_frame, text="*", width=3).pack(side=LEFT, padx=2, pady=2)

ttk.Button(button_frame, text="1", width=3).pack(side=LEFT, padx=2, pady=2)
ttk.Button(button_frame, text="2", width=3).pack(side=LEFT, padx=2, pady=2)
ttk.Button(button_frame, text="3", width=3).pack(side=LEFT, padx=2, pady=2)
ttk.Button(button_frame, text="-", width=3).pack(side=LEFT, padx=2, pady=2)

ttk.Button(button_frame, text="0", width=3).pack(side=LEFT, padx=2, pady=2)
ttk.Button(button_frame, text=".", width=3).pack(side=LEFT, padx=2, pady=2)
ttk.Button(button_frame, text="=", width=3).pack(side=LEFT, padx=2, pady=2)
ttk.Button(button_frame, text="+", width=3).pack(side=LEFT, padx=2, pady=2)

root.mainloop()
