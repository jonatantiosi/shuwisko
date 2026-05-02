"""level.py"""

import pygame
from pygame import Surface
import sys

from code.const import EVENT_ENEMY, ENEMY_SPAWN_TIME
from code.entity import Entity
from code.entity_factory import EntityFactory
from code.entity_mediator import EntityMediator
from code.player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode:str, player_score: int):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.player_score = player_score
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + '_background'))
        self.player = EntityFactory.get_entity('player_frame')
        self.entity_list.append(self.player)
        self.last_difficult_update = 0
        # SPAWN TIME BASE/INICIAL, vai aumentando no while do run
        self.spawn_time = ENEMY_SPAWN_TIME
        # legacy
        # pygame.time.set_timer(EVENT_ENEMY, ENEMY_SPAWN_TIME)
        self.start_time = pygame.time.get_ticks()

    def run(self, player_score: int):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60) # 60 fps
            # correção de erro personagem ficando atrás do bg
            self.window.fill((0,0,0))

            time = (pygame.time.get_ticks() - self.start_time) / 1000 # tempo em segundos
            if time - self.last_difficult_update > 2:
                # verifica se passaram 2 segundos desde a última atualização
                self.last_difficult_update = time # novo tempo de referência
                # 1 / (1 + k * tempo) curva de dificuldade conforme tempo
                self.spawn_time = int(ENEMY_SPAWN_TIME/ (1 + 0.3 * time))
                # máximo para não ficar impossível
                self.spawn_time = max(20, self.spawn_time)
                pygame.time.set_timer(EVENT_ENEMY, self.spawn_time)

            for entity in self.entity_list:
                self.window.blit(source=entity.surface, dest=entity.rect)
                entity.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('enemy_1'))

            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            found_player = False
            for entity in self.entity_list:
                if isinstance(entity, Player):
                    found_player = True

            if not found_player:
                survival_time = (pygame.time.get_ticks() - self.start_time) / 1000
                return survival_time
                # return True


            pygame.display.flip()