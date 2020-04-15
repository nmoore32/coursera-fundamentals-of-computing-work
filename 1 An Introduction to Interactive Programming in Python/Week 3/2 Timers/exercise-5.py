##
# Create a program that determines how quickly you can click a button
#
from datetime import timedelta
from tkinter import Button, Label, Tk


root = Tk()

# Create variable to track elapsed time
centiseconds = 0
doTick = False

# Define functions


def tick():
    '''Increments the timer if running'''
    if doTick:
        global centiseconds
        # The slice is to remove 4 places datetime includes after the hundredths of seconds place
        timer_label.configure(
            text=str(timedelta(seconds=centiseconds / 100))[:-4])
        centiseconds += 1
        root.after(10, tick)
    else:
        root.after(10, tick)


def click():
    '''Toggles the active state'''
    global doTick
    global centiseconds
    if doTick:
        doTick = False
        centiseconds = 0
    else:
        doTick = True


# Create and display timer label
timer_label = Label(root, text='0:00:00:00')
timer_label.pack()
# Create and display button
my_button = Button(root, text='Click here', command=click)
my_button.pack()

tick()
root.mainloop()
