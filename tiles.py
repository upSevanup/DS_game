import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, texture):
        super().__init__()
        self.image = pygame.image.load(f'assets/textures/{texture}')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
