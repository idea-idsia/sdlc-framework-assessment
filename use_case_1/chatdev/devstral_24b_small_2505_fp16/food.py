'''
Food class to represent the food item in the game.
'''
import random
import pygame
from colors import RED  # Import colors from new module
class Food:
    def __init__(self, grid):
        self.grid = grid
        self.position = self.random_position()
    def random_position(self):
        return (random.randint(0, self.grid.width - 1), random.randint(0, self.grid.height - 1))
    def spawn(self):
        self.position = self.random_position()
    def draw(self, screen, cell_size):
        pygame.draw.rect(screen, RED,
                         (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))