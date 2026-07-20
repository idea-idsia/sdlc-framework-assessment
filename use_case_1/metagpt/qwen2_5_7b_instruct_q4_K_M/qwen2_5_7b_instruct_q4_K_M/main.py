## main.py

import pygame
from game import Game  # Import the Game class from game.py

def main() -> None:
    """Main function to initialize and run the snake game."""
    width = 640
    height = 480
    game = Game(width, height)  # Initialize a new game instance with default dimensions

    try:
        game.run()  # Start the game loop
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pygame.quit()  # Ensure Pygame quits properly even if an exception occurs

if __name__ == "__main__":
    main()
