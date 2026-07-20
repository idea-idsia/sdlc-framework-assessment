import pygame
'''
The GameBoard class represents the game board and handles its display.
'''
class GameBoard:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
    '''
    Draws the game board on the screen.
    '''
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, self.screen_width, self.screen_height), 1)
        for i in range(20, self.screen_width, 20):
            pygame.draw.line(screen, (255, 255, 255), (i, 0), (i, self.screen_height))
        for i in range(20, self.screen_height, 20):
            pygame.draw.line(screen, (255, 255, 255), (0, i), (self.screen_width, i))