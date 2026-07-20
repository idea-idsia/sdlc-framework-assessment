'''
Module containing the Snake model representing the snake's body, movement and collision logic.
'''
import pygame
class Snake:
    """
    Represents the snake on the board.
    Attributes
    ----------
    body : list of tuples
        List of (x, y) coordinates for each segment, head first.
    direction : tuple
        Current movement direction as (dx, dy).
    """
    def __init__(self, grid_size):
        """
        Initialize the snake with a default length of 3, centered in the grid,
        moving to the right.
        Parameters
        ----------
        grid_size : int
            Size of the square grid.
        """
        self.grid_size = grid_size
        center = grid_size // 2
        self.body = [
            (center - 1, center),
            (center, center),
            (center + 1, center)
        ]
        self.direction = (1, 0)  # moving right initially
    def set_direction(self, new_dir):
        """
        Update the snake's direction if it's not directly opposite to current.
        Parameters
        ----------
        new_dir : tuple
            New direction vector (dx, dy).
        """
        opposite = (-self.direction[0], -self.direction[1])
        if new_dir != opposite:
            self.direction = new_dir
    def move(self):
        """
        Move the snake one step forward in the current direction.
        """
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)
        self.body.pop()  # remove tail segment
    def grow(self):
        """
        Grow the snake by adding a new segment at the current tail position.
        (Deprecated – growth now handled directly in Game logic for accurate placement)
        """
        tail = self.body[-1]
        self.body.append(tail)
    def collides_with_self(self):
        """
        Check if the snake's head collides with its body.
        Returns
        -------
        bool
            True if collision occurs, else False.
        """
        return self.body[0] in self.body[1:]
    def collides_with_wall(self):
        """
        Check if the snake's head collides with the grid boundaries.
        Returns
        -------
        bool
            True if collision occurs, else False.
        """
        head_x, head_y = self.body[0]
        return not (0 <= head_x < self.grid_size and 0 <= head_y < self.grid_size)