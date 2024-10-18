import pygame
import AnimationTestSprite

from config import *

pygame.init()

# Fenster zum Zeichnen einrichten
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
test_sprite = AnimationTestSprite.AnimationTestSprite()

# Liste der gedrückten Tasten
gedrueckte_tasten = []

# Läuft, bis der Benutzer das Programm beendet
running = True
clock = pygame.time.Clock()

def movement(tasten):
    for taste in tasten:
        if taste == pygame.K_LEFT:
            test_sprite.bewege('links', delta_time)
        elif taste == pygame.K_RIGHT:
            test_sprite.bewege('rechts', delta_time)
        elif taste == pygame.K_UP:
            test_sprite.bewege('oben', delta_time)
        elif taste == pygame.K_DOWN:
            test_sprite.bewege('unten', delta_time)


while running:
    delta_time = clock.tick(120) / 1000.0  # Delta-Zeit in Sekunden

    # Ereignisse verarbeiten
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key not in gedrueckte_tasten:
                gedrueckte_tasten.append(event.key)
        elif event.type == pygame.KEYUP:
            if event.key in gedrueckte_tasten:
                gedrueckte_tasten.remove(event.key)

    # Gedrückte Tasten verarbeiten
    movement(gedrueckte_tasten)

    # Sprite-Animation aktualisieren
    test_sprite.update(delta_time)

    # Hintergrund mit einer Farbe füllen
    screen.fill((50, 50, 50))

    # Sprite zeichnen
    test_sprite.draw(screen)

    # Anzeige aktualisieren
    pygame.display.flip()

pygame.quit()
