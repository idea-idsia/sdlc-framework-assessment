'''
Create a grid-based game board with a defined grid size (e.g., 10x10). Display the grid on the screen.
'''
from typing import List
import numpy as np
class Food:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols))
    def draw(self):
        # Display the food on the game board.
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) in self.food_positions:
                    print('O', end='')
                else:
                    print('.', end='')