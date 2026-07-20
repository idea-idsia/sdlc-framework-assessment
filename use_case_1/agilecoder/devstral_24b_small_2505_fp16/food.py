import random

class Food:
    def __init__(self, grid_dimensions):
        self.grid_dimensions = grid_dimensions
        self.position = (0, 0)

    def generate_food(self):
        x = random.randint(0, self.grid_dimensions[0] - 1)
        y = random.randint(0, self.grid_dimensions[1] - 1)
        self.position = (x, y)