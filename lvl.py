import pygame
from tiles import Tile
from map import tile_size, size_width
from Player import Player

class Lvl:
    def __init__(self, lvl_data, surface):

        # Создание уровня
        self.display_surface = surface
        self.setup_lvl(lvl_data)
        self.world_shift = 0

    def setup_lvl(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def horiz_move_coll(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vert_move_coll(self):
        player = self.player.sprite
        player.world_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.is_jump = True


    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.x
        direction_x = player.direction.x

        if player_x < size_width / 4 and direction_x < 0:
            if player.is_run:
                self.world_shift = 8
            else:
                self.world_shift = 4
            player.speed = 0
        elif player_x > size_width - (size_width / 4) and direction_x > 0:
            if player.is_run:
                self.world_shift = -8
            else:
                self.world_shift = -4
            player.speed = 0
        else:
            self.world_shift = 0
            if player.is_run:
                player.speed = 8
            else:
                player.speed = 4

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        self.player.update()
        self.player.draw(self.display_surface)
        self.vert_move_coll()
        self.horiz_move_coll()
