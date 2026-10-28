import pygame
from base_state import GameState
from uipanel import UIPanel


class ScoreState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.high_scores = []  # Placeholder for high scores, will be populated later
        self.bg = pygame.image.load("assets/bg_screen.png").convert_alpha()
        # self.img = pygame.image.load("assets/.png").convert_alpha()
        self.panel_img = pygame.image.load("assets/cadre.png").convert_alpha()
        self.panel = UIPanel(self.game, 50, 110, 90, 90, self.panel_img, "1. Hello World")  # Placeholder text lines
        self.mid_x = self.game.MENU_WIDTH // 2
        self.mid_y = self.game.MENU_HEIGHT // 2

    def handle_action(self, action):
        if action.type == pygame.KEYDOWN and action.key == pygame.K_ESCAPE:
            self.game.change_state("MENU")

    def draw(self, surface):
        surface.fill((0, 0, 0))  # Clear the screen with black
        surface.blit(self.bg, (0, 0))
        text = pygame.image.load("assets/title_scores.png").convert_alpha()
        text_pos = (self.mid_x - text.get_width() // 2, self.mid_y // 16)
        surface.blit(text, text_pos)
        self.panel.draw(surface)  # Draw the UI panel with the high scores