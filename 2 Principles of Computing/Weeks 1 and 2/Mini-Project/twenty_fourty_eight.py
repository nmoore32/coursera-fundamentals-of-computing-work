"""
Clone of 2048 game.
"""
from random import randint
import sys

import pygame as pg

# Layout related constants
WIDTH = 600
HEIGHT = 600
MARGIN = 85
GRID_HEIGHT = 4
GRID_WIDTH = 4
GAP = 10
TILE_SIZE = 100
# Associates tile values with the tile position in image file (indexed from 0)
# This makes it easy to use for loops to draw all the tiles
TILE_NUMBERS = {0: 0, 2: 1, 4: 2, 8: 3, 16: 4, 32: 5,
                64: 6, 128:  7, 256: 8, 512: 9, 1024: 10, 2048: 11}

# Display related constants
BACKGROUND = (187, 173, 160)
BLACK = (0, 0, 0)
FPS = 30
FONT_SIZE = 42

# Directions
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    @param line - a list of values for a line of tiles on the board
    @return - returns a list representing the merged line
    """
    # Slide all the tiles (non-zero elements) to the front by removing zeros
    # E.g. [2, 0, 2, 4] becomes [2, 2, 4]
    result_list = []
    for num in line:
        if num != 0:
            result_list.append(num)

    # Merge pairs of matching values in result_list
    # E.g. [2, 2, 4] becomes [4, 0, 4]
    for tile in range(len(result_list)):
        # Don't do anything if the given list is empty or has only one element
        if len(result_list) <= 1:
            break
        # If we find a matching pair of tiles, merge them and replace the second tile with 0
        if result_list[tile] == result_list[tile + 1]:
            result_list[tile] *= 2
            result_list[tile + 1] = 0
        # Stop one index before the end of the list
        if tile == len(result_list) - 2:
            break

    # Slide all the tiles to the front by removing zeros (empty spaces)
    # E.g. [4, 0, 4] becomes [4, 4]
    while 0 in result_list:
        result_list.remove(0)

    # Return result_list to original line length by adding 0s
    # E.g. [4, 4] becomes [4, 4, 0, 0] since the original example list had 4 elements
    while len(result_list) < len(line):
        result_list.append(0)

    return result_list


def create_merge_line(pos, direction, game_board):
    """
    Helper functions that determines the tile values along the merge line
    for a given direction in 2048
    @param pos - a tuple specifying the location of a tile in the grid
    @param direction - the direction to move along the board from pos
    @return line - a list representing the line of tiles to be merged
    """
    # For each initial position, move through the board in the specified
    # direction to determine the line of tiles to merge
    line = []
    # For non-square grids, the range to loop over will differ
    # between up/down and left/right
    if direction < LEFT:
        for idx in range(GRID_HEIGHT):
            row = pos[0] + idx * OFFSETS[direction][0]
            col = pos[1] + idx * OFFSETS[direction][1]
            line.append(game_board.get_tile(row, col))
    else:
        for idx in range(GRID_WIDTH):
            row = pos[0] + idx * OFFSETS[direction][0]
            col = pos[1] + idx * OFFSETS[direction][1]
            line.append(game_board.get_tile(row, col))
    return line


def calculate_indices():
    """
    Helper function that determines the indices for the first tile
    of each line to be merged in a given direction
    @ return initial_indices - a dictionary containing grid positions
    """
    dir_dict = {}
    # Create dictionaries of the iteration values needed for each direction
    dir_dict[UP] = (GRID_WIDTH, 0, UP)
    dir_dict[DOWN] = (GRID_WIDTH, GRID_HEIGHT - 1, DOWN)
    dir_dict[LEFT] = (GRID_HEIGHT, 0, LEFT)
    dir_dict[RIGHT] = (GRID_HEIGHT, GRID_WIDTH - 1, RIGHT)
    # Loop over each key, using the iteration values to calculate indices for that direction
    initial_indices = {}
    for key, value in dir_dict.items():
        dir_list = []
        for idx in range(value[0]):
            if key < 3:
                dir_list.append((value[1], idx))
            else:
                dir_list.append((idx, value[1]))
        initial_indices[value[2]] = dir_list
    return initial_indices


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid = []
        self._grid_height = grid_height
        self._grid_width = grid_width

        # Create a grid with two tiles set
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._grid_width)]
                      for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def get_grid(self):
        """
        Get a copy of the board grid.
        """
        return list(self._grid)

    def move(self, direction, indices_dict):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        @param direction - the direction to move
        @param indices_dict - dictionary specifying the initial tile
        positions associated with each movement direction
        """
        # Keep track of whether the board state changed
        board_change = False

        # Create the list of tiles values to pass to the merge function
        for pos in indices_dict[direction]:
            line = create_merge_line(pos, direction, self)

            # Create the merged list
            new_list = merge(line)

            # Change the board to reflect the merge
            # For rectangular boards, idx will range over different values
            if direction < LEFT:
                for idx in range(self._grid_height):
                    row = pos[0] + idx * OFFSETS[direction][0]
                    col = pos[1] + idx * OFFSETS[direction][1]
                    if self._grid[row][col] != new_list[idx]:
                        board_change = True
                    self._grid[row][col] = new_list[idx]
            else:
                for idx in range(self._grid_width):
                    row = pos[0] + idx * OFFSETS[direction][0]
                    col = pos[1] + idx * OFFSETS[direction][1]
                    if self._grid[row][col] != new_list[idx]:
                        board_change = True
                    self._grid[row][col] = new_list[idx]

        # Add a new tile if the board state changed
        if board_change:
            board_change = False
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # Do nothing if there are no empty squares
        if not any(0 in row for row in self._grid):
            return
        # Find a random empty square
        row = randint(0, self._grid_height - 1)
        col = randint(0, self._grid_width - 1)
        while self._grid[row][col] != 0:
            row = randint(0, self._grid_height - 1)
            col = randint(0, self._grid_width - 1)
        # Determine value of new tile
        prob = randint(1, 10)
        if prob == 10:
            value = 4
        else:
            value = 2
        # Set the tile in the grid
        self.set_tile(row, col, value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


def draw(screen, board, images, outcome, font):
    """
    Draws everything to the screen
    @param images - a tuple containing all of the game images
    @param outcome - string with outcome text to display
    """
    screen.fill(BACKGROUND)
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            value = board.get_tile(row, col)
            # Set the position to draw the tile
            pos_x = MARGIN + col * (TILE_SIZE + GAP)
            pos_y = MARGIN + row * (TILE_SIZE + GAP)
            # Specify left and top position of the tile in the tiled image
            tile_left = TILE_NUMBERS[value] * TILE_SIZE
            tile_top = 0
            # Draw the tile to the screen
            screen.blit(images[0], (pos_x, pos_y),
                        (tile_left, tile_top, TILE_SIZE, TILE_SIZE))

    # Draw new game button
    button_rect = images[1].get_rect()
    pos_x = (WIDTH - button_rect.width) // 2
    pos_y = HEIGHT - GAP - button_rect.height
    screen.blit(images[1], (pos_x, pos_y))

    # Draw outcome text if any
    outcome_text = font.render(outcome, True, BLACK)
    screen.blit(
        outcome_text, ((WIDTH - outcome_text.get_rect().width) // 2, GAP))


def check_end_game(board, indices_dict):
    """
    Check if the game is over and display appropriate message
    @ return outcome - string stating outcome
    """
    outcome = ''
    grid = board.get_grid()
    if any(2048 in row for row in grid):
        outcome = 'You won!'
    elif not any(0 in row for row in grid):
        # Determine if the game is lost by checking if any merges
        # would change the board state
        board_change = False
        for direction in indices_dict:
            for pos in indices_dict[direction]:
                line = create_merge_line(pos, direction, board)
                new_list = merge(line)
                if line != new_list:
                    board_change = True
        if not board_change:
            outcome = 'You lost'
    return outcome


def main():
    """
    Runs the program
    """
    pg.init()
    # Initialize screen, clock, game board, and assets
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    game_board = TwentyFortyEight(GRID_HEIGHT, GRID_WIDTH)
    tile_images = pg.image.load('tiles.png')
    # Buttom image created by Cayden Franklin and obtained from opengameart.org
    # License CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
    button_image = pg.image.load('new_game.png')

    # Set rect object for new game button
    button_rect = button_image.get_rect()
    button_rect.centerx = WIDTH // 2
    button_rect.centery = HEIGHT - -GAP - button_rect.height

    # Calculate indices for the initial tiles in each row or column
    # from which to start a move in a given direction
    initial_indices = calculate_indices()

    # Create variable to determine whether game is in play
    in_play = True

    # Create font for displaying outcome and variable for outcome text
    font = pg.font.Font('freesansbold.ttf', FONT_SIZE)
    outcome = ''

    while True:
        draw(screen, game_board, (tile_images, button_image), outcome, font)
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and in_play:
                if event.key == pg.K_UP:
                    game_board.move(UP, initial_indices)
                elif event.key == pg.K_DOWN:
                    game_board.move(DOWN, initial_indices)
                elif event.key == pg.K_LEFT:
                    game_board.move(LEFT, initial_indices)
                elif event.key == pg.K_RIGHT:
                    game_board.move(RIGHT, initial_indices)
            elif event.type == pg.MOUSEBUTTONDOWN:
                coords = event.pos
                if button_rect.collidepoint(coords):
                    game_board.reset()
                    in_play = True
                    outcome = ''

        outcome = check_end_game(game_board, initial_indices)
        if outcome:
            in_play = False

        clock.tick(FPS)


if __name__ == '__main__':
    main()
