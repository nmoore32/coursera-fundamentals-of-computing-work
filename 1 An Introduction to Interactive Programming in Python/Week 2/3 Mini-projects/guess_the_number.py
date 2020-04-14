from random import randrange
from tkinter import Button, END, Entry, Label, StringVar, Tk

root = Tk()

# Define global variables to keep track of various quantities
secret_number = None
guesses = 7
guesses_remaining = guesses
# Upper limit for random number generation
upper_limit = 100
# Variables to update response to display and remaining guesses
response = StringVar()
remaining = StringVar()

# Define functions


def validate(inp):
    '''Ensures the input is valid'''
    return inp.isdigit()


def new_game():
    '''Start a new game'''
    global response
    global secret_number
    global guesses_remaining
    # Pick new secret number, reset number of guesses, and indicate new game start
    secret_number = randrange(0, upper_limit)
    guesses_remaining = guesses
    response.set('New Game!')


def range100():
    '''Reset game with range [0, 100)'''
    global upper_limit
    global guesses
    # Set the upper range for the secret number to 100 and set number of guesses
    upper_limit = 100
    guesses = 7
    new_game()


def range1000():
    '''Reset game with range [0, 1000)'''
    global upper_limit
    global guesses
    # Set the upper range for the secret number to 1000 and set number of guesses
    upper_limit = 1000
    guesses = 9
    new_game()


def input_guess(event):
    '''Print appropriate response to guess and decrements guesses remaining'''
    global response
    global remaining
    global guesses_remaining
    # Decrement the guesses remaining
    guesses_remaining -= 1
    # Convert the current guess into an integer and clear the input field
    guess = int(e.get())
    e.delete(0, END)

    # Display appropriate responses if the guess was incorrect
    if guess != secret_number:
        if guess < secret_number:
            response.set(f"Guess was {guess}: Higher")
        elif guess > secret_number:
            response.set(f"Guess was {guess}: Lower")
        if guesses_remaining == 0:
            # Start a new game after a game over
            remaining.set('Game Over!')
            new_game()
        else:
            remaining.set(f"Guesses remaining: {guesses_remaining}")
    # Display the appropriate response if the guess was correct and start new game
    else:
        remaining.set(f"Guess was {guess}: Correct!")
        new_game()


# Create and display entry field
e = Entry(root, width=50, borderwidth=5)
reg = root.register(validate)
e.bind('<Return>', input_guess)
e.configure(validate='key', vcmd=(reg, '%P'))
e.grid(row=0, column=0, columnspan=2, pady=10)

# Create and display buttons
restart_100 = Button(root, text='Range [0, 100)', command=range100)
restart_1000 = Button(root, text='Range [0, 1000)', command=range1000)
restart_100.grid(row=1, column=0)
restart_1000.grid(row=1, column=1)

# Create output labels
label_response = Label(root, textvariable=response)
label_remaining = Label(root, textvariable=remaining)
label_response.grid(row=2, column=0, columnspan=2, pady=10)
label_remaining.grid(row=3, column=0, columnspan=2)


new_game()
root.mainloop()
