import pygame
from board import Board
from snake import Snake
from food import Food
from game import Game

def main():
    """
    Main function to run the game.
    """
    # Initialize Pygame
    pygame.init()

    # Create a new game instance
    game = Game()

    # Run the game
    game.run()

if __name__ == "__main__":
    main()
