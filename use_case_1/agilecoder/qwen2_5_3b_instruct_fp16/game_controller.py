import snake_init
from growth import grow_snake
class GameController:
    def __init__(self):
        self.board = snake_init.initialize_board()
        self.snake = snake_init.initialize_snake(self.board)
        self.direction = 'RIGHT'
        self.food_position = snake_init.generate_food()
    def handle_movement(self, direction=None):
        if direction is not None:
            self.direction = direction
        new_head = move_snake(self.board, self.snake[0], self.direction)
        if not detect_collision(new_head, self.snake + [self.snake[0]]):
            self.board[new_head[1]][new_head[0]] = 'S'
            snake_init.move_snake(self.snake, new_head)
            grow_snake(self.board, self.snake)
            return True
        else:
            return False
    def detect_collision(self):
        head = self.snake[-1]
        return not is_valid_move(self.board, head)
# Helper function to validate move
def is_valid_move(board, position):
    x, y = position
    return 0 <= x < len(board[0]) and 0 <= y < len(board) and board[y][x] == ' '