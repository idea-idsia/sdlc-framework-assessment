'''
Handles user input for snake movement.
'''
import pygame
class PlayerInput:
    def __init__(self):
        pass
    def handle_key_down(self, key):
        if key == pygame.K_LEFT:
            self.direction = "left"
        elif key == pygame.K_RIGHT:
            self.direction = "right"
        elif key == pygame.K_UP:
            self.direction = "up"
        elif key == pygame.K_DOWN:
            self.direction = "down"