"""enemy.py"""

import random

from code.const import ENTITY_SPEED
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name:str, position: tuple):
        super().__init__(name, position)
        # usado caso quiser randomizar a velocidade dos pingos de chuva com tupla
        min_speed, max_speed = ENTITY_SPEED[self.name]
        self.speed = random.randint(min_speed, max_speed)

    def move(self):
        self.rect.centery += self.speed
        self.rect.centerx -= 1