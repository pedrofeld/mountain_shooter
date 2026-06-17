from xml.dom.minidom import Entity

class Level:
    def __init__(self, window, name, game_mode):
        self.window = None
        self.name = None
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

    def run(self, ):
        pass