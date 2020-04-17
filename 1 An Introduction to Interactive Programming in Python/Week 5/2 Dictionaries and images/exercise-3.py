##
# Load image of astroid, and draw the image centered at the last mouse click.
#
import pygame as pg

pg.init()

# Initialize constants
WIDTH = 500
HEIGHT = 500
BLACK = (0, 0, 0)

# Create screen, asteroid image, and center asteroid on screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
image = pg.image.load('asteroid.png')
x_pos = (WIDTH - image.get_rect().width) / 2
y_pos = (HEIGHT - image.get_rect().height) / 2
screen.blit(image, (x_pos, y_pos))

while True:
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        # If mouse is clicked, redraw asteroid centered at mouse click position
        if event.type == pg.MOUSEBUTTONDOWN:
            screen.fill(BLACK)
            pos = pg.mouse.get_pos()
            x_pos = pos[0] - image.get_rect().width / 2
            y_pos = pos[1] - image.get_rect().height / 2
            screen.blit(image, (x_pos, y_pos))
