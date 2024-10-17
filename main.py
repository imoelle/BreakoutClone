##### main.py #####################################################################################
# Some description of the main.py file
#
# Author: Ingo Möller
# Version: 1.0 (15.10.2024)
###################################################################################################
# History:
# 10.10.2024 Erstellen der Datei und einfügen des Pygame-Beispiels
#
#
###################################################################################################

import pygame

from config import *

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

    def update(self):
        self.rect.x += 1
        print(self.rect.left)
        if self.rect.left > WINDOW_WIDTH:
            self.rect.left = 50

    def draw(self, scr):
        screen.blit(self.image, self.rect)


pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
ball = Ball()

# Run until the user asks to quit
running = True

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    ball.draw(screen)
    ball.update()


    # Flip the display
    pygame.display.flip()

pygame.quit()