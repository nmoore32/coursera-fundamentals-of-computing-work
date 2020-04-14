from tkinter import *
from random import randrange

root = Tk()


def number_to_fortune(number):
    '''Converts a number into one of 8 fortunes'''
    if number == 0:
        return 'Yes, for sure!'
    elif number == 1:
        return 'Probably yes.'
    elif number == 2:
        return 'Seems like yes...'
    elif number == 3:
        return 'Definitely not!'
    elif number == 4:
        return 'Probably not.'
    elif number == 5:
        return 'I really doubt it...'
    elif number == 6:
        return 'Not sure, check back later!'
    elif number == 7:
        return 'I really can\'t tell'
    else:
        return 'Input error'


def mystical_octosphere(event):
    '''Returns a fortune to answer the given question'''
    question = e.get()
    print(question)
    print("You shake the mystical octosphere")

    answer_number = randrange(0, 8)
    answer_fortune = number_to_fortune(answer_number)

    print("The cloudy liquid swirls, and a reply comes into view...")
    print(f"The mytical octosphere says...{answer_fortune}")
    print()


e = Entry(root, width=50, borderwidth=5)
e.bind('<Return>', mystical_octosphere)
e.pack()


root.mainloop()
