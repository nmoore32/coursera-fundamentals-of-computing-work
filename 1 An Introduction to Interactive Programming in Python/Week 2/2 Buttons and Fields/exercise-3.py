from tkinter import *

root = Tk()

count = 0

# Define functions


def reset():
    '''Resets count to zero'''
    global count
    count = 0


def increment():
    '''Increments count by one'''
    global count
    count += 1


def decrement():
    '''Decrements count by one'''
    global count
    count -= 1


def print_count():
    '''Prints the current count'''
    print(count)


# Create buttons
button_reset = Button(root, text='Reset', command=reset)
button_increment = Button(root, text='Increment', command=increment)
button_decrement = Button(root, text='Decrement', command=decrement)
button_print = Button(root, text='Print', command=print_count)

# Display buttons
button_reset.pack()
button_increment.pack()
button_decrement.pack()
button_print.pack()

root.mainloop()
