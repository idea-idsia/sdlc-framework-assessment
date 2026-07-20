import pygame
class GameBoard:
    def __init__(self, screen):
        self.screen = screen
    def draw_grid(self):
        for x in range(0, 800, 20):
            pygame.draw.line(self.screen, (40, 40, 40), (x, 0), (x, 600))
        for y in range(0, 600, 20):
            pygame.draw.line(self.screen, (40, 40, 40), (0, y), (800, y))
    def draw_boundaries(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 800, 1))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 599, 800, 1))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 1, 600))
        pygame.draw.rect(self.screen, (0, 0, 0), (799, 0, 1, 600))