import pygame
from base_state import GameState
from mazegenerator import MazeGenerator

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


class PlayingState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.tile_size = 40
        maze_gen = MazeGenerator((self.game.width, self.game.height), seed=42, perfect=False)
        self.cells = []
        for j, row in enumerate(maze_gen.maze):
            row_cells = []
            for i, value in enumerate(row):
                row_cells.append(Cell(i, j, value))
            self.cells.append(row_cells)

    def handle_action(self, action):
        # Press ESC to browse back to the menu
        if action.type == pygame.KEYDOWN and action.key == pygame.K_ESCAPE:
            self.game.change_state("MENU")
        # cheat mode
        if action.type == pygame.KEYDOWN and action.key == pygame.K_f:
            # if I want to write a text in the flat screen, I can use the following code:
            font = pygame.font.Font(None, 36)
            text_surface = font.render("Cheat mode activated!", True, (255, 0, 0))
            self.game.screen.blit(text_surface, (10, 10))

    def draw(self, surface):
        for row in self.cells:
            for cell in row:
                # the maze need to be drawn in the center of the screen leaving a margin of 50 pixels at the top and bottom
                px_x = cell.x * self.tile_size + (self.game.PLAY_WIDTH - len(self.cells[0]) * self.tile_size) // 2
                px_y = cell.y * self.tile_size + (self.game.PLAY_HEIGHT - len(self.cells) * self.tile_size) // 2 + 50

                if not cell.can_go_north:
                    pygame.draw.line(surface, (0, 0, 255), (px_x, px_y), (px_x + self.tile_size, px_y), 2)
                if not cell.can_go_south:
                    pygame.draw.line(surface, (0, 0, 255), (px_x, px_y + self.tile_size), (px_x + self.tile_size, px_y + self.tile_size), 2)
                if not cell.can_go_west:
                    pygame.draw.line(surface, (0, 0, 255), (px_x, px_y), (px_x, px_y + self.tile_size), 2)
                if not cell.can_go_east:
                    pygame.draw.line(surface, (0, 0, 255), (px_x + self.tile_size, px_y), (px_x + self.tile_size, px_y + self.tile_size), 2)