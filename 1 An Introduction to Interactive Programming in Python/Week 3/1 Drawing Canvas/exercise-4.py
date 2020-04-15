from tkinter import Button, Canvas, Tk

root = Tk()

# Define global variables
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Create canvas
C = Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
C.grid(row=0, column=0, columnspan=2)

# Draw circle
x = WIDTH // 2
y = HEIGHT // 2
# The tag is used to provide a way to refer to the circle
C.create_oval(x - ball_radius, y - ball_radius,
              x + ball_radius, y + ball_radius, outline='white', tag='circ')

# Define functions for changing the radius


def increase_radius():
    global ball_radius
    ball_radius += RADIUS_INCREMENT
    # The .coords method replaces the coordinates of the specified object
    C.coords('circ', x - ball_radius, y - ball_radius,
             x + ball_radius, y + ball_radius)


def decrease_radius():
    global ball_radius
    if ball_radius >= 10:
        ball_radius -= RADIUS_INCREMENT
        C.coords('circ', x - ball_radius, y - ball_radius,
                 x + ball_radius, y + ball_radius)
    else:
        return


# Add buttons to control radius
increase_radius = Button(root, text='Increase radius', command=increase_radius)
increase_radius.grid(row=1, column=0)
decrease_radius = Button(root, text='Decrease radius', command=decrease_radius)
decrease_radius.grid(row=1, column=1)


root.mainloop()
