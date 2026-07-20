'''
Grid class to represent the game grid.
'''
import pygame
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def draw_grid(self, screen, cell_size):
        for x in range(0, self.width * CELL_SIZE, CELL_SIZE):
            pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, self.height * CELL_SIZE))
        for y in range(0, self.height * CELL_SIZE, CELL_SIZE):
            pygame.draw.line(screen, (255, 255, 255), (0, y), (self.width * CELL_SIZE, y))