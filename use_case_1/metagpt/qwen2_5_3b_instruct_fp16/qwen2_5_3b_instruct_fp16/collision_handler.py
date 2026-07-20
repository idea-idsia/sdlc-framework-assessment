class CollisionHandler:
    def __init__(self):
        self.snake = None  # Initialize snake reference to None
    
    def check_collision(self, snake: 'Snake', food: 'Food', board: 'GameBoard') -> bool:
        """
        Check for collisions between the snake and the food or boundaries of the game board.

        Parameters:
            snake (Snake): The current state of the snake.
            food (Food): The current position of the food on the board.
            board (GameBoard): The current state of the game board.

        Returns:
            bool: True if a collision is detected, False otherwise.
        """
        # Check for collision with boundaries
        if not (0 <= snake.position[0] < board.width // 20 and 0 <= snake.position[1] < board.height // 20):
            return True
        
        # Check for collision with itself
        for segment in snake.body[:-1]:  # Exclude the head to avoid checking against itself
            if segment == snake.position:
                return True

        # Check for collision with food
        if snake.position == food.position:
            board.update_grid(board.grid)  # Update grid after eating food
            food.generate_food(board)
            return True
        
        return False
