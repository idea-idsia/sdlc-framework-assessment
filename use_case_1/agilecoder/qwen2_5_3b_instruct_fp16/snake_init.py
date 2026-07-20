import snake_game.utils as utils
class SnakeInit:
    @staticmethod
    def initialize_board():
        return [[utils.SPACE for _ in range(21)] for _ in range(21)]
    @staticmethod
    def generate_food(snake=None):
        board = SnakeInit.initialize_board()
        food_position = (random.randint(0, 20), random.randint(0, 20))
        while food_position in snake:
            food_position = (random.randint(0, 20), random.randint(0, 20))
        return food_position
    @staticmethod
    def initialize_snake(board):
        head_x, head_y = board[0].index(utils.SPACE)
        return [(head_x - i % 4, head_y) for i in range(16)]