import pygame
import random
'''
The Food class represents the food and handles its generation.
'''
class Food:
    def __init__(self):
        self.pos = self.generate_food()
    '''
    Generates a new food position.
    '''
    def generate_food(self, snake=None):
        while True:
            x = random.randint(0, 39) * 20
            y = random.randint(0, 29) * 20
            if (x, y) not in [(s[0], s[1]) for s in snake.body] if snake else True:
                return (x, y)
        self.pos = self.generate_food()