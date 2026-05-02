"""entity.py"""

from abc import ABC, abstractmethod
import pygame

from code.const import ENTITY_HEALTH, ENTITY_DAMAGE


class Entity(ABC):
    def __init__(self, name:str, position: tuple):
        self.name = name
        self.position = position
        self.surface = pygame.image.load('./asset/' + self.name + '.png').convert_alpha()
        self.rect = self.surface.get_rect(left=self.position[0], top=self.position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]

    @abstractmethod
    def move(self):
            pass