##
# Create multiple independent timers with start, stop, and reset buttons.
#
from tkinter import Button, Label, Tk
from datetime import timedelta


class Timer():

    def __init__(self, row):
        '''Initalize Timer.
        @param row - the row for the Timer grid position
        '''
        # Create timer label
        self.timer_label = Label(text='')
        self.timer_label.grid(row=row, column=1)

        # Create buttons
        start_button = Button(text='Start', command=self.start)
        start_button.grid(row=row+1, column=0)
        stop_botton = Button(text='Stop', command=self.stop)
        stop_botton.grid(row=row+1, column=1)
        reset_button = Button(text='Reset', command=self.reset)
        reset_button.grid(row=row+1, column=2)

        # Create variables to track and display time elapsed
        self.seconds = 0
        self.now = str(timedelta(seconds=self.seconds))
        # Create variable to determine whether to increment the clock
        self.doTick = True

        # Call the tick() function
        self.tick()

    def tick(self):
        '''Increment the timer if it's running'''
        if self.doTick:
            self.timer_label.configure(text=self.now)
            self.seconds += 1
            self.now = str(timedelta(seconds=self.seconds))
            root.after(1000, self.tick)
        else:
            root.after(1000, self.tick)

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


root = Tk()
t1 = Timer(0)
t2 = Timer(2)
root.mainloop()
