import pygame
from writte import write
from map import lvl_end

class Gate(pygame.sprite.Sprite):
    def __init__(self, pos, surfase):
        super().__init__()
        self.image = pygame.image.load(f'assets/textures/gate.png')
        self.rect = self.image.get_rect(topleft=pos)

        self.player_near = False
        self.screen = surfase

    def open_door(self, is_key):
        keys = pygame.key.get_pressed()

        if not keys[pygame.K_e] and self.player_near:
            write('open E', self.rect.y, self.rect.x, self.screen)
        if keys[pygame.K_e] and self.player_near:
            if is_key:
                pygame.event.post(lvl_end)
            else:
                write('need a key', self.rect.y, self.rect.x, self.screen)

    def update(self, x_shift):
        self.rect.x += x_shift
