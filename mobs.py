import pygame

class Mob(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((48, 80))
        self.image.fill('black')
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3
        self.pos = pos
        self.dist = 0
        self.dir = 1
        self.mob_hp = 100

    def udarmob(self):
        self.mob_hp -= 20

    def update(self, x_shift):
        self.rect.x += x_shift

        self.dist += self.dir
        if self.dist >= 80:
            self.direction.x = -1
            self.dist = 0
            self.dir = -1
        if self.dist <= -80:
            self.direction.x = 1
            self.dist = 0
            self.dir = 1

        self.rect.x += self.direction.x * self.speed
