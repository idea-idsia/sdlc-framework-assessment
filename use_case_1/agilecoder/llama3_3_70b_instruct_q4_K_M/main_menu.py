# Python
'''
This module contains the MainMenu class.
It displays the main menu and handles user input.
The user can select a difficulty level before starting the game.
'''
import pygame
class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.options = ["Easy", "Medium", "Hard"]
        self.selected_option = 0
    def render(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Select Difficulty:", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))
        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected_option else (128, 128, 128)
            text = font.render(option, True, color)
            self.screen.blit(text, (10, 50 + i * 30))
        pygame.display.flip()
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected_option]
        return None