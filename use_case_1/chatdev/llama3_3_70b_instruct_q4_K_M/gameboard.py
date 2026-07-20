# Import necessary libraries
import pygame
'''
This file contains the implementation of the GameBoard class.
It represents a game board in the game, with a method to draw the board.
'''
class GameBoard:
    def __init__(self, width, height, block_size):
        # Initialize the game board's dimensions and block size
        self.width = width
        self.height = height
        self.block_size = block_size
    def draw(self, display):
        # Draw the game board on the screen
        for i in range(0, self.width, self.block_size):
            pygame.draw.line(display, (50, 50, 50), (i, 0), (i, self.height))
        for i in range(0, self.height, self.block_size):
            pygame.draw.line(display, (50, 50, 50), (0, i), (self.width, i))