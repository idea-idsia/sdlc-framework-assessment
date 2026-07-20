'''
Represents the grid in the game.
'''
import pygame
class Grid:
    def __init__(self, width, height):
        """
        Initializes the grid.
        Args:
            width: The width of the game screen.
            height: The height of the game screen.
        """
        self.width = width
        self.height = height
    def draw(self, screen):
        """
        Draws the grid on the screen.
        """
        for x in range(0, self.width, 20):
            pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, self.height))
        for y in range(0, self.height, 20):
            pygame.draw.line(screen, (255, 255, 255), (0, y), (self.width, y))