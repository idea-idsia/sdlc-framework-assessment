'''
This module contains a class to manage the grid-based game board.
It defines its dimensions and provides methods for displaying it.
'''
import pygame
from constants import GRID_SIZE
class Board:
    def __init__(self, width, height):
        '''
        Initializes the game board with given dimensions.
        Parameters:
            width (int): The width of the game board.
            height (int): The height of the game board.
        '''
        self.width = width
        self.height = height
        self.grid_size = GRID_SIZE
    def draw(self, screen):
        '''
        Draws the grid lines on the provided screen surface.
        Parameters:
            screen: The Pygame screen to draw onto.
        '''
        for x in range(0, self.width, self.grid_size):
            for y in range(0, self.height, self.grid_size):
                rect = pygame.Rect(x, y, self.grid_size, self.grid_size)
                pygame.draw.rect(screen, (128, 128, 128), rect, 1)
    def clear(self):
        '''
        Clears the board by filling it with a solid color.
        This method should be extended to implement more complex clearing
        actions if necessary.
        '''
        screen = pygame.display.get_surface()
        screen.fill((0, 0, 0))