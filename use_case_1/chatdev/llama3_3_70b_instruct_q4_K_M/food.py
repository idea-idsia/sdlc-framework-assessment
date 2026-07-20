# Import necessary libraries
import pygame
import random
'''
This file contains the implementation of the Food class.
It represents food in the game, with a method to generate new food at a random position.
'''
class Food:
    def __init__(self, block_size):
        # Initialize the food's position and block size
        self.position = (random.randint(0, 39) * block_size, random.randint(0, 29) * block_size)
        self.block_size = block_size
    def generate(self, width, height):
        # Generate new food at a random position within the game board
        self.position = (random.randint(0, width // self.block_size - 1) * self.block_size, 
                         random.randint(0, height // self.block_size - 1) * self.block_size)