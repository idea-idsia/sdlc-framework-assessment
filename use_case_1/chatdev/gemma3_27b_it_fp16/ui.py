'''
Handles the user interface elements of the game.
'''
import pygame
class UI:
    def __init__(self, width, height):
        """
        Initializes the UI.
        Args:
            width: The width of the game screen.
            height: The height of the game screen.
        """
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)
    def draw_score(self, screen, score):
        """
        Draws the score on the screen.
        """
        score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        text_rect = score_text.get_rect(topleft=(10, 10))
        screen.blit(score_text, text_rect)
    def draw_game_over(self, screen, score):
        """
        Draws the game over message and score on the screen.
        """
        game_over_text = self.font.render("Game Over!", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(game_over_text, text_rect)
        score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(self.width // 2, self.height // 2 + 40))
        screen.blit(score_text, score_rect)