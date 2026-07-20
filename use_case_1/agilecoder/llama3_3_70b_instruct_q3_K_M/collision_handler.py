import pygame
'''
This class handles collisions between the snake and other objects.
'''
class CollisionHandler:
    def __init__(self, snake, game_board, food):
        self.snake = snake
        self.game_board = game_board
        self.food = food
    '''
    Checks for collisions.
    '''
    def check_collisions(self):
        head = self.snake.body[-1]
        if (head[0] < 0 or head[0] >= self.game_board.screen_width or
            head[1] < 0 or head[1] >= self.game_board.screen_height or
            head in self.snake.body[:-1]):
            return False
        if head == self.food.pos:
            self.snake.length += 1
            self.food.pos = self.food.generate_new_food()
        return True