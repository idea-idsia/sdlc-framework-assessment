# food.py
from snake import Snake
class Food:
    def __init__(self, board: GameBoard):
        self.board = board
    def generate_food(self):
        free_positions = [pos for row in self.board.snake.board for pos in enumerate(row) if pos[1] == ' ']
        self.position = random.choice(free_positions)
    def place_food(self):
        x, y = self.position
        self.board.snake.board[y][x] = '*'