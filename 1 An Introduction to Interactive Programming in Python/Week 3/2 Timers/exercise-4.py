##
# Create a circle that increases in radius by 1 pixel every tenth of a second
#
from tkinter import Canvas, Tk

root = Tk()

# Create constants
WIDTH = 500
HEIGHT = 500

# Create a variable to store current radius
r = 1

# Create and display canvas
C = Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
C.pack()

# Draw circle
x = WIDTH // 2
y = HEIGHT // 2
C.create_oval(x - r, y - r, x + r, y + r, outline='red', tag='circ')


def increase_radius():
    '''Increments the radius and draws the new circle. Repeats every tenth of a second'''
    global r
    r += 1
    C.coords('circ', x - r, y - r, x + r, y + r)
    root.after(100, increase_radius)


root.after(100, increase_radius)
root.mainloop()
