import os, sys, time
import pygame
from settings import *

# Game display: 6 | Title: 7 | Game Exit: 8 | Initialization: 9-10
# Lead X & Y |
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
gameExit = False
init = pygame.init()
print("{} Successes, {} Failures".format(init[0], init[1]))

square_x = WIDTH / 2
square_y = HEIGHT / 2

speed = 4

cube_size = 20
cube = pygame.Rect(square_x, square_y, cube_size, cube_size)

square_x_change = 0
square_y_change = 0

clock = pygame.time.Clock()

# Game loop
while not gameExit:
    # Event handler | Quit: 16 |
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        # Key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                square_x_change = -10
                square_y_change = 0
            elif event.key == pygame.K_d:
                square_x_change = 10
                square_y_change = 0
            elif event.key == pygame.K_w:
                square_y_change = -10
                square_x_change = 0
            elif event.key == pygame.K_s:
                square_y_change = 10
                square_x_change = 0

    # Border detections
    if square_x >= WIDTH:
        square_x = 0
    elif square_x == 0:
        square_x = WIDTH

    if square_y >= HEIGHT:
        square_y = 0
    elif square_y == 0:
        square_y = HEIGHT

    square_x += square_x_change
    square_y += square_y_change
    gameDisplay.fill(WHITE)
    pygame.draw.rect(gameDisplay, BLACK, [square_x, square_y, 10, 10])
    pygame.display.update()

    clock.tick(30)
    
pygame.quit()
quit()


#Isaac is a nerd

