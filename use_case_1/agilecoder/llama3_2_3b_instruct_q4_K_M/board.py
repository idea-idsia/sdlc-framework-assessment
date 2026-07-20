'''
Manages the game board's layout and updates.
'''
import pygame
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def update(self):
        # Update game board here
        pass
    def draw(self, screen):
        # Draw game board here
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(screen, (0, 0, 255), (x * 20, y * 20, 20, 20))