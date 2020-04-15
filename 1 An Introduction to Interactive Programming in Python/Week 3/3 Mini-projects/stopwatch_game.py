##
# Stopwatch game, try to stop on whole seconds
#
from datetime import timedelta
from tkinter import Button, Canvas, SW, Tk

root = Tk()

# Define varibles to track time, state, and score
tenth_of_second = 0
doTick = False
total_clicks = 0
total_score = 0

# Define functions


def start():
    '''Start the timer'''
    global doTick
    doTick = True


def stop():
    '''Stop the timer and check the score'''
    global doTick
    doTick = False
    check_score()


def reset():
    '''Reset the game'''
    global tenth_of_second, total_score, total_clicks, doTick
    tenth_of_second = 0
    total_clicks = 0
    total_score = 0
    doTick = False
    # Reset the text fields
    C.itemconfig('score', text=f"{total_score}/{total_clicks}")
    C.itemconfig('timer', text='0:00:0')


def check_score():
    '''Adjust the score'''
    global total_clicks, total_score
    total_clicks += 1
    if tenth_of_second % 10 == 0:
        total_score += 1
    C.itemconfig('score', text=f"{total_score}/{total_clicks}")


def tick():
    '''Increment the timer'''
    global tenth_of_second
    if doTick:
        tenth_of_second += 1
        string = str(tenth_of_second)
        while len(string) < 4:
            string = f"0{string}"
        C.itemconfig('timer', text=f"{string[0:1]}:{string[1:3]}:{string[-1]}")
        root.after(100, tick)
    else:
        root.after(100, tick)


# Create canvas and display canvas
C = Canvas(root, width=300, height=200, bg='black')
C.grid(row=0, column=1, rowspan=3)
C.create_text(150, 100, text='0:00:0', fill='white',
              font='TkDefaultFont, 48', tag='timer')
C.create_text(260, 20, text='0/0', fill='green',
              font='TkDefaultFont, 32', tag='score')

# Create buttons display buttons
start_button = Button(root, text='start', command=start)
stop_button = Button(root, text='stop', command=stop)
reset_button = Button(root, text='reset', command=reset)
start_button.grid(row=0, column=0)
stop_button.grid(row=1, column=0)
reset_button.grid(row=2, column=0)

tick()
root.mainloop()
