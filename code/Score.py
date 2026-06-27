import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_YELLOW, SCORE_POS, MENU_OPTION
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load("assets/ScoreBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('assets/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!', C_YELLOW, SCORE_POS['Title'])
            if game_mode == MENU_OPTION[0]:
                text = 'Player 1 enter your name (4 characters):'
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('assets/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_sur: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_sur.get_rect(center=text_center_pos)
        self.window.blit(source=text_sur, dest=text_rect)