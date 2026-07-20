# Python
'''
This module contains the Snake class.
It represents a snake on the game board, with attributes for its position and methods for moving and checking collisions.
'''
import pygame
class Snake:
    def __init__(self):
        self.body = [(200, 200), (220, 200), (240, 200)]
        self.direction = (1, 0)
        self.growing = False
    def move(self):
        head = self.body[-1]
        new_head = (head[0] + self.direction[0] * 20, head[1] + self.direction[1] * 20)
        self.body.append(new_head)
        if len(self.body) > 3 and not self.growing:
            self.body.pop(0)
    def collides_with_wall(self):
        head = self.body[-1]
        return (head[0] < 0 or head[0] >= 800 or
                head[1] < 0 or head[1] >= 600)
    def collides_with_self(self):
        head = self.body[-1]
        for pos in self.body[:-1]:
            if pos == head:
                return True
        return False
    def eats_food(self, food):
        head = self.body[-1]
        return (head[0] == food.position[0] and
                head[1] == food.position[1])
    def grow(self):
        # Set a flag to indicate that the snake is growing
        self.growing = True