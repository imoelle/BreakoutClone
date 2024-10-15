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

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

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
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()
