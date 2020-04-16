##
# Change radius of white ball centered on canvas in response to up and down keypresses.
# tkinter
#
from tkinter import Canvas, Tk

root = Tk()

WIDTH = 500
HEIGHT = 500
RADIUS_INCREMENT = 5
radius = 20

# Create canvas
C = Canvas(root, width=500, height=500, bg='black')
C.pack()

# Draw circle
x = WIDTH // 2
y = HEIGHT // 2
C.create_oval(x - radius, y - radius, x + radius,
              y + radius, fill='white', tag='circ')


# Define functions for changing the radius
def increment_radius(key):
    global radius
    radius += RADIUS_INCREMENT
    update_circle()


def decrement_radius(key):
    global radius
    if radius > RADIUS_INCREMENT:
        radius -= RADIUS_INCREMENT
        update_circle()
    else:
        return


def update_circle():
    C.coords('circ', x - radius, y - radius, x + radius, y + radius)


root.bind('<Up>', increment_radius)
root.bind('<Down>', decrement_radius)

root.mainloop()
