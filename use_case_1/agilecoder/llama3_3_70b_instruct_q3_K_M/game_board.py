import pygame
'''
This class represents the game board.
'''
class GameBoard:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
    '''
    Draws the game board on the screen.
    '''
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, self.screen_width, self.screen_height), 1)