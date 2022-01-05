import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((48, 80))
        self.image.fill('purple')
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)

        # movement
        self.is_run = False
        self.is_jump = False
        self.speed = 4
        self.gravity = 0.8
        self.jump_height = -16

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]:
            self.jump()

        if keys[pygame.K_LSHIFT]:
            self.is_run = True
        else:
            self.is_run = False

    def world_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        if self.is_jump:
            self.direction.y = self.jump_height
            self.is_jump = False

    def update(self):
        self.get_input()
