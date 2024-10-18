import pygame

def konvertiere_sprite_sheet(sprite_sheet):
    x_num = 5
    y_num = 3
    frames = []
    for y in range(y_num):
        for x in range(x_num):
            frames.append(sprite_sheet.subsurface(x * 100, y * 100, 100, 100))
    return frames

class AnimationTestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite_sheet = pygame.image.load('test_spritesheet.png').convert_alpha()
        self.sprite_animation = konvertiere_sprite_sheet(self.sprite_sheet)
        self.aktuelles_frame = 0
        self.letztes_update = pygame.time.get_ticks()
        self.frame_rate = 150  # Millisekunden pro Frame
        self.position = pygame.Vector2(100, 100)
        self.geschwindigkeit = 300  # Pixel pro Sekunde

    def update(self, delta_time):
        jetzt = pygame.time.get_ticks()
        if jetzt - self.letztes_update > self.frame_rate:
            self.letztes_update = jetzt
            self.aktuelles_frame = (self.aktuelles_frame + 1) % len(self.sprite_animation)

    def bewege(self, richtung, delta_time):
        bewegung = self.geschwindigkeit * delta_time
        if richtung == 'links':
            self.position.x -= bewegung
        elif richtung == 'rechts':
            self.position.x += bewegung
        elif richtung == 'oben':
            self.position.y -= bewegung
        elif richtung == 'unten':
            self.position.y += bewegung

    def draw(self, ziel_bildschirm):
        ziel_bildschirm.blit(self.sprite_animation[self.aktuelles_frame], self.position)
