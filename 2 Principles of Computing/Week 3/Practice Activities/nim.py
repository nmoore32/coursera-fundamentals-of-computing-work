"""
Implementation of Nim (21 version)

Player and computer each take turns removing 1 to 3 seeds from a starting heap of
21 seeds. Whoever removes the last seed wins
"""
from random import randrange

MAX_REMOVE = 3
TRIALS = 10000


def evaluate_moves(num_seeds):
    """
    Monte Carlo evaluation method to determine computers next move
    Comp reliably chooses optimal move when num_seeds is less than 10
    """
    # Keep track of the number of wins and the move associated
    # with the largest number of wins
    win_rates = []  # (This is just for printing out win rates for curiosity)
    max_wins = 0
    best_move = 0
    # Run simulations for each possible move
    for initial_move in range(1, MAX_REMOVE + 1):
        wins = 0
        for trial in range(TRIALS):
            # Keep track of the total number of seeds removed
            total = initial_move
            # Comp wins if first_move removes all seeds
            win = True
            while total < num_seeds:
                total += randrange(1, MAX_REMOVE + 1)
                # Player and comp alternate removing seeds
                win = not win
            if win:
                wins += 1
        win_rates.append(wins / TRIALS)  # (Used to print out win rates)
        if wins > max_wins:
            max_wins = wins
            best_move = initial_move
    print(win_rates)  # (Used to print out win rates)
    return best_move


def play_game(start_seeds):
    """
    Play game of Nim against bot that uses Monte Carlo simulation to determine moves
    """
    current_seeds = start_seeds
    print(f"Starting game with {current_seeds} seeds")
    while True:
        comp_move = evaluate_moves(current_seeds)
        current_seeds -= comp_move
        if current_seeds < 0:
            current_seeds = 0
        print(f"Computer chooses: {comp_move}, current seeds {current_seeds}")
        if current_seeds == 0:
            print("Computer wins")
            break

        player_move = int(input("Enter your move (1, 2, or 3): "))
        current_seeds -= player_move
        if current_seeds < 0:
            current_seeds = 0
        print(f"Player chooses: {player_move}, current seeds {current_seeds}")
        if current_seeds == 0:
            print("Player wins")
            break


play_game(21)
