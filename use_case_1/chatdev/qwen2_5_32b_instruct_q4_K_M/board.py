'''
Board class to manage the grid-based game board.
Draws the grid on the screen.
'''
import pygame
from constants import GRID_SIZE
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid_size = GRID_SIZE
    def draw(self, screen):
        for x in range(0, self.width, self.grid_size):
            for y in range(0, self.height, self.grid_size):
                rect = pygame.Rect(x, y, self.grid_size, self.grid_size)
                pygame.draw.rect(screen, (128, 128, 128), rect, 1)
    def clear(self, screen):
        screen.fill((0, 0, 0))