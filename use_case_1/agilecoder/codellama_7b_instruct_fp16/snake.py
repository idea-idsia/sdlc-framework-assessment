'''
snake.py - Class for representing the snake in the game
'''
import pygame
from game_board import GameBoard
from constants import *
class Snake:
    def __init__(self, board, start_position, direction):
        self.board = board  # Initialize board attribute with a GameBoard object
        self.body = [start_position]
        self.direction = direction
    def move(self, direction):
        self.direction = direction
    def update(self):
        head = self.body[0]
        if self.direction == 'right':
            head = (head[0] + 1, head[1])
        elif self.direction == 'left':
            head = (head[0] - 1, head[1])
        elif self.direction == 'up':
            head = (head[0], head[1] - 1)
        elif self.direction == 'down':
            head = (head[0], head[1] + 1)
        if head not in self.board.body:  # Access body attribute on the GameBoard object
            self.body.insert(0, head)
            self.board.body.pop()
        else:
            print('Snake hit itself! Game over')
            pygame.quit()