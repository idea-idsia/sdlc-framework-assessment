"""
This module contains the Snake class.
"""
from tkinter import Canvas
import random
class Direction:
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)
class Snake:
    def __init__(self, canvas, grid, x, y, direction):
        self.canvas = canvas
        self.grid = grid
        self.body = [(x, y)]
        self.direction = direction
    def set_direction(self, new_dir):
        # Ensure we don't reverse direction immediately
        if (new_dir == Direction.LEFT and self.direction != Direction.RIGHT) or \
           (new_dir == Direction.RIGHT and self.direction != Direction.LEFT) or \
           (new_dir == Direction.UP and self.direction != Direction.DOWN) or \
           (new_dir == Direction.DOWN and self.direction != Direction.UP):
            self.direction = new_dir
    def move(self):
        x, y = self.body[0]
        dx, dy = self.direction
        # Move the snake's head
        x_new, y_new = x + dx, y + dy
        if 0 <= x_new < self.grid.size and 0 <= y_new < self.grid.size:  # Check bounds
            if (x_new, y_new) in self.body:
                raise Exception("Snake collided with itself")
            elif (x_new, y_new) == self.grid.get_position(x, y):
                raise Exception("Snake hit a wall")
            self.body.insert(0, (x_new, y_new))
            # Remove the tail if no food was eaten
            if (x_new, y_new) != self.grid.get_position(*self.body[-1]):
                del self.body[-1]
            # Redraw snake on canvas
            for segment in self.body:
                x, y = segment
                self.canvas.create_rectangle(x * 50, y * 50, (x + 1) * 50, (y + 1) * 50, fill="green")
        else:
            raise Exception("Snake hit a wall")
    def grow(self):
        x, y = self.body[0]
        dx, dy = self.direction
        x_new, y_new = x + dx, y + dy
        # Ensure the new head position is not out of bounds or on the body
        if (x_new, y_new) in self.body:
            raise Exception("Snake collided with itself")
        self.body.insert(0, (x_new, y_new))
    def get_head_position(self):
        return self.body[0]