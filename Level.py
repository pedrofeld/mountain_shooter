from xml.dom.minidom import Entity

import pygame


class Level:
    def __init__(self, window, name, game_mode):
        self.window = None
        self.name = None
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surface, rect=ent.rect)
                pygame.display.flip()
        pass