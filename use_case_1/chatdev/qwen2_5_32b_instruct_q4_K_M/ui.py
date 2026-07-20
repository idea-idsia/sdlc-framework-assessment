'''
UserInterface class to handle UI elements like score display and game over messages.
Handles rendering text on the screen for user interface purposes.
'''
import pygame
from constants import COLORS
class UserInterface:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)
    def display_score(self, score):
        text = f'Score: {score}'
        label = self.font.render(text, True, COLORS['WHITE'])
        self.screen.blit(label, (10, 10))
    def game_over_screen(self):
        text_gameover = "Game Over!"
        label = self.font.render(text_gameover, True, COLORS['RED'])
        x, y = (self.width // 2 - label.get_width() // 2), (self.height // 3)
        self.screen.blit(label, (x, y))