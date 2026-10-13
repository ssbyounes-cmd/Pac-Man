class GameState:
    def __init__(self, game):
        self.game = game # Reference to the router to call change_state()

    def handle_action(self, action):
        pass

    def draw(self, surface):
        pass