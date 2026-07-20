# game.py
import random
from snake import initialize_score, Scoreboard
class Game:
    def __init__(self, board_size=(10, 10)):
        self.board_size = board_size
        self.score_board = Scoreboard()
    @property
    def score(self) -> int:
        return len(self.snake_positions) - 1
    def play_game(self):
        initialize_score()  # Initialize the score for each game session
        while True:
            snake_input(snake=self)
            food_position = self.generate_food()
            increment_score(initialize_score())  # Increment the score for each move
            handle_input(snake_positions=self.snake_positions())
            if not self.move_snake(self.directions[self.current_direction]):
                break