from base_state import GameState
from button import button
import pygame

class PauseState(GameState):
    def __init__(self, game):
        super().__init__(game)
        
        # 1. Create a black surface the exact size of the play area
        self.overlay = pygame.Surface((self.game.PLAY_WIDTH, self.game.PLAY_HEIGHT))
        self.overlay.fill((0, 0, 0))
        
        # 2. Set the transparency level (0 is invisible, 255 is pitch black)
        # 150 gives a perfect "dimmed" look
        self.overlay.set_alpha(220)
        
        # 3. Load panel and the "PAUSED" text image
        self.panel = pygame.image.load("assets/panel_pause.png").convert_alpha()
        self.paused_text = pygame.image.load("assets/title_paused.png").convert_alpha()
        self.panel_x = self.game.PLAY_WIDTH // 2 - self.panel.get_width() // 2
        self.panel_y = self.game.PLAY_HEIGHT // 2 - self.panel.get_height() // 2

        # 4. Render the two buttons for "Resume" and "Back to Menu"
        btn_normal = pygame.image.load("assets/button_normal.png").convert_alpha()
        btn_hover = pygame.image.load("assets/button_hover.png").convert_alpha()
        self.btn_resume = button(self.panel_x + 110, self.panel_y + 150, btn_normal, btn_hover, "Resume")
        self.btn_menu = button(self.panel_x + 110, self.panel_y + 220, btn_normal, btn_hover, "Main Menu")

    def handle_action(self, action):
        if action.type == pygame.KEYDOWN and action.key == pygame.K_SPACE:
            self.game.change_state("PLAYING")
        if action.type == pygame.MOUSEBUTTONDOWN and action.button == 1:
            if self.btn_resume.is_clicked(action):
                self.game.change_state("PLAYING")
            elif self.btn_menu.is_clicked(action):
                self.game.change_state("MENU")

    def draw(self, surface):
        # 1. Draw the frozen game board first
        self.game.states["PLAYING"].draw(surface)
        
        # 2. Blit the dark transparent overlay on top
        surface.blit(self.overlay, (0, 0))
        surface.blit(self.panel, (self.panel_x, self.panel_y))
        width_start = self.panel.get_width() // 2 - self.paused_text.get_width() // 2
        surface.blit(self.paused_text, (self.panel_x + width_start, self.panel_y + 20))
        self.btn_resume.draw(surface)
        self.btn_menu.draw(surface)