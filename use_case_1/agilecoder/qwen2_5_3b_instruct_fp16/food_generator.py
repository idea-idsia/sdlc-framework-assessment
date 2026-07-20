import random
class FoodGenerator:
    def __init__(self):
        pass
    @staticmethod
    def generate_food(game_board):
        x, y = random.randint(0, game_board.grid_size - 1), random.randint(0, game_board.grid_size - 1)
        while (x, y) in game_board.snake.body:
            x, y = random.randint(0, game_board.grid_size - 1), random.randint(0, game_board.grid_size - 1)
        return (x, y)