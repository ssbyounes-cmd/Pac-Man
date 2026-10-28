import pygame
from base_state import GameState
from mazegenerator import MazeGenerator
from entities import Pacman, Ghost

class Cell:
    NORTH = 1
    EAST = 2
    SOUTH = 4
    WEST = 8

    def __init__(self, x: int, y: int, val: int):
        self.x = x
        self.y = y
        self.val = val
        # True means the path is open, False means there is a wall
        self.can_go_north = not bool(val & self.NORTH)
        self.can_go_east = not bool(val & self.EAST)
        self.can_go_south = not bool(val & self.SOUTH)
        self.can_go_west = not bool(val & self.WEST)


class Maze:
    def __init__(self, game):
        self.tile_size = 40
        self.game = game
        maze_gen = MazeGenerator((self.game.width, self.game.height), seed=42, perfect=False)
        self.cells = []
        for j, row in enumerate(maze_gen.maze):
            row_cells = []
            for i, value in enumerate(row):
                row_cells.append(Cell(i, j, value))
            self.cells.append(row_cells)
        self.cached_surface = pygame.Surface((game.PLAY_WIDTH, game.PLAY_HEIGHT), pygame.SRCALPHA)
        self._render_to_cache()

    def draw_wall(self, surface: pygame.Surface, x1, y1, x2, y2, thickness=2):
        # Draw Horizontal Line
        if y1 == y2:
            for px in range(x1, x2 + 1):
                for offset in range(thickness):
                    surface.set_at((px, y1 + offset), (0, 0, 255))
        # Draw Vertical Line
        elif x1 == x2:
            for py in range(y1, y2 + 1):
                for offset in range(thickness):
                    surface.set_at((x1 + offset, py), (0, 0, 255))

    def _render_to_cache(self):
        for row in self.cells:
            for cell in row:
                # converting cell coordinates to pixel coordinates for drawing
                px_x = cell.x * self.tile_size + (self.game.PLAY_WIDTH - len(self.cells[0]) * self.tile_size) // 2
                px_y = cell.y * self.tile_size + (self.game.PLAY_HEIGHT - len(self.cells) * self.tile_size) // 2 + 50

                if not cell.can_go_north:
                    self.draw_wall(self.cached_surface, px_x, px_y, px_x + self.tile_size, px_y, 2)
                if not cell.can_go_south:
                    self.draw_wall(self.cached_surface, px_x, px_y + self.tile_size, px_x + self.tile_size, px_y + self.tile_size, 2)
                if not cell.can_go_west:
                    self.draw_wall(self.cached_surface, px_x, px_y, px_x, px_y + self.tile_size, 2)
                if not cell.can_go_east:
                    self.draw_wall(self.cached_surface, px_x + self.tile_size, px_y, px_x + self.tile_size, px_y + self.tile_size, 2)

    def draw(self, surface: pygame.Surface):
        surface.blit(self.cached_surface, (0, 0))

    



