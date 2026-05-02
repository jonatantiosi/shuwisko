"""game.py"""

import pygame

from code.const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTIONS
from code.level import Level
from code.menu import Menu
from code.menu_game_over import MenuGameOver


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        while True:
            menu_game_over = MenuGameOver(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTIONS[0]: # 'NEW GAME'
                player_score = 0
                level = Level(self.window, 'level_1', menu_return, player_score)
                survival_time = level.run(player_score)
                if survival_time:
                    menu_game_over.show(survival_time)


            elif menu_return == MENU_OPTIONS[1]: # 'EXIT'
                pygame.quit()
                quit()

