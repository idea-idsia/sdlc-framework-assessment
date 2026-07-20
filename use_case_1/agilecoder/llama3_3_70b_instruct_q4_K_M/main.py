# Python
'''
This module contains the main function.
It initializes Pygame and sets up the game loop.
The game loop handles user input, updates the game state, and renders the game board.
'''
import pygame
from game import Game
def initialize_pygame():
    try:
        pygame.init()
        return True
    except pygame.error as e:
        print(f"Failed to initialize Pygame: {e}")
        raise
def main():
    if not initialize_pygame():
        print("Pygame initialization failed. Exiting program.")
        return
    screen_width = 800
    screen_height = 600
    try:
        screen = pygame.display.set_mode((screen_width, screen_height))
    except Exception as e:
        print(f"Failed to set up display mode: {e}")
        pygame.quit()
        return
    game = Game(screen, "Easy")
    game.run()
if __name__ == "__main__":
    main()