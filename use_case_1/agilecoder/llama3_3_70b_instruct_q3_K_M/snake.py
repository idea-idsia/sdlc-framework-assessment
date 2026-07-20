import pygame
'''
The Snake class represents the snake and handles its movement.
'''
class Snake:
    def __init__(self):
        self.body = [(200, 200), (220, 200), (240, 200)]
        self.length = 3
        self.direction = 'right'
    '''
    Moves the snake.
    '''
    def move(self):
        head = self.body[-1]
        if self.direction == 'right':
            new_head = (head[0] + 20, head[1])
        elif self.direction == 'left':
            new_head = (head[0] - 20, head[1])
        self.body.append(new_head)
        if len(self.body) > self.length:
            self.body.pop(0)
    '''
    Resets the snake.
    '''
    def reset(self):
        self.body = [(200, 200), (220, 200), (240, 200)]
        self.length = 3