"""entity_factory.py"""

from code.background import Background
from code.const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.enemy import Enemy
from code.player import Player
import random


class EntityFactory:
    @staticmethod
    def get_entity(entity_name:str, position=(0,0)):
        match entity_name:
            case 'level_1_background':
                background_list = []
                for i in range(3):
                    background_list.append(Background(f'level_1_background_{i}', position = (0,0)))
                    background_list.append(Background(f'level_1_background_{i}', position = (WINDOW_WIDTH,0)))
                return background_list
            case 'player_frame':
                return Player('player_frame_0', position=(10, WINDOW_HEIGHT/2))
            case 'enemy_1':
                return Enemy('enemy_1', (random.randint(0, WINDOW_WIDTH + 324), -10))
        return None