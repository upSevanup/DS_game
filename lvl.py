import pygame
from tiles import Tile
from map import tile_size, size_width
from Player import Player
from mobs import Mob
from inter import Game
from ui import UI
from loot_home import Home


class Lvl:
    def __init__(self, lvl_data, surface):

        # Создание уровня
        self.display_surface = surface
        self.setup_lvl(lvl_data)
        self.world_shift = 0
        self.hp = Game(self.display_surface)
        self.ui = UI(self.display_surface)

    def setup_lvl(self, layout):
        self.all_sprites = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.mob = pygame.sprite.Group()
        self.houses = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x, y), 'earth.png')
                    self.tiles.add(tile)
                    self.all_sprites.add(tile)
                if cell == 'Z':
                    tile = Tile((x, y), 'wall.png')
                    self.tiles.add(tile)
                    self.all_sprites.add(tile)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                if cell == 'M':
                    mob_sprite = Mob((x, y))
                    self.mob.add(mob_sprite)
                    self.all_sprites.add(mob_sprite)
                if cell == 'H':
                    house_sprite = Home((x, y), self.display_surface)
                    self.houses.add(house_sprite)
                    self.all_sprites.add(house_sprite)
                if cell == 'h':
                    house_sprite = Home((x, y), self.display_surface, is_key=True)
                    self.houses.add(house_sprite)
                    self.all_sprites.add(house_sprite)

    def horiz_move_coll(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.all_sprites.sprites():
            if self.tiles.has(sprite):
                if sprite.rect.colliderect(player.rect):
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left
            if self.mob.has(sprite):
                if sprite.rect.colliderect(player.rect):
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                        self.hp.change_hp()
                        print(self.hp.cur_hp)
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left
                        self.hp.change_hp()
            if self.houses.has(sprite):
                if sprite.rect.colliderect(player.rect):
                    sprite.player_near = True
                    have_key = sprite.get_input()
                    if have_key:
                        player.key = True
                else:
                    sprite.player_near = False

    def vert_move_coll(self):
        player = self.player.sprite
        player.world_gravity()

        for sprite in self.all_sprites.sprites():
            if self.tiles.has(sprite):
                if sprite.rect.colliderect(player.rect):
                    if player.direction.y < 0:
                        player.rect.top = sprite.rect.bottom
                        player.direction.y = 0
                    elif player.direction.y > 0:
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0
                        player.is_jump = True
            if self.mob.has(sprite):
                if player.direction.y < 0:
                    self.hp.change_hp()
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.is_jump = True
                    self.hp.change_hp()

    def udar_mob(self):
        player = self.player.sprite

        for sprite in self.mob.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    print(self.hp.cur_hp)
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left


    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.x
        direction_x = player.direction.x

        if player_x < size_width / 4 and direction_x < 0:
            if player.is_run:
                if self.hp.cur_st <= 100 and self.hp.cur_st > 0:
                    self.world_shift = 8
                    self.hp.regen_st = 0
                    self.hp.regen()
                else:
                    self.hp.regen_st = 0.4
                    self.world_shift = 4
            else:
                self.world_shift = 4
            player.speed = 0
        elif player_x > size_width - (size_width / 4) and direction_x > 0:
            if player.is_run:
                if self.hp.cur_st <= 100 and self.hp.cur_st > 0:
                    self.world_shift = -8
                    self.hp.regen_st = 0
                    self.hp.regen()
                else:
                    self.hp.regen_st = 0.4
                    self.world_shift = -4
            else:
                self.world_shift = -4
            player.speed = 0
        else:
            self.world_shift = 0
            if player.is_run:
                if self.hp.cur_st <= 100 and self.hp.cur_st > 0:
                    player.speed = 8
                    self.hp.regen()
                else:
                    player.speed = 4
            else:
                player.speed = 4
                self.hp.regen_st = 0.2

    def run(self):
        self.tiles.update(self.world_shift)
        self.houses.update(self.world_shift)
        self.mob.update(self.world_shift)
        self.all_sprites.draw(self.display_surface)
        self.scroll_x()

        self.player.update()
        self.player.draw(self.display_surface)
        self.vert_move_coll()
        self.horiz_move_coll()

        self.ui.show_heal(self.hp.cur_hp, self.hp.hp_max)
        self.ui.show_stam(self.hp.cur_st, self.hp.st_max)
        self.ui.show_soul(self.hp.souls)
        self.hp.run()

