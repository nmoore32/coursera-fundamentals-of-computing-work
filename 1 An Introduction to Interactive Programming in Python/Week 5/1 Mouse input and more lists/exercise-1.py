##
# Print the position of the mouse on each click
#
from tkinter import Canvas, Tk

root = Tk()


def echo_click(click):
    pos = (click.x, click.y)
    print(pos)


C = Canvas(root, width=300, height=300)
C.bind('<Button-1>', echo_click)
C.pack()

root.mainloop()
