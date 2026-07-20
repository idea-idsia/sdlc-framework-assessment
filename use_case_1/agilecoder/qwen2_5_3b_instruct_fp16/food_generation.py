import random
class FoodGenerator:
    @staticmethod
    def generate_food(snake=None):
        if snake is None:
            board = initialize_board()
        else:
            board = [row[:] for row in snake]
        food_position = (random.randint(0, 20), random.randint(0, 20))
        while food_position in [pos for pos, _ in snake]:
            food_position = (random.randint(0, 20), random.randint(0, 20))
        return food_position