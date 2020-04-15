##
# Use a timer to toggle a canvas background color every three seconds
#
from tkinter import Canvas, Tk

root = Tk()

C = Canvas(root, width=300, height=200, bg='blue')
C.pack()


def change_background():
    if C['background'] == 'blue':
        C.configure(bg='red')
    else:
        C.configure(bg='blue')
    root.after(3000, change_background)


root.after(3000, change_background)
root.mainloop()
