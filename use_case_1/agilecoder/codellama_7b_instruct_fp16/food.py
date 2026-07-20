'''
food.py - Class for representing food in the game
'''
import pygame
from game_board import GameBoard
from constants import *
class Food:
    def __init__(self, board, start_position):
        self.board = board
        self.x = start_position[0]
        self.y = start_position[1]
    def spawn(self):
        valid_positions = []
        for y in range(self.board.height):
            for x in range(self.board.width):
                if (x, y) not in self.board.snake.body:
                    valid_positions.append((x, y))
        if valid_positions:
            self.x, self.y = random.choice(valid_positions)
        else:
            print('No valid food positions left!')