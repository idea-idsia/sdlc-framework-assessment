'''
Represents the food in the game.
Handles food generation and position management.
'''
import random
class Food:
    def __init__(self, grid_width, grid_height):
        '''
        Initializes the food with grid dimensions.
        '''
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.position = self.generate_new_position([])
    def generate_new_position(self, snake_body):
        '''
        Generates a new position for the food that is not occupied by the snake.
        '''
        while True:
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            if (x, y) not in snake_body:
                return (x, y)
    def get_position(self):
        '''
        Returns the position of the food.
        '''
        return self.position