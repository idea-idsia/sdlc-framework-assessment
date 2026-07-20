'''
Entry point for the Snake game. Instantiates the Game class and starts the loop.
'''
import sys
from game import Game
def main():
    game = Game()
    game.run()
if __name__ == "__main__":
    main()