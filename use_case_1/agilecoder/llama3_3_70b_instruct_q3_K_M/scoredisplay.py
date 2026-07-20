import pygame
'''
The ScoreDisplay class displays the current score.
'''
class ScoreDisplay:
    def __init__(self):
        self.score = 0
    '''
    Updates the score.
    '''
    def update_score(self, length):
        self.score = length
    '''
    Draws the score on the screen.
    '''
    def display_score(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        screen.blit(text, (10, 10))