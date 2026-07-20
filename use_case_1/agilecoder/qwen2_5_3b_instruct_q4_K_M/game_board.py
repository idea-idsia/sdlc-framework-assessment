# game_board.py
import numpy as np
class GameBoard:
    def __init__(self, dimensions=(10, 10)):
        self.dimensions = dimensions
        self.board = np.full((dimensions[1], dimensions[0]), " ")
    def display(self):
        for row in self.board:
            print(" ".join(row))