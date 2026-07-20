"""
This module contains the Grid class.
"""
class Grid:
    def __init__(self, size):
        self.size = size
        self.grid_map = [[None for _ in range(size)] for _ in range(size)]
    def set_position(self, x, y, value):
        if 0 <= x < self.size and 0 <= y < self.size:  # Check bounds
            self.grid_map[y][x] = value
    def get_position(self, x, y):
        return self.grid_map[y][x]