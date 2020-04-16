##
# Print "Pressed up arrow" or "Pressed down arrow" to console when the appropriate key is pressed.
# Using tkinter
#
from tkinter import Frame, Tk

root = Tk()


def upKey(event):
    print("Pressed up arrow")


def downKey(event):
    print("Pressed down arrow")


root.bind("<Up>", upKey)
root.bind("<Down>", downKey)

root.mainloop()
