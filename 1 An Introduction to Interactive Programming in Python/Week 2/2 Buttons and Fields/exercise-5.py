from tkinter import *

root = Tk()


def pig_latin(event):
    word = e.get()
    if e.get() == '':
        return
    else:
        first_letter = word[0].lower()
        rest_of_word = word[1:]
        if first_letter in ['a', 'e', 'i', 'o', 'u']:
            print(f"{word}way")
        else:
            print(f"{rest_of_word}{first_letter}ay")


# Create and display entry field
e = Entry(root, width=50, borderwidth=5)
e.pack()
e.bind('<Return>', pig_latin)

root.mainloop()
