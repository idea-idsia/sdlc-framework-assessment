'''
Main entry point of the Snake Game application.
Initializes Pygame and runs the game loop.
'''
import pygame
from game import Game
def main():
    pygame.init()
    game = Game(10, 10)
    game.run()
if __name__ == "__main__":
    main()