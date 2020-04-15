##
# Create a canvas and print "It works!" on the canvas
#

from tkinter import Canvas, Tk

root = Tk()

C = Canvas(root, width=300, height=200)
C.pack()
C.create_text(140, 95, text='It works!')

root.mainloop()
