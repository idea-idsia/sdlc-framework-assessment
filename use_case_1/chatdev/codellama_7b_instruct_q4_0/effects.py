from effects import GameBoard
import sys
import time
class Snake(object):
    """Define a grid-based game board with a fixed size (e.g., 10x10)."""
    def __init__(self, size=(10, 10)):
        self.size = size
        self.grid = [[' ' for _ in range(size[1])] for _ in range(size[0])]
    def render(self):
        """Render the game board on the screen."""
        print('Game Board:')
        print('  ' + ' '.join(['{:^5}'.format(i) for i in range(1, self.size[0] + 1)]))
        for y in range(self.size[1]):
            print('{} | {}'.format(y + 1, ''.join(['{:^5}'.format(cell) for cell in self.grid[y]])))
    def update(self, snake):
        """Update the game board with the snake's position and length."""
        # Update the snake's position on the grid
        for i in range(len(snake)):
            self.grid[snake.y + i][snake.x] = 'S' if i == 0 else '.'
        # Update the snake's length on the grid
        for i in range(1, len(snake)):
            self.grid[snake.y + i][snake.x] = '*'
# Initialize game board
game_board = GameBoard((10, 10))
# Initialize snake
snake = Snake()
snake.render()
snake.update(snake)