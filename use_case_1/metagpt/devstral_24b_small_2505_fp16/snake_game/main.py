"""
Main entry point for the Snake Game application.
This module initializes and starts the game by creating an instance of SnakeGame.
"""

from snake_game import SnakeGame

def main() -> None:
    """
    Main function to initialize and start the SnakeGame.
    """
    game = SnakeGame()
    game.run()

if __name__ == "__main__":
    main()
