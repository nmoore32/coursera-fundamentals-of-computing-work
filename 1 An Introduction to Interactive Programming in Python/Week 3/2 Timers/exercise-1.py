##
# Create a simple timer function
#
from tkinter import Label, Tk
from datetime import timedelta


class Timer():

    def __init__(self):
        self.root = Tk()
        self.timer_label = Label(text="")
        self.timer_label.pack()
        self.seconds = 0
        self.now = str(timedelta(seconds=self.seconds))
        self.tick()
        self.root.mainloop()

    def tick(self):
        self.timer_label.configure(text=self.now)
        self.seconds += 1
        self.now = str(timedelta(seconds=self.seconds))
        self.root.after(1000, self.tick)


t1, t2 = Timer(), Timer()
