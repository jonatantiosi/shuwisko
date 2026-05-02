"""menu.py"""

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import COLOR_BEIGE, WINDOW_WIDTH, MENU_OPTIONS, COLOR_WHITE, COLOR_CRIMSON


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu_background.png').convert_alpha()
        # especificando posição default
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/menu_background_music.wav')
        # "-1" garante que a música toque indefinidamente
        pygame.mixer_music.play(-1)

        while True:
            # mostrar a imagem
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(100, "SHUWISKO", COLOR_BEIGE, ((WINDOW_WIDTH / 2), 70))

            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTIONS[i], COLOR_CRIMSON, ((WINDOW_WIDTH / 2), 150 + 25 * i))
                else:
                    self.menu_text(30, MENU_OPTIONS[i], COLOR_BEIGE, ((WINDOW_WIDTH / 2), 150 + 25 * i))

            self.menu_text(25, "use keys A W S D to move Shuwisko, the Bat", COLOR_BEIGE, ((WINDOW_WIDTH / 2), 280))
            self.menu_text(25, "and avoid raindrops", COLOR_BEIGE, ((WINDOW_WIDTH / 2), 300))


            # checagem de todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fecha janela
                    quit()  # fecha o jogo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s: # tecla pra baixo
                        if menu_option < len(MENU_OPTIONS) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_w: # tecla pra cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1
                    if event.key == pygame.K_RETURN: # enter
                        return MENU_OPTIONS[menu_option]

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        # metodo copiado do professor, para settar a fonte
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)
