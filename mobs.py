import pygame
from frame_cut import cut_sheet

class Mob(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # анимация
        self.animations = {'Mb_walk': [], 'Mb_attack': []}
        self.mob_assets()
        self.frame_index = 0
        self.animation_speed = 0.15

        # mob
        self.image = self.animations['Mb_walk'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)

        # статус
        self.status = 'Mb_walk'
        self.is_right = True

        # движение
        self.speed = 3
        self.pos = pos
        self.dist = 0
        self.dir = 1

        # хп
        self.mob_hp = 100

    def udarmob(self):
        self.mob_hp -= 20

    def what_direction(self):
        self.dist += self.dir
        if self.dist >= 80:
            self.direction.x = -1
            self.dist = 0
            self.dir = -1
            self.is_right = False
        if self.dist <= -80:
            self.direction.x = 1
            self.dist = 0
            self.dir = 1
            self.is_right = True

    def mob_assets(self):
        for anim in self.animations.keys():

            # ДОДЕЛАТЬ КОГДА БУДЕТ АНИМАЦИЯ!!!!!!!!
            row = None
            col = None

            self.animations[anim] = cut_sheet(pygame.image.load(f'assets/mob/{anim}.png'), col, row)

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

    def get_status(self):
        if self.direction.x != 0:
            self.status = 'Mb_walk'
        else:
            self.status = 'Mb_attack'

    def update(self, x_shift):
        self.rect.x += x_shift
        self.what_direction()
        self.rect.x += self.direction.x * self.speed

        self.get_status()
        self.animate()





