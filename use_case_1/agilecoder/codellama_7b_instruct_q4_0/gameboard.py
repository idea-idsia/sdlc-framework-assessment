'''
Create a grid-based game board with a defined grid size (e.g., 10x10). Display the grid on the screen.
'''
from typing import List
import numpy as np
class GameBoard:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols))
    def draw(self):
        # Display the game board on the screen.
        for row in range(self.rows):
            for col in range(self.cols):
                print('O', end='')