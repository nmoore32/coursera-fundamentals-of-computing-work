##
# Display color of clicked circle
#
from tkinter import Canvas, Label, Tk

# Create root window
root = Tk()

# Define constants
RADIUS = 50


def display_color(click):
    '''Displays the color of the clicked circle'''
    # Returns the fill color (capitalized) of closest widget to click point
    color_label.configure(text=C.itemcget(click.widget.find_closest(
        click.x, click.y), 'fill').capitalize())


# Create canvas
C = Canvas(root, width=500, height=500)
C.pack()

# Create label to display color
color_label = Label(root, text='', font='TkDefaultFont, 32')
color_label.pack()

# Create three different colored circles
blue_circle = C.create_oval(100 - RADIUS, 60 - RADIUS, 100 + RADIUS,
                            60 + RADIUS, fill='blue')
red_circle = C.create_oval(400 - RADIUS, 60 - RADIUS, 400 + RADIUS,
                           60 + RADIUS, fill='red')
green_circle = C.create_oval(250 - RADIUS, 250 - RADIUS, 250 + RADIUS,
                             250 + RADIUS, fill='green')

# Bind circles to display_color function via mouse click
C.tag_bind(blue_circle, '<Button-1>', display_color)
C.tag_bind(red_circle, '<Button-1>', display_color)
C.tag_bind(green_circle, '<Button-1>', display_color)


root.mainloop()
