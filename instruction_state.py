import pygame
from base_state import GameState

class InstructionsState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.mid_x = self.game.MENU_WIDTH // 2
        self.mid_y = self.game.MENU_HEIGHT // 2
        self.bg = pygame.image.load("assets/bg_screen.png").convert_alpha()
        self.instructions_text = [
    "- Use Arrow Keys to move through the corridors.", #[cite: 15]
    "- Eat all pacgums/ Super-pacgums to complete the level.", #[cite: 15]
    "- Avoid the 4 ghosts. Touching a ghost costs 1 of your lives.", #[cite: 15]
    "- Eat a super-pacgum (in the corners) to make ghosts edible chasing", #[cite: 15]
    "them for a short period of time.",
    "- Gain points by eating pacgums, super-pacgums, and edible ghosts.", #[cite: 15, 17]
    "- Press ESC at any time to pause or return to the main menu." #[cite: 18]
]

    def handle_action(self, action):
        if action.type == pygame.KEYDOWN and action.key == pygame.K_ESCAPE:
            self.game.change_state("MENU")

    def draw(self, surface):
        surface.fill((0, 0, 0))  # Clear the screen with black
        surface.blit(self.bg, (0, 0))
        text = pygame.image.load("assets/title_instructions.png").convert_alpha()
        text_pos = (self.mid_x - text.get_width() // 2, self.mid_y // 16)
        surface.blit(text, text_pos)

        font = pygame.font.Font(None, 26)
        for i, line in enumerate(self.instructions_text):
            text = font.render(line, True, (255, 255, 255))  # white
            text_pos = (self.mid_x - 300, self.mid_y + i * 40 - 300)  # Adjust vertical spacing as needed
            surface.blit(text, text_pos)