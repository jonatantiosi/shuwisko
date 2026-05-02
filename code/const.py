"""const.py"""
# import random

import pygame

# C
COLOR_BEIGE = (107, 90, 89)
COLOR_WHITE = (255, 255, 255)
COLOR_CRIMSON = (220, 20, 60)

# E
ENEMY_SPAWN_TIME = 3000
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'level_1_background_0': 1, # stars
    'level_1_background_1': 0, # moon
    'level_1_background_2': 2, # trees
    'player_frame_0': 3,
    'enemy_1': (2, 2),
}
ENTITY_HEALTH = {
    'level_1_background_0': 999,
    'level_1_background_1': 999,
    'level_1_background_2': 999,
    'player_frame_0': 1,
    'enemy_1': 999,
}
ENTITY_DAMAGE = {
    'level_1_background_0': 0,
    'level_1_background_1': 0,
    'level_1_background_2': 0,
    'player_frame_0': 0,
    'enemy_1': 999,
}


# M
MENU_OPTIONS = (
    'NEW GAME', # 0
    'EXIT', # 1
)

# W
WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324