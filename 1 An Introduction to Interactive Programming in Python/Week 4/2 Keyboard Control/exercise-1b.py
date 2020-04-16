##
# Print "Pressed up arrow" or "Pressed down arrow" to console when the appropriate key is pressed.
# Using pygame
#
import pygame as pg

pg.init()

# You need to create a window as pygame expects events to come from an active pygame window
screen = pg.display.set_mode((300, 300))

while True:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                print("Pressed down arrow")
            elif event.key == pg.K_UP:
                print("Pressed up arrow")
            elif event.key == pg.K_q:
                pg.quit()
                quit()
