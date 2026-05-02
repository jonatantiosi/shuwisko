from code.const import WINDOW_HEIGHT
from code.enemy import Enemy
from code.entity import Entity
from code.player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(entity: Entity):
        if isinstance(entity, Enemy):
            if entity.rect.bottom >= WINDOW_HEIGHT:
                entity.health = 0

    @staticmethod
    def __verify_collision_entity(entity_1, entity_2):
        valid_interaction = False # Flag
        if isinstance(entity_1, Enemy) and isinstance(entity_2, Player):
            valid_interaction = True
        elif isinstance(entity_1, Player) and isinstance(entity_2, Enemy):
            valid_interaction = True

        if valid_interaction:
            if (entity_1.rect.right >= entity_2.rect.left and
            entity_1.rect.left <= entity_2.rect.right and
            entity_1.rect.bottom >= entity_2.rect.top and
            entity_1.rect.top <= entity_2.rect.bottom):
                entity_1.health -= entity_2.damage
                entity_2.health -= entity_1.damage

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity_1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity_1)
            # i + 1 resolve o problema das redundâncias e.g. Player com Player
            for j in range(i+1, len(entity_list)):
                entity_2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity_1, entity_2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for entity in entity_list:
            if entity.health <= 0:
                entity_list.remove(entity)
