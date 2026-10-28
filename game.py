import os
import pygame
from menustate import MenuState
from playingstate import PlayingState
from score_state import ScoreState
from instruction_state import InstructionsState
from pause_state import PauseState


class Game:
    MENU_WIDTH = 600
    MENU_HEIGHT = 800
    PLAY_WIDTH = 1200
    PLAY_HEIGHT = 1000
    def __init__(self, width, height):
        self.width = width
        self.height = height
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # Center the window on the screen
        pygame.init()
        # Keep the global dimensions from your test script
        self.screen = pygame.display.set_mode((self.MENU_WIDTH, self.MENU_HEIGHT)) 
        pygame.display.set_caption("Pac-Man Engine Test")
        self.running = True
        
        # Register your pages
        self.states = {
            "MENU": MenuState(self),
            "PLAYING": PlayingState(self),
            "SCORE": ScoreState(self),  # Placeholder for ScoreState, will be initialized later
            "INSTRUCTIONS": InstructionsState(self),  # Placeholder for InstructionsState, will be initialized later
            "PAUSE": PauseState(self)  # Placeholder for PauseState, will be initialized later
        }
        self.current_state = self.states["MENU"]
        self.clock = pygame.time.Clock()


    def change_state(self, state_name):
        if state_name == "PLAYING" and self.current_state == self.states["MENU"]:
            self.screen = pygame.display.set_mode((self.PLAY_WIDTH, self.PLAY_HEIGHT))
        elif state_name == "MENU" and self.current_state in [self.states["PLAYING"], self.states["PAUSE"]]:
            self.screen = pygame.display.set_mode((self.MENU_WIDTH, self.MENU_HEIGHT))

        self.current_state = self.states[state_name]

    def run(self):
        while self.running:
            # 1. Tick the clock at 60 FPS and capture the milliseconds passed (dt)
            dt = self.clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.current_state.handle_action(event)
            self.screen.fill((0, 0, 0))

            # 2. Call the update method on whichever page is currently active
            if hasattr(self.current_state, "update"):
                self.current_state.update(dt)


            self.current_state.draw(self.screen)
            pygame.display.flip()

        pygame.quit()