import pygame

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./assets/MenuBg.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./assets/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()

        pass