class PlayingState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.tile_size = 40
        self.maze = Maze(game)
        self.cells = self.maze.cells

        # Img loading
        self.bg = pygame.image.load("assets/bg_game.png").convert_alpha()
        self.pacman_img = pygame.image.load("assets/sprites/pacman_1.png").convert_alpha()
        self.hud_bar = pygame.image.load("assets/hud_bar.png").convert_alpha()
        self.hud_slot = pygame.image.load("assets/hud_slot.png").convert_alpha()
        self.ghost_img = []
        self.ghost_img.append(pygame.image.load("assets/sprites/ghost_blinky_right_0.png").convert_alpha())
        self.ghost_img.append(pygame.image.load("assets/sprites/ghost_clyde_left_0.png").convert_alpha())
        self.ghost_img.append(pygame.image.load("assets/sprites/ghost_inky_right_0.png").convert_alpha())
        self.ghost_img.append(pygame.image.load("assets/sprites/ghost_pinky_left_0.png").convert_alpha())
        self.widgets = []
        self.widgets.append(pygame.image.load("assets/sprites/clock.png").convert_alpha())
        self.widgets.append(pygame.image.load("assets/sprites/heart.png").convert_alpha())
        self.widgets.append(pygame.image.load("assets/sprites/stage.png").convert_alpha())
        self.widgets.append(pygame.image.load("assets/sprites/score.png").convert_alpha())

        # Pacman in the middle of the maze
        mid_x = len(self.cells[0]) // 2
        mid_y = len(self.cells) // 2
        self.pacman = Pacman()
        self.pacman.x, self.pacman.y = self.get_pixel_pos(mid_x, mid_y, self.pacman_img)

        # 4 Ghosts in the 4 corners
        self.ghosts = [Ghost() for _ in range(4)]
        max_x = len(self.cells[0]) - 1
        max_y = len(self.cells) - 1
        corners = [(0, 0), (max_x, 0), (0, max_y), (max_x, max_y)]
        
        for i, ghost in enumerate(self.ghosts):
            ghost.x, ghost.y = self.get_pixel_pos(corners[i][0], corners[i][1], self.ghost_img[i])

    def handle_action(self, action):
        # Press ESC to browse back to the menu
        if action.type == pygame.KEYDOWN and action.key == pygame.K_ESCAPE:
            self.game.change_state("MENU")
        if action.type == pygame.KEYDOWN and action.key == pygame.K_SPACE:
            self.game.change_state("PAUSE")


    def draw(self, surface):
        # Drawing the maze
        surface.blit(self.bg, (0, 0))
        self.maze.draw(surface)
        surface.blit(self.hud_bar, (0, 0))
        # Draw Pacman and Ghosts
        surface.blit(self.pacman_img, (self.pacman.x, self.pacman.y))
        for n, ghost in enumerate(self.ghosts):
            surface.blit(self.ghost_img[n], (ghost.x, ghost.y))

        # Draw HUD.
        hud_font = pygame.font.Font(None, 36)
        score_text = hud_font.render(f"Score: {self.pacman.score}", True, (255, 255, 255))
        lives_text = hud_font.render(f"Lives: {self.pacman.lives}", True, (255, 255, 255))
        level_text = hud_font.render("Level: 1/10", True, (255, 255, 255))
        time_text = hud_font.render("Time: 90", True, (255, 255, 255))

        # Drawing the texts on the screen with some spacing
        y_pos = 15
        for n, widget in enumerate(self.widgets):
            surface.blit(self.hud_slot, (n * 300 + 40, 5))
            surface.blit(widget, (n * 300 + 50, 10))
        surface.blit(time_text, (90, y_pos))
        surface.blit(lives_text, (390, y_pos))
        surface.blit(level_text, (690, y_pos))
        surface.blit(score_text, (990, y_pos))


    def get_pixel_pos(self, grid_x, grid_y, image):
        """Takes cell coordinates and convert them to page coordinates."""
        # 1. Calculate the maze offset to center it on the screen
        maze_offset_x = (self.game.PLAY_WIDTH - len(self.cells[0]) * self.tile_size) // 2
        maze_offset_y = (self.game.PLAY_HEIGHT - len(self.cells) * self.tile_size) // 2 + 50
        
        # Quick logic shift if the cell is closed for pacman initial positioning
        target_cell = self.cells[int(grid_y)][int(grid_x)]
        is_closed = not (target_cell.can_go_north or target_cell.can_go_south or 
                         target_cell.can_go_east or target_cell.can_go_west)
        if is_closed:
            grid_x -= 1
            
        # 2. Calculate absolute pixel coordinates
        cell_pixel_x = grid_x * self.tile_size + maze_offset_x
        cell_pixel_y = grid_y * self.tile_size + maze_offset_y
        
        # 3. Center the asset inside the 40x40 logical space
        img_width = image.get_width()
        img_height = image.get_height()
        center_offset_x = (self.tile_size - img_width) // 2
        center_offset_y = (self.tile_size - img_height) // 2
        
        return cell_pixel_x + center_offset_x, cell_pixel_y + center_offset_y

    def update(self, dt):
        # Update game logic here
        pass