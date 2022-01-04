import pygame
from gg import Tile
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

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.x
        direction_x = player.direction.x

        if player_x < size_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > size_width - (size_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()
