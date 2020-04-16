##
# Change radius of white ball centered on canvas in response to up and down keypresses.
# pygame
#
from time import sleep
import pygame as pg

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RADIUS_INCREMENT = 1
radius = 20

# Initialize pygame
pg.init()

# Create window
screen = pg.display.set_mode((500, 500))

while True:
    # To get rid of the previously drawn circle you either have to draw over it (screen.fill) or
    # you need to create a new screen object each time by putting the screen assignment in the
    # while loop.
    screen.fill(BLACK)
    pg.draw.circle(screen, WHITE, (250, 250), radius)
    pg.display.update()
    # Use key.get_pressed() for key holding behavior
    keys = pg.key.get_pressed()
    if keys[pg.K_DOWN] and radius > RADIUS_INCREMENT:
        radius -= RADIUS_INCREMENT
    elif keys[pg.K_UP]:
        radius += RADIUS_INCREMENT

    # Pass/process any other events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        else:
            pass

    # Run loop at 60 FPS
    sleep(1 / 60)
