'''
Module that handles food generation on the grid, ensuring it doesn't overlap with the snake.
'''
import random
import pygame
class Food:
    """
    Represents the food item on the board.
    Attributes
    ----------
    position : tuple
        Current (x, y) position of the food.
    """
    def __init__(self, grid_size, snake):
        """
        Initialize food at a random position not occupied by the snake.
        Parameters
        ----------
        grid_size : int
            Size of the square grid.
        snake : Snake
            Reference to the snake instance to avoid overlapping.
        """
        self.grid_size = grid_size
        self.snake = snake
        self.position = self._random_position()
    def _random_position(self):
        """
        Generate a random position on the grid not occupied by the snake.
        Uses a set for efficient lookup.
        If no positions are available (the snake fills the board), returns None.
        """
        all_positions = {(x, y) for x in range(self.grid_size) for y in range(self.grid_size)}
        occupied = set(self.snake.body)
        free_positions = all_positions - occupied
        if not free_positions:
            return None
        return random.choice(list(free_positions))
    def respawn(self):
        """
        Respawn food at a new random position or handle the full-board scenario gracefully.
        """
        new_pos = self._random_position()
        if new_pos is not None:
            self.position = new_pos
        else:
            # If the board is full, keep the old food to avoid crash
            pass