import pygame
class GameBoard:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.snake = Snake()
        self.food_position = None
        self.current_directions = []
    @staticmethod
    def check_valid_move(game_board, snake_head):
        x, y = snake_head
        if 0 <= x < game_board.grid_size and 0 <= y < game_board.grid_size:
            return True
        return False
    @staticmethod
    def update_snake_position(snake_body, new_head):
        for segment in reversed(range(len(snake_body))):
            if segment == len(snake_body) - 1:
                snake_body[segment] = (new_head)
            else:
                snake_body[segment] = snake_body[segment + 1]