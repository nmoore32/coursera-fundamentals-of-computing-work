from tkinter import *

root = Tk()

# Define functions


def print_input(event):
    print(e.get())


# Create and display entry field
e = Entry(root, width=50, borderwidth=5)
e.pack()
e.bind('<Return>', print_input)

root.mainloop()
