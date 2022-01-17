import pygame

def load_level(filename):
    with open(filename, 'r') as mapFile:
        map = [line.strip() for line in mapFile]
    return list(map)

tile_size = 80
size_width = 1600
size_height = 960

# события
LVL_COMPITED = pygame.USEREVENT
lvl_comp = pygame.event.Event(LVL_COMPITED)

PLAYER_DEAD = pygame.USEREVENT
pl_d = pygame.event.Event(PLAYER_DEAD)