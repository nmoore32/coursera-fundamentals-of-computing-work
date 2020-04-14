import pygame

# Constants
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
WHITE = (255, 255, 255)

# Initialize pygame
pygame.init()


# Create a display surface
screen_width = 400
screen_height = 200
screen = pygame.display.set_mode([screen_width, screen_height])

# Set the pygame window name
pygame.display.set_caption('Show Text')

# Create a font object
font = pygame.font.Font('freesansbold.ttf', 32)

# Create a text surface object on which to draw text
# Paramters (text, antialiasing, color, background)
text = font.render('My first frame!', True, GREEN, BLUE)

# Create a rectangular object for the text surface object
textRect = text.get_rect()

# Set the center of the rectangular object.
textRect.center = (screen_width // 2, screen_height // 2)

# Infinite loop
while True:

    # Completely fill the surface object
    screen.fill(WHITE)

    # Copy the text surface object to the display surface object
    screen.blit(text, textRect)

    # Iterate over the list of Event objects
    for event in pygame.event.get():

        # If event object type is QUIT, then quit
        if event.type == pygame.QUIT:

            # Deactivate the pygame library
            pygame.quit()

            # quit the program
            quit()

    pygame.display.update()
