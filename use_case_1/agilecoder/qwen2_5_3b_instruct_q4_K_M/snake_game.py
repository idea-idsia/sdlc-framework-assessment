# snake_game.py
from snake import SnakeGameUIHandler
class SnakeGame:
    def __init__(self):
        self.board_size = (10, 10)
    @property
    def current_direction(self) -> int:
        return self.snake_game.current_direction
    @current_direction.setter
    def current_direction(self, value: int):
        self.snake_game.current_direction = value
    def start_game(self):
        curses.initscr()
        screen = curses.newwin(*self.board_size, 0, 0)
        board = self.draw_board()
        while True:
            if not self.move_snake(self.directions[self.current_direction]):
                break
            # Draw the board with snake and food
            for row in board:
                print(''.join(row))
            screen.refresh()
        curses.endwin()
    def draw_board(self):
        return [self.board_size[0] * ['#'] + [' '] + self.board_size[0] * ['#']]
    @property
    def directions(self) -> dict:
        return {key: (value, 0) for key, value in enumerate(range(256))}
    def move_snake(self, direction: int):
        if not isinstance(direction, int) or direction < 0 or direction > 255:
            raise ValueError("Invalid input. Use one of the following directions: {}".format(", ".join(map(str, list(self.directions.keys())))))
        return self.snake_game.move_snake(direction)