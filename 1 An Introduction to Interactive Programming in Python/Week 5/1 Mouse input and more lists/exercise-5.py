##
# Draw a 10x10 grid of balls on a canvas
#
from tkinter import Canvas, Tk

root = Tk()

# Define constants
RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * RADIUS + 2
HEIGHT = 2 * GRID_SIZE * RADIUS + 2

C = Canvas(root, width=WIDTH, height=HEIGHT)
C.pack()
for i in range(GRID_SIZE):
    x_pos = 22 + i * 40
    for j in range(GRID_SIZE):
        y_pos = 22 + j * 40
        C.create_oval(x_pos - RADIUS, y_pos - RADIUS,
                      x_pos + RADIUS, y_pos + RADIUS, fill='blue', outline='blue')

root.mainloop()
