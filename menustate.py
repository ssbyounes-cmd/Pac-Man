from base_state import GameState
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


class button:
    def __init__(self, x, y, img_normal, img_hover, text):
        self.x = x
        self.y = y
        self.img_normal = img_normal
        self.img_hover = img_hover
        # Dimensions are now automatically pulled from the PNG
        self.width = img_normal.get_width()
        self.height = img_normal.get_height()
        self.text = text

    def draw(self, surface: pygame.Surface):
        # Dynamically check mouse position to swap images
        mouse_x, mouse_y = pygame.mouse.get_pos()
        is_hovered = self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height
        
        current_img = self.img_hover if is_hovered else self.img_normal
        surface.blit(current_img, (self.x, self.y))

        # Text rendering (retaining MLX compliance math)
        approx_char_width = 12
        approx_text_width = len(self.text) * approx_char_width
        approx_text_height = 20
        
        text_x = self.x + (self.width // 2) - (approx_text_width // 2)
        text_y = self.y + (self.height // 2) - (approx_text_height // 2)
        
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (0, 0, 0))
        surface.blit(text_surface, (text_x, text_y))

    def is_clicked(self, action):
        mouse_x, mouse_y = action.pos
        if action.type == pygame.MOUSEBUTTONDOWN and action.button == 1:
            if self.x <= mouse_x <= self.x + self.width:
                if self.y <= mouse_y <= self.y + self.height:
                        return True
        return False




class MenuState(GameState):
    def __init__(self, game):
        super().__init__(game)
        center_x = self.game.MENU_WIDTH // 2
        center_y = self.game.MENU_HEIGHT // 2
        # creating a header for the menu
        self.header_font = pygame.font.Font(None, 62)
        self.header_text = self.header_font.render("PAC MAN", True, (255, 165, 0)) # orange color
        self.header_x = center_x - self.header_text.get_width() // 2
        self.header_y = center_y - 300

        # 1. Load the images once
        btn_normal = pygame.image.load("assets/button_normal.png").convert_alpha()
        btn_hover = pygame.image.load("assets/button_hover.png").convert_alpha()
        sparkle_img = pygame.image.load("assets/sparkle.png").convert_alpha()

        self.button_start = button(center_x - 100, center_y - 40, btn_normal, btn_hover, "Start")
        self.button_quit = button(center_x - 100, center_y + 20, btn_normal, btn_hover, "Quit")

        # Initialize 100 particles for the background
        self.particles = []
        for _ in range(100):
            self.particles.append(Sparkle(self.game.MENU_WIDTH, self.game.MENU_HEIGHT, sparkle_img))
    
    def handle_action(self, action):
        if action.type == pygame.MOUSEBUTTONDOWN and action.button == 1:
            if self.button_start.is_clicked(action):
                self.game.change_state("PLAYING")
            elif self.button_quit.is_clicked(action):
                self.game.running = False

    def update(self, dt):
        # Calculate the new math for every single particle
        for particle in self.particles:
            particle.update(dt)
        
    def draw(self, surface: pygame.Surface):
        for particle in self.particles:
            particle.draw(surface)
        self.button_start.draw(surface)
        self.button_quit.draw(surface)
        surface.blit(self.header_text, (self.header_x, self.header_y))