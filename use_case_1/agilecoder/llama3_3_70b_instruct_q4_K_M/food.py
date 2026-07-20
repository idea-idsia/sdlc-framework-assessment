# Python
'''
This module contains the Food class.
It represents food on the game board, with attributes for its position and methods for generating new positions.
'''
import pygame
import random
class Food:
    def __init__(self):
        self.position = (random.randint(0, 39) * 20, random.randint(0, 29) * 20)
    def generate_new_position(self):
        self.position = (random.randint(0, 39) * 20, random.randint(0, 29) * 20)