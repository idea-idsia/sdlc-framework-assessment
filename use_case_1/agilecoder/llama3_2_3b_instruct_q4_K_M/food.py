'''
Generates and manages food at random positions.
'''
import pygame
import random
class Food:
    def __init__(self):
        self.rect = (random.randint(0, 10 - 20) // 20 * 20, random.randint(0, 10 - 20) // 20 * 20)
    def generate(self):
        self.rect = (random.randint(0, 10 - 20) // 20 * 20, random.randint(0, 10 - 20) // 20 * 20)
    def reset(self):
        self.rect = (random.randint(0, 10 - 20) // 20 * 20, random.randint(0, 10 - 20) // 20 * 20)
food = Food()