"""menu.py"""

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import COLOR_BEIGE, WINDOW_WIDTH, MENU_OPTIONS, COLOR_WHITE, WINDOW_HEIGHT


class MenuGameOver:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu_background.png').convert_alpha()
        # especificando posição default
        self.rect = self.surf.get_rect(left=0, top=0)

    def show(self, survival_time):

        pygame.mixer_music.load('./asset/menu_background_music.wav')
        # "-1" garante que a música toque indefinidamente
        pygame.mixer_music.play(-1)

        while True:
            # mostrar a imagem
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(100, "GAME OVER", COLOR_BEIGE, ((WINDOW_WIDTH / 2), (WINDOW_HEIGHT/2)))
            self.menu_text(25, f"You survived for {survival_time:.0f} seconds", COLOR_BEIGE, ((WINDOW_WIDTH / 2), (WINDOW_HEIGHT/2) + 50))
            self.menu_text(25, "Press Esc to leave", COLOR_BEIGE, ((WINDOW_WIDTH / 2), (WINDOW_HEIGHT/2) + 70))

            # checagem de todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fecha janela
                    quit()  # fecha o jogo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        # metodo copiado do professor, para settar a fonte
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)
