"""
This module contains the Board class, which represents the game board in the snake game.
"""

import pygame

class Board:
    """
    Represents the game board with a grid of squares.
    
    Attributes:
        width (int): The width of the board in number of squares.
        height (int): The height of the board in number of squares.
        grid (list): A 2D list representing the board, where each element is a square.
    """

    def __init__(self, width: int = 20, height: int = 20):
        """
        Initializes a new Board instance with the given width and height.

        Args:
            width (int, optional): The width of the board. Defaults to 20.
            height (int, optional): The height of the board. Defaults to 20.
        """
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def draw_grid(self):
        """
        Draws the grid on the screen using Pygame.

        Note:
            This method assumes that a Pygame window has already been initialized.
        """
        cell_size = 20  # Default cell size
        for i in range(self.height):
            for j in range(self.width):
                rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                pygame.draw.rect(pygame.display.get_surface(), (255, 255, 255), rect, 1)

# Example usage:
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()

    board = Board(20, 20)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black color
        board.draw_grid()  # Draw the grid on the screen
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
