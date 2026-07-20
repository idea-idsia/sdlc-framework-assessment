## food.py
import pygame
import random

class Food:
    """
    Represents the food for the snake.
    """

    def __init__(self, width: int, height: int, color: tuple = (255, 0, 0)):
        """
        Initializes the food.

        Args:
            width (int): The width of the game board in blocks.
            height (int): The height of the game board in blocks.
            color (tuple, optional): The color of the food. Defaults to red.
        """
        self.width = width
        self.height = height
        self.color = color
        self.position = self.generate(width, height)

    def generate(self, width: int, height: int) -> tuple:
        """
        Generates food at a random position on the game board.

        Args:
            width (int): The width of the game board in blocks.
            height (int): The height of the game board in blocks.

        Returns:
            tuple: The position of the food.
        """
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        self.position = (x, y)
        return self.position

    def draw(self, screen: pygame.Surface, block_size: int):
        """
        Draws the food on the screen.

        Args:
            screen (pygame.Surface): The screen to draw the food on.
            block_size (int): The size of each block in pixels.
        """
        x, y = self.position
        pygame.draw.rect(screen, self.color, (x * block_size, y * block_size, block_size, block_size))

    def get_position(self) -> tuple:
        """
        Returns the position of the food.

        Returns:
            tuple: The position of the food.
        """
        return self.position
