'''
Food class to handle the food's creation and drawing.
Manages the random placement of food on the grid.
'''
import pygame
from constants import GRID_SIZE
class Food:
    def __init__(self):
        self.grid_size = GRID_SIZE
        self.position = (0, 0)
    def new_position(self, width, height):
        x = (pygame.math.randint(0, width // self.grid_size - 1) * self.grid_size)
        y = (pygame.math.randint(0, height // self.grid_size - 1) * self.grid_size)
        self.position = (x, y)
    def draw(self, screen):
        rect = pygame.Rect(self.position[0], self.position[1], self.grid_size, self.grid_size)
        pygame.draw.rect(screen, COLORS['RED'], rect)