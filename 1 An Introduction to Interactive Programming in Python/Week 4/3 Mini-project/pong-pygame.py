import pygame as pg
from pygame.sprite import Sprite
from random import choice

pg.init()

# Create constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 1080
HEIGHT = 720

# Initialize scoring variables
score_1 = 0
score_2 = 0

# Create game window
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pong")

# Create font object
font = pg.font.Font('freesansbold.ttf', 100)

# Clock for limiting game to 60 FPS
clock = pg.time.Clock()


class Paddle(Sprite):
    ''' Class represents a paddle as a subclass of Sprite'''

    def __init__(self):
        # Initialize sprite superclass and paddle attributes
        super().__init__()
        self.width = 15
        self.height = 145
        self.color = WHITE
        self.velocity = 5

        # Create paddle image
        self.image = pg.Surface([self.width, self.height])
        self.image.fill(self.color)

        # Create paddle rectangle
        pg.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        self.rect = self.image.get_rect()

    def moveUp(self):
        '''Move the paddle up'''
        if self.rect.y <= 0:
            pass
        else:
            self.rect.y -= self.velocity

    def moveDown(self):
        '''Move the paddle down'''
        if self.rect.y >= HEIGHT - self.height:
            pass
        else:
            self.rect.y += self.velocity


class Ball(Sprite):
    '''Class represents ball as a subclass of Sprite'''

    def __init__(self):
        # Initialize sprite superclass and ball attributes
        super().__init__()
        self.width = 50
        self.height = 50
        self.color = WHITE
        self.velocity = [choice([-3, -4, 3, 4]), -1]

        # Create ball image
        self.image = pg.Surface([self.width, self.height], pg.SRCALPHA)

        # Create ball rectangle
        pg.draw.circle(self.image, self.color, [
                       self.width // 2, self.height // 2], self.width // 2)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - self.width // 2
        self.rect.y = HEIGHT // 2 - self.height // 2

    def update(self):
        '''Update the ball position'''
        self.rect.x += int(self.velocity[0])
        self.rect.y += int(self.velocity[1])

    def bounce(self):
        '''Bounce off paddle'''
        self.velocity[0] = -self.velocity[0]

    def reset(self):
        global sprites, ball
        sprites.remove(self)
        ball = Ball()
        sprites.add(ball)


# Create and position, left paddle, right paddle, and ball
paddle_l = Paddle()
paddle_l.rect.x = 0
paddle_l.rect.y = (HEIGHT // 2 - paddle_l.height // 2)

paddle_r = Paddle()
paddle_r.rect.x = WIDTH - paddle_r.width
paddle_r.rect.y = (HEIGHT // 2 - paddle_r.height // 2)

ball = Ball()

# Add paddles and ball to sprite group
sprites = pg.sprite.Group()
sprites.add(paddle_l)
sprites.add(paddle_r)
sprites.add(ball)

# Main game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                pg.quit()
                quit()

    # Move the paddles in response to key presses
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        paddle_l.moveUp()
    if keys[pg.K_s]:
        paddle_l.moveDown()
    if keys[pg.K_UP]:
        paddle_r.moveUp()
    if keys[pg.K_DOWN]:
        paddle_r.moveDown()

    # Handle ball collisions with the walls
    if ball.rect.y >= HEIGHT - ball.height:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y <= 0 + ball.height:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.x >= WIDTH - ball.width:
        score_1 += 1
        ball.reset()
    if ball.rect.x <= 0:
        score_2 += 1
        ball.reset()

    # Handle ball collisions with the paddles
    if paddle_l.rect.colliderect(ball.rect):
        ball.velocity[0] = -ball.velocity[0]
        # This line is to ensure the ball doesn't get stuck in the paddle
        ball.rect.left = paddle_l.rect.right
    if paddle_r.rect.colliderect(ball.rect):
        ball.velocity[0] = -ball.velocity[0]
        ball.rect.right = paddle_r.rect.left

    # Update sprites
    sprites.update()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the center line and sprites
    pg.draw.line(screen, WHITE, [WIDTH // 2 - 2, 0],
                 [WIDTH // 2 - 2, HEIGHT], 4)
    sprites.draw(screen)

    # Draw the scores
    score_a = font.render(f"{score_1}", True, WHITE)
    score_b = font.render(f"{score_2}", True, WHITE)
    screen.blit(score_a, [100, 0])
    screen.blit(score_b, [WIDTH - 150, 0])

    # Update the screen
    pg.display.flip()

    # Speed up the ball as time goes on
    if ball.velocity[0] > 0:
        ball.velocity[0] += 0.01
    else:
        ball.velocity[0] -= 0.01
    if ball.velocity[1] > 0:
        ball.velocity[1] += 0.01
    else:
        ball.velocity[1] -= 0.01

    # Limit to 60 FPS
    clock.tick(60)
