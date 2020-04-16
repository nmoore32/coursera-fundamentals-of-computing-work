##
# Displays "Space bar down" on screen as long as space is held down, otherwise displays
# "Space bar up"
# pygame
#
import pygame as pg

BLUE = (0, 0, 128)
BLACK = (0, 0, 0)
RED = (128, 0, 0)
WIDTH = 500
HEIGHT = 500

# Initialize pygame
pg.init()

# Create window
screen = pg.display.set_mode((WIDTH, HEIGHT))

# Create font object
font = pg.font.Font('freesansbold.ttf', 32)

# Create a text surface object
# Arguments for render() are (text, antialias, color, background)
text_up = font.render('Space bar up', True, BLUE)
text_down = font.render('Space bar down', True, RED)
# Determine coordinates to center text_up
w = text_up.get_rect().width
h = text_up.get_rect().height
text_pos = (WIDTH / 2 - w / 2, HEIGHT / 2 - h / 2)
# Display text_up initially
screen.blit(text_up, text_pos)

while True:
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            # Clear screen before drawing new text
            screen.fill(BLACK)
            screen.blit(text_down, text_pos)
        elif event.type == pg.KEYUP and event.key == pg.K_SPACE:
            screen.fill(BLACK)
            screen.blit(text_up, text_pos)
        elif event.type == pg.QUIT:
            pg.quit()
            quit()
