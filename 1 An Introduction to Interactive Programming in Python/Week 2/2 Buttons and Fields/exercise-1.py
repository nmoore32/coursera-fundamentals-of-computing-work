from tkinter import *

root = Tk()


def hello_click():
    print('Hello')


def goodbye_click():
    print('Goodbye')


# Create buttons
hello_button = Button(root, text='Hello', command=hello_click)
goodbye_button = Button(root, text='Goodbye', command=goodbye_click)

# Display buttons
hello_button.pack()
goodbye_button.pack()

root.mainloop()
