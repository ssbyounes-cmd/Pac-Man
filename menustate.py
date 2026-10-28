from base_state import GameState
from button import button
import pygame
import random


class Sparkle:
    def __init__(self, screen_width, screen_height, image):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = image
        
        # Spawn randomly anywhere on the screen initially
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)
        
        # Randomize speed (pixels per second). Smaller particles move slower.
        self.speed = random.uniform(20.0, 60.0)

    def update(self, dt):
        self.y -= self.speed * (dt / 1000.0)
        # Reset the sparkle to the bottom of the screen if it goes off the top
        if self.y < -self.image.get_height():
            self.y = self.screen_height + self.image.get_height()

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, (int(self.x), int(self.y)))




class MenuState(GameState):
    def __init__(self, game):
        super().__init__(game)
        center_x = self.game.MENU_WIDTH // 2
        center_y = self.game.MENU_HEIGHT // 2
        # upload the bg & header for the menu
        self.header_img = pygame.image.load("assets/logo.png").convert_alpha()
        self.header_x = center_x - self.header_img.get_width() // 2
        self.header_y = center_y - 300
        self.bg_img = pygame.image.load("assets/bg_menu.png").convert_alpha()

        # 1. Load the images once
        btn_normal = pygame.image.load("assets/button_normal.png").convert_alpha()
        btn_hover = pygame.image.load("assets/button_hover.png").convert_alpha()
        sparkle_img = pygame.image.load("assets/sparkle.png").convert_alpha()

        self.button_start = button(center_x - 100, center_y - 60, btn_normal, btn_hover, "Start")
        self.button_score = button(center_x - 100, center_y + 0, btn_normal, btn_hover, "Scores")
        self.buton_instructions = button(center_x - 100, center_y + 60, btn_normal, btn_hover, "Instructions")
        self.button_quit = button(center_x - 100, center_y + 120, btn_normal, btn_hover, "Quit")

        # Initialize 100 particles for the background
        self.particles = []
        for _ in range(100):
            self.particles.append(Sparkle(self.game.MENU_WIDTH, self.game.MENU_HEIGHT, sparkle_img))
    
    def handle_action(self, action):
        if action.type == pygame.MOUSEBUTTONDOWN and action.button == 1:
            if self.button_start.is_clicked(action):
                self.game.change_state("PLAYING")
            elif self.button_score.is_clicked(action):
                self.game.change_state("SCORE")
            elif self.buton_instructions.is_clicked(action):
                self.game.change_state("INSTRUCTIONS")
            elif self.button_quit.is_clicked(action):
                self.game.running = False

    def update(self, dt):
        # Calculate the new math for every single particle
        for particle in self.particles:
            particle.update(dt)
        
    def draw(self, surface: pygame.Surface):
        surface.blit(self.bg_img, (0, 0))
        for particle in self.particles:
            particle.draw(surface)
        self.button_start.draw(surface)
        self.button_score.draw(surface)
        self.buton_instructions.draw(surface)
        self.button_quit.draw(surface)
        surface.blit(self.header_img, (self.header_x, self.header_y))