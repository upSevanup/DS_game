import pygame
from writte import write
class Home(pygame.sprite.Sprite):
    def __init__(self, pos, surface, is_key=False):
        super().__init__()
        self.image = pygame.image.load(f'assets/textures/house.png')
        self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - 100))

        self.is_key = is_key
        self.player_near = False
        self.pos = pos
        self.screen = surface

    def get_input(self):
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_e] and self.player_near:
            write('search E', self.rect.y + 70, self.rect.x + 60, self.screen)
        if keys[pygame.K_e] and self.player_near:
            if self.is_key:
                write('key found', self.rect.y + 70, self.rect.x + 60, self.screen)
                return True
            else:
                write('empty', self.rect.y + 70, self.rect.x + 60, self.screen)

    def update(self, x_shift):
        self.rect.x += x_shift
