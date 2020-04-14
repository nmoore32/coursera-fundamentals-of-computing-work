from tkinter import *

root = Tk()

color = (0, 0, 0)


# Define functions
def print_color():
    print(color)


def set_red():
    global color
    color = (255, 0, 0)


def set_blue():
    global color
    color = (0, 0, 255)


# Create buttons
print_button = Button(root, text='Print', command=print_color)
red_button = Button(root, text='Red', command=set_red)
blue_button = Button(root, text='Blue', command=set_blue)

# Display buttons
print_button.pack()
red_button.pack()
blue_button.pack()

root.mainloop()
