import pygame

class GameBoard:
    """
    Represents the game board.
    """
    def __init__(self, width: int, height: int, block_size: int, color: tuple = (0, 0, 0)):
        """
        Initializes the game board.

        Args:
            width (int): The width of the game board in blocks.
            height (int): The height of the game board in blocks.
            block_size (int): The size of each block in pixels.
            color (tuple, optional): The color of the game board. Defaults to black.
        """
        self.width = width
        self.height = height
        self.block_size = block_size
        self.color = color

    def draw(self, screen: pygame.Surface):
        """
        Draws the game board on the screen.

        Args:
            screen (pygame.Surface): The screen to draw the game board on.
        """
        pygame.draw.rect(screen, self.color, (0, 0, self.width * self.block_size, self.height * self.block_size))
