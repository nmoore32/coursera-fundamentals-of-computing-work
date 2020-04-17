##
# Draws a polyline (open polygon) based on a series of mouse clicks
#
from tkinter import Button, Canvas, Tk

root = Tk()

# Initialize variables to track positions clicked
first_pos = []
second_pos = []


def select_point(click):
    '''Function to store selected points'''
    global first_pos, second_pos
    # Store new click coordinates if first_pos if empty
    if not first_pos:
        first_pos.append(click.x)
        first_pos.append(click.y)
    # Store new click coordinates in second_pos if it's empty but first_pos isn't
    elif not second_pos:
        second_pos.append(click.x)
        second_pos.append(click.y)
        draw_line()
    # Record previous click coordinates in first_pos and update second_pos with new coordinates
    else:
        first_pos[0] = second_pos[0]
        first_pos[1] = second_pos[1]
        second_pos[0] = click.x
        second_pos[1] = click.y
        draw_line()


def draw_line():
    '''Draw a line connecting the first_pos and second_pos coordinates'''
    C.create_line(first_pos[0], first_pos[1], second_pos[0], second_pos[1])


def clear():
    '''Clear the current canvas and the stored coordinates'''
    global first_pos, second_pos
    C.delete('all')
    first_pos = []
    second_pos = []


# Create canvas and bind it to select_point function via mouse click
C = Canvas(root, width=500, height=500)
C.bind('<Button-1>', select_point)
C.pack()

# Create clear button
clear_button = Button(root, text='Clear',
                      font='TkDefaultFont, 32', command=clear)
clear_button.pack()

root.mainloop()
