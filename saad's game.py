import pygame
pygame.init()

''' setting up variabels '''
# Screen dimensions
screen_width = 640
screen_height = 480

# Paddle dimensions
paddle_width = 15
paddle_height = 100

# Ball dimensions
ball_size = 20

# Colors
white = (255, 255, 255)

"game window"

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")

'games loop'
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    # Update the screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()


