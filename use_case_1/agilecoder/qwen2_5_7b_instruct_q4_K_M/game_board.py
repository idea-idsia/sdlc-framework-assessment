"""
Game Board Class
"""
import pygame
from utils import generate_random_position
class GameBoard:
    def __init__(self, screen):
        self.screen = screen
        self.grid_size = 20
        self.grid_dimensions = (10, 10)
        self.food_position = None
    def draw(self):
        """
        Draws the game board and food.
        This method clears the screen with black color, then draws the grid and food positions.
        """
        self.screen.fill((0, 0, 0))  # Clear the screen with black color
        for y in range(self.grid_dimensions[1]):
            for x in range(self.grid_dimensions[0]):
                rect = pygame.Rect(x * self.grid_size, y * self.grid_size, self.grid_size, self.grid_size)
                if (x, y) == self.food_position:
                    pygame.draw.rect(self.screen, (255, 0, 0), rect)  # Red food
                else:
                    pygame.draw.rect(self.screen, (169, 169, 169), rect)  # Gray background
    def generate_food(self):
        self.food_position = generate_random_position(self.grid_dimensions)