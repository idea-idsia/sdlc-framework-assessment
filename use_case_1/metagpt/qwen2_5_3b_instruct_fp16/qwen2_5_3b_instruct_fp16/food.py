"""Defines the Food class with methods to generate new food positions on the game board and update the grid based on the current snake's position."""
from typing import Tuple

class Food:
    def __init__(self, game_board: 'GameBoard'):
        self.game_board = game_board
    
    def generate_food(self, game_board: 'GameBoard') -> None:
        """
        Generate a new food position that is not colliding with the snake.
        
        Parameters:
            game_board (GameBoard): The current state of the game board.
        """
        while True:
            # Generate random position for food
            x = self.game_board.width // 20 + np.random.randint(-1, 2) * 20
            y = self.game_board.height // 20 + np.random.randint(-1, 2) * 20
            
            # Check if the generated position is within bounds and not occupied by the snake
            if (x, y) != game_board.grid[game_board.height // 20 - 1][game_board.width // 20 - 1] and \
               (x, y) != game_board.grid[game_board.height // 20 - 1][0] and \
               (x, y) != game_board.grid[0][game_board.width // 20 - 1] and \
               (x, y) != game_board.grid[0][0]:
                break
        
        # Update the grid with food at the new position
        self.game_board.update_grid(game_board.grid)
        game_board.grid[y][x] = 'F'
