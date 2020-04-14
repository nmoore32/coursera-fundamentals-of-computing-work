from random import randrange


def name_to_number(name):
    '''Converts a rpsls answer to a number'''
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4


def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'


def rpsls(player_choice):
    print()
    print(f"Player chooses {player_choice}")
    player_number = name_to_number(player_choice)

    comp_number = randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print(f"Computer chooses {comp_choice}")

    diff = comp_number - player_number
    if diff < 0:
        diff += 5

    if diff == 0:
        print("Tie!")
    elif diff < 3:
        print("Computer wins!")
    else:
        print("Player wins!")


rpsls('rock')
rpsls('paper')
rpsls('scissors')
rpsls('lizard')
rpsls('Spock')
