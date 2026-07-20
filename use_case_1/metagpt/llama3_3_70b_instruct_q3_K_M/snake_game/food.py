import random
from game import Board, Snake

class Food:
    def __init__(self, x: int = 400, y: int = 300):
        """
        Initialize the Food object with default values.
        
        Attributes:
            x (int): The x-coordinate of the food on the game board. Defaults to 400.
            y (int): The y-coordinate of the food on the game board. Defaults to 300.
        """
        self.x = x
        self.y = y

    def generate_new_food(self, board: Board, snake: Snake):
        """
        Generate new food at a random position on the game board.
        
        Args:
            board (Board): The game board object.
            snake (Snake): The snake object.
        
        Returns:
            None
        """
        # Check if board dimensions are valid (multiples of 20)
        if board.width % 20 != 0 or board.height % 20 != 0:
            raise ValueError("Board width and height must be multiples of 20.")
        
        # Generate a list of all possible positions on the board
        possible_positions = [(x, y) for x in range(0, board.width, 20) 
                             for y in range(0, board.height, 20)]
        
        # Filter out positions that are part of the snake's body
        valid_positions = [pos for pos in possible_positions if pos not in snake.body]
        
        # If there are no valid positions, handle game over condition
        if not valid_positions:
            raise Exception("No empty spaces on the board. Game Over.")
        
        # Randomly select a position from the valid ones
        self.x, self.y = random.choice(valid_positions)
