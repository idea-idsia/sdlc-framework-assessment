'''
Handles user input for snake movement.
'''
import pygame
class PlayerInput:
    def __init__(self):
        pass
    def handle_key_down(self, key):
        if key == pygame.K_LEFT:
            return "left"
        elif key == pygame.K_RIGHT:
            return "right"
        elif key == pygame.K_UP:
            return "up"
        elif key == pygame.K_DOWN:
            return "down"
player_input = PlayerInput()