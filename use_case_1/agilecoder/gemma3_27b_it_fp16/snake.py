'''
Represents the snake in the game.
Handles snake movement, growth, and collision detection.
'''
class Snake:
    def __init__(self, initial_position, initial_length):
        '''
        Initializes the snake with an initial position and length.
        '''
        self.body = [initial_position]
        for i in range(1, initial_length):
            self.body.append((initial_position[0] - i, initial_position[1]))
        self.direction = "right"
    def move(self, direction):
        '''
        Moves the snake in the given direction.
        '''
        head_x, head_y = self.body[0]
        if direction == "up":
            new_head = (head_x, head_y - 1)
        elif direction == "down":
            new_head = (head_x, head_y + 1)
        elif direction == "left":
            new_head = (head_x - 1, head_y)
        elif direction == "right":
            new_head = (head_x + 1, head_y)
        else:
            return
        self.body.insert(0, new_head)
        self.body.pop()
    def grow(self):
        '''
        Increases the snake's length by adding a new segment to the end of the body.
        '''
        tail_x, tail_y = self.body[-1]  # Get the tail position
        self.body.append((tail_x, tail_y)) # Append tail position to the end of the body
    def check_collision(self, grid_width, grid_height):
        '''
        Checks for collisions with the walls or itself.
        '''
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= grid_width or head_y < 0 or head_y >= grid_height:
            return True
        if self.body[0] in self.body[1:]:
            return True
        return False
    def get_head_position(self):
        '''
        Returns the head position of the snake.
        '''
        return self.body[0]
    def get_body(self):
        '''
        Returns the body of the snake.
        '''
        return self.body