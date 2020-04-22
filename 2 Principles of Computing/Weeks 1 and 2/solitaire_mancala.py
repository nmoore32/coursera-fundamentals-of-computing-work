"""
Solitaire version of Mancala

Goal: Move all the seeds from each house into the store.

You must move all the seeds in a given house at the same time. Put the first seed in the house
on the right then the second seed in the second house on the right, and so on. The last seed
MUST go in the storehouse as a result of following this placement method.

Click on a house to move the seeds for that house.
"""
from random import choice, randint
import sys

import pygame as pg

WIDTH = 975
HEIGHT = 300
LEFT_MARGIN = 50
TOP_MARGIN = 75
FONT_SIZE = 64
HOUSE_SIZE = (125, 200)

BLACK = (0, 0, 0)  # Text and outline color
GRAY = (128, 128, 128)  # Background color


class SolitaireMancala:
    """
    Class that implements Solitaire Mancala
    """

    def __init__(self):
        """
        Create empty Mancala game board
        """
        self._board = []

    def set_board(self, configuration):
        """
        Sets the board state to given configuration
        house zero corresponds to the store and is on right
        houses are labeled in ascending order, house one is nearest to store
        """
        self._board = list(configuration)

    def __str__(self):
        """
        Return string representation of Mancala board
        """
        # The board is in the reverse order of the list
        temp = list(self._board)
        temp.reverse()
        return str(temp)

    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        if sum(self._board[1:]) != 0 or self._board == []:
            return False
        return True

    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        house_in_range = 0 < house_num < len(self._board)
        index_matches_value = self._board[house_num] == house_num
        return house_in_range and index_matches_value

    def apply_move(self, house_num):
        """
        Move all of the seeds from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            self._board[house_num] = 0
            for i in range(house_num):
                self._board[i] += 1

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for house_num in range(1, len(self._board)):
            if self.is_legal_move(house_num):
                return house_num
        return 0

    def generate_legal_configuration(self):
        """
        Generates and returns a legal board configuration
        """
        # As long as the current board state is not a winning state
        while not self.is_game_won():
            config = [0]
            # Generate a random configuration with enough seeds to be non-trivial
            # For a move from a given house to be legal the number of seeds on
            # that house must be equal to its number, hence the upper limits
            while sum(config) < 5:
                config = [0, randint(0, 1), randint(0, 2),
                          randint(0, 3), choice([0, 2, 3, 4]), choice([0, 4, 5]), choice([0, 6])]
            self.set_board(config)
            # Check to see if the selected configuration is winnable
            next_move = self.choose_move()
            while next_move != 0:
                self.apply_move(next_move)
                next_move = self.choose_move()
        # Return winnable configuration
        return config


def start_game(board):
    """
    Sets up the board
    """
    board.set_board([])
    config = board.generate_legal_configuration()
    board.set_board(config)


def draw_board(board, houses, font, screen):
    """
    Draws the current game board state
    """
    # Draw the houses, store, and number of seeds in each
    screen.fill(GRAY)
    for house_num, rect in enumerate(houses):
        pg.draw.rect(screen, BLACK, rect, 1)
        txt = font.render(str(board.get_num_seeds(house_num)), True, BLACK)
        txt_rect = txt.get_rect()
        txt_rect.center = rect.center
        screen.blit(txt, txt_rect)
    pg.display.flip()


def display_outcome(result, font, screen):
    """
    Displays the outcome of the game for 5 seconds
    """
    outcome = font.render(result, True, BLACK)
    outcome_rect = outcome.get_rect()
    outcome_rect.center = (WIDTH // 2, FONT_SIZE // 2)
    screen.blit(outcome, outcome_rect)
    pg.display.flip()
    pg.time.wait(5000)


def main():
    """
    Runs the program
    """
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    font = pg.font.SysFont(None, FONT_SIZE)

    # Create and set up the board
    board = SolitaireMancala()
    start_game(board)

    # Create rect objects associated with each of the six houses and the store
    houses = []
    for house_num in range(7):
        rect = pg.Rect(
            LEFT_MARGIN + house_num * HOUSE_SIZE[0], TOP_MARGIN, HOUSE_SIZE[0], HOUSE_SIZE[1])
        houses.append(rect)
    # Reverse the list of houses so that the house number matches its index number
    houses.reverse()

    while True:
        # Draw the board
        draw_board(board, houses, font, screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                # If one of the houses is clicked on, perform move from that house if legal
                for house_num in range(1, len(houses)):
                    if houses[house_num].collidepoint(mouse_pos):
                        board.apply_move(house_num)

        # If the game is won, display a "You won!" message for 5 seconds before starting new game
        if board.is_game_won():
            draw_board(board, houses, font, screen)
            display_outcome('You won!', font, screen)
            start_game(board)

        # If the game is lost, display a 'You lost" message for 5 seconds before starting new game
        if not board.choose_move():
            draw_board(board, houses, font, screen)
            display_outcome('You lost', font, screen)
            start_game(board)


if __name__ == '__main__':
    main()
