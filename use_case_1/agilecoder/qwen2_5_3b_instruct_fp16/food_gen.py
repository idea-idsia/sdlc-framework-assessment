'''
Food generation module.
Randomly places food on the game board avoiding the snake's body.
'''
from typing import List, Tuple
import random
class FoodGenerator:
    def __init__(self):
        self.snake = None
    def generate_food(self, snake: 'Snake') -> Tuple[int]:
        """Generate a new piece of food."""
        while True:
            food_pos = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
            if food_pos not in snake.body and self.is_position_valid(food_pos):
                return food_pos
    def is_position_valid(self, position: Tuple[int]) -> bool:
        """Check if the given position is valid to place a piece of food."""
        x, y = position
        size_x, size_y = GRID_SIZE, GRID_SIZE
        return not (0 <= x < size_x and 0 <= y < size_y)
food_generator = FoodGenerator()