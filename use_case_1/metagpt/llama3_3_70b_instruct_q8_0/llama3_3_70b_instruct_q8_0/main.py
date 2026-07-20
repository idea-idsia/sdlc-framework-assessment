"""
This module contains the main entry point for the game.
"""

import pygame
from board import Board
from snake import Snake
from food import Food
from game import Game

def main():
    """
    The main function that runs the game.
    """
    game = Game(20, 20)
    game.run()

if __name__ == "__main__":
    main()
