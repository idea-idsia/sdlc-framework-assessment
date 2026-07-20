'''
A basic implementation of a snake game in Python with features such as grid-based game board, snake initialization, food generation, collision handling, score display, and game over condition.
'''
from typing import List
import numpy as np
import random
class Snake:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols))
        self.snake_body = []
        self.direction = 'right'
        self.score = 0
    def update(self):
        # Update the snake's position on the grid.
        for index in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[index] = self.snake_body[index - 1]
        if self.direction == 'right':
            self.snake_body[0][0] += 1
        elif self.direction == 'left':
            self.snake_body[0][0] -= 1
        elif self.direction == 'up':
            self.snake_body[0][1] -= 1
        elif self.direction == 'down':
            self.snake_body[0][1] += 1
    def draw(self):
        # Display the snake on the game board.
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) in self.snake_body:
                    print('O', end='')
                else:
                    print('.', end='')
    def check_collision(self):
        # Check for collisions between the snake and the game board boundaries or its own body.
        if self.snake_body[0][0] >= self.rows or self.snake_body[0][1] >= self.cols:
            print('Game over!')
            return True
        for index in range(len(self.snake_body) - 1):
            if (self.snake_body[index][0], self.snake_body[index][1]) == (self.snake_body[index + 1][0], self.snake_body[index + 1][1]):
                print('Game over!')
                return True
        return False
    def grow(self):
        # Grow the snake by adding a new segment to its body.
        self.snake_body.append((self.snake_body[-1][0], self.snake_body[-1][1] + 1))