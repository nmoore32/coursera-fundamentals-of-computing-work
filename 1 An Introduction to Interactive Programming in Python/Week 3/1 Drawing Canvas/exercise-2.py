##
# Create a 96x96 canvas and draw the letter "X" with font size 48 in upper left.
#

from tkinter import Canvas, NW, Tk

root = Tk()

C = Canvas(root, width=96, height=96)
C.grid(row=0, column=0)
# anchor=NW sets the northwest corner of the text element as the reference point
C.create_text(0, 0, text='X', font=('TkDefaultFont', 48), anchor=NW)

root.mainloop()
