"""player.py"""

import pygame

from code.const import ENTITY_SPEED, WINDOW_HEIGHT, WINDOW_WIDTH
from code.entity import Entity


class Player(Entity):
    def __init__(self,name:str, position:tuple):
        super().__init__(name,position)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_w] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_s] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_a] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_d] and self.rect.right < WINDOW_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]