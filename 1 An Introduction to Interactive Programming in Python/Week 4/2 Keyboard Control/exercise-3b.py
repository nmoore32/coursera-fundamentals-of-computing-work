##
# Displays "Space bar down" on screen as long as space is held down, otherwise displays
# "Space bar up"
# tkinter
#
from tkinter import Label, CENTER, Tk

root = Tk()
# Set size of root window
root.geometry('500x500')
# Set background color of root window
root.configure(bg='black')

label = Label(root, text='Space bar up', font=(
    'TkDefaultFont, 32'), fg='blue', bg='black')
# The following centers a widget with respect to its parent
label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Define functions for pressing and releasing space


def space_down(key):
    label.configure(text='Space bar down', fg='red')


def space_up(key):
    label.configure(text='Space bar up', fg='blue')


# Bind space keypresses and releases to the appropriate functions
root.bind('<KeyPress-space>', space_down)
root.bind('<KeyRelease-space>', space_up)

root.mainloop()
