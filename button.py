import pygame

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

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (0, 0, 0))

        text_x = self.x + (self.width // 2) - text_surface.get_width() // 2
        text_y = self.y + (self.height // 2) - 10  # Adjusting for text height
        
        surface.blit(text_surface, (text_x, text_y))

    def is_clicked(self, action):
        mouse_x, mouse_y = action.pos
        if action.type == pygame.MOUSEBUTTONDOWN and action.button == 1:
            if self.x <= mouse_x <= self.x + self.width:
                if self.y <= mouse_y <= self.y + self.height:
                        return True
        return False