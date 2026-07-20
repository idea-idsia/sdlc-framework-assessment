## main.py

import pygame

from game import Game  # Assuming Game class is defined in game.py

def main():
    """
    Main function to initialize and run the snake game.
    """
    width = 800
    height = 600
    game = Game(width, height)
    
    try:
        game.run()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
