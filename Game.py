import pygame

from Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                pass
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass