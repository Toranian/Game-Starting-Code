import os, sys, time, random
import pygame
from settings import *

# Game display: 6 | Title: 7 | Game Exit: 8 | Initialization: 9-10
# Lead X & Y |
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption(TITLE)
init = pygame.init()
print("{} Successes, {} Failures".format(init[0], init[1]))


# Game loop
class GameLoop:

    def __init__(self):
        self.game_exit = False

        self.square_x = WIDTH / 2
        self.square_y = HEIGHT / 2

        self.speed = 4

        self.cube_size = 20
        self.cube = pygame.Rect(self.square_x, self.square_y, self.cube_size, self.cube_size)

        self.square_x_change = 0
        self.square_y_change = 0

        self.clock = pygame.time.Clock()

        pygame.display.set_caption(TITLE)

    def main_loop(self):
        while not self.game_exit:
            # Event handler | Quit: 16 |
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_exit = True

                # Key events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.square_x_change = -self.speed
                        self.square_y_change = 0
                    elif event.key == pygame.K_d:
                        self.square_x_change = self.speed
                        self.square_y_change = 0
                    elif event.key == pygame.K_w:
                        self.square_y_change = -self.speed
                        self.square_x_change = 0
                    elif event.key == pygame.K_s:
                        self.square_y_change = self.speed
                        self.square_x_change = 0

            # Border detections
            if self.square_x >= WIDTH:
                self.square_x = 0
            elif self.square_x == 0:
                self.square_x = WIDTH

            if self.square_y >= HEIGHT:
                self.square_y = 0
            elif self.square_y == 0:
                self.square_y = HEIGHT

            self.square_x += self.square_x_change
            self.square_y += self.square_y_change
            gameDisplay.fill(WHITE)
            pygame.draw.rect(gameDisplay, BLACK, [self.square_x, self.square_y, 10, 10])
            pygame.display.update()

            self.clock.tick(FPS)

    pygame.quit()
    quit()

GameLoop().main_loop()

# Isaac is a nerd

