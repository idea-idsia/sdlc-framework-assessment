## snake.py
class Snake:
    def __init__(self):
        """
        Initialize the Snake object with default values.
        
        Attributes:
            body (list): A list of tuples representing the snake's body positions.
            direction (str): The current direction of the snake.
        """
        self.body = [(200, 200), (220, 200), (240, 200)]
        self.direction = 'RIGHT'

    def move(self):
        """
        Move the snake one step in the current direction.
        
        Updates the snake's body positions based on the current direction.
        """
        head = self.body[-1]
        if self.direction == 'RIGHT':
            new_head = (head[0] + 20, head[1])
        elif self.direction == 'LEFT':
            new_head = (head[0] - 20, head[1])
        elif self.direction == 'UP':
            new_head = (head[0], head[1] - 20)
        elif self.direction == 'DOWN':
            new_head = (head[0], head[1] + 20)
        self.body.append(new_head)
        self.body.pop(0)

    def grow(self):
        """
        Grow the snake by adding a new segment to its body.
        
        Appends a new segment at the end of the snake's body based on the current direction.
        """
        last_segment = self.body[-1]
        if self.direction == 'RIGHT':
            new_segment = (last_segment[0] + 20, last_segment[1])
        elif self.direction == 'LEFT':
            new_segment = (last_segment[0] - 20, last_segment[1])
        elif self.direction == 'UP':
            new_segment = (last_segment[0], last_segment[1] - 20)
        elif self.direction == 'DOWN':
            new_segment = (last_segment[0], last_segment[1] + 20)
        self.body.append(new_segment)

    def check_collision(self, board):
        """
        Check if the snake has collided with the board or itself.
        
        Args:
            board (Board): The game board object.
        
        Returns:
            bool: True if collision is detected, False otherwise.
        """
        head = self.body[-1]
        if (head[0] < 0 or head[0] >= board.width or
                head[1] < 0 or head[1] >= board.height):
            return True
        for segment in self.body[:-1]:
            if segment == head:
                return True
        return False
