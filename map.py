import pygame

level_map = [
    '                                                                    ',
    '                                                               Z Z Z',
    '                                                               ZZZZZ',
    '                                                                ZZZZ',
    '                                                                ZOOZ',
    '                                                                ZZZZ',
    '                                                                ZOOZ',
    'Z                                                               ZZZZ',
    'Z                                                               ZOOZ',
    'Z                                                               ZZZZ',
    'Z  P      M         H   H    h      H                           UZZZ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

tile_size = 80
size_width = 1600
size_height = 960

# события
LVL_COMPITED = pygame.USEREVENT + 1
lvl_end = pygame.event.Event(LVL_COMPITED)
