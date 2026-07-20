"""
This module contains the Food class.
"""
from random import randint
class Food:
    def __init__(self, grid):
        self.grid = grid
    def generate(self, snake_body):
        while True:
            x, y = randint(0, self.grid.size - 1), randint(0, self.grid.size - 1)
            if (x, y) not in snake_body:  # Check that the food is not on the snake
                break
        self.position = (x, y)
    def get_position(self):
        return self.position