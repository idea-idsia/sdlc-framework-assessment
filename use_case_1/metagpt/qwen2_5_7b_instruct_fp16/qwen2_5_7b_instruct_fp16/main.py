## main.py

import pygame
from game import Game

def main():
    """
    Main function to run the snake game.
    
    :return: None
    """
    # Initialize Pygame
    pygame.init()
    
    # Create a game instance with default screen size (400x400)
    game = Game(400, 400)
    
    try:
        # Run the game loop
        game.run()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
