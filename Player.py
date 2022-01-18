import pygame
from frame_cut import cut_sheet
from inter import Game


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # анимация
        self.animations = {'Idle': [], 'Run': [], 'Jump': [], 'Attack': []}
        self.character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15

        # игрок
        self.image = self.animations['Idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)

        # движение
        self.is_run = False
        self.is_jump = False
        self.speed = 4
        self.gravity = 0.8
        self.jump_height = -12

        # статус
        self.status = 'Idle'
        self.is_right = True
        self.is_attack = False

        # предметы
        self.key = False

        self.st = Game((1600, 960))

    # принятие кнопок + передвижение
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.is_right = True
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.is_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.jump()

        if keys[pygame.K_LSHIFT]:
            self.is_run = True
        else:
            self.is_run = False

        if keys[pygame.K_SPACE]:
            self.is_attack = True

    #анимация
    def character_assets(self):
        for anim in self.animations.keys():
            if anim != 'Attack':
                row = 4
                col = 2
            else:
                row = 1
                col = 8

            self.animations[anim] = cut_sheet(pygame.image.load(f'assets/character/{anim}.png'), col, row)

    # анимация
    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.is_right:
            self.image = image
        else:
            flip_img = pygame.transform.flip(image, True, False)
            self.image = flip_img

    # статус
    def get_status(self):
        if self.direction.y < 0:
            self.animation_speed = 0.01
            self.status = 'Jump'
        elif self.is_attack:
            self.animation_speed = 0.15
            self.status = 'Attack'
            self.is_attack = False
        else:
            self.animation_speed = 0.15
            if self.direction.x != 0:
                self.status = 'Run'
            else:
                self.status = 'Idle'

    # гравитация
    def world_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    # прыжок
    def jump(self):
        if self.is_jump:
            self.direction.y = self.jump_height
            self.is_jump = False

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()