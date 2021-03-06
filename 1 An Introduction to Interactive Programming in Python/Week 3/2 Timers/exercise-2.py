##
# Create a simple timer function with buttons to start, stop, and reset the timer
#
from tkinter import Button, Label, Tk
from datetime import timedelta


class Timer():

    def __init__(self):
        self.root = Tk()
        # Create timer label
        self.timer_label = Label(text='')
        self.timer_label.grid(row=0, column=1)

        # Create buttons
        start_button = Button(text='Start', command=self.start)
        start_button.grid(row=1, column=0)
        stop_botton = Button(text='Stop', command=self.stop)
        stop_botton.grid(row=1, column=1)
        reset_button = Button(text='Reset', command=self.reset)
        reset_button.grid(row=1, column=2)

        # Create variables to track and display time elapsed
        self.seconds = 0
        self.now = str(timedelta(seconds=self.seconds))
        # Create variable to determine whether to increment the clock
        self.doTick = True

        # Call the tick() function
        self.tick()
        self.root.mainloop()

    def tick(self):
        '''Increment the timer if it's running'''
        if self.doTick:
            self.timer_label.configure(text=self.now)
            self.seconds += 1
            self.now = str(timedelta(seconds=self.seconds))
            self.root.after(1000, self.tick)
        else:
            self.root.after(1000, self.tick)

    def start(self):
        '''Start the timer if it's not running'''
        self.doTick = True

    def stop(self):
        '''Stop the timer if it is running'''
        self.doTick = False

    def reset(self):
        '''Reset and stop the timer'''
        self.seconds = 0
        self.now = str(timedelta(seconds=self.seconds))
        # Update the label otherwise it keeps reading the pre-reset value until restarted
        self.timer_label.configure(text=self.now)
        self.doTick = False


Timer()
