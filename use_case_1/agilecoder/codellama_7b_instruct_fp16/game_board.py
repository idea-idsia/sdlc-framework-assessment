'''
game_board.py - Class for representing the game board
'''
import pygame
from constants import *
class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.block_size = 20
        self.board = [[(0, 0, 0) for _ in range(self.width)] for _ in range(self.height)]
    def draw(self, screen, color):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, color, (x * self.block_size, y * self.block_size, self.block_size, self.block_size))