import random

# Constants
GRID_WIDTH = 10
GRID_HEIGHT = 10
SNAKE_LENGTH = 3

class SnakeGame:
    def __init__(self):
        self.grid = [[' ' for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.snake = [(4, 5), (4, 6), (4, 7)]  # Initial position of the snake
        self.direction = 'RIGHT'  # Initial direction

    def display_grid(self):
        for row in self.grid:
            print(' '.join(row))
        print()

    def initialize_game(self):
        # Place the snake on the grid
        for x, y in self.snake:
            self.grid[x][y] = 'S'

    def main_loop(self):
        self.initialize_game()
        self.display_grid()
        # Here you would add game logic like movement, food generation, etc.

if __name__ == "__main__":
    game = SnakeGame()
    game.main_loop()