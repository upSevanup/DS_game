import pygame

class Mob(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((48, 80))
        self.image.fill('black')
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 4

    def update(self, x_shift):
        self.rect.x += x_shift

        while True:
            self.direction.x = 1
            if изночальное положение - 240 == положение сейчас:
                self.direction.x = 1
            if изночальное положение + 240 == положение сейчас:
                self.direction.x = -1






