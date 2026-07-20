class Snake:
    def __init__(self, position: tuple[int, int], direction: str = 'right', length: int = 3):
        """
        Initialize the snake with a starting position and direction.
        
        Parameters:
            position (tuple[int, int]): The initial position of the snake's head as (x, y).
            direction (str): The initial direction of the snake ('up', 'down', 'left', 'right').
            length (int): The initial length of the snake. Defaults to 3.
        """
        self.position = position
        self.direction = direction
        self.length = length
        self.body = [position]
    
    def move(self, keys: dict[str, bool] = None) -> None:
        """
        Move the snake in the current direction based on user input or predefined movement logic.
        
        Parameters:
            keys (dict[str, bool]): A dictionary of key states. Defaults to None.
        """
        if not keys:
            keys = self._get_keys_pressed()
        
        new_head = self.position
        if keys.get('UP', False) and self.direction != 'down':
            self.direction = 'up'
        elif keys.get('DOWN', False) and self.direction != 'up':
            self.direction = 'down'
        elif keys.get('LEFT', False) and self.direction != 'right':
            self.direction = 'left'
        elif keys.get('RIGHT', False) and self.direction != 'left':
            self.direction = 'right'
        
        if self.direction == 'up':
            new_head = (self.position[0], max(0, self.position[1] - 20))
        elif self.direction == 'down':
            new_head = (self.position[0], min(self.game_board.height // 20 - 1, self.position[1] + 20))
        elif self.direction == 'left':
            new_head = (max(0, self.position[0] - 20), self.position[1])
        else:  # direction == 'right'
            new_head = (min(self.game_board.width // 20 - 1, self.position[0] + 20), self.position[1])
        
        if new_head != self.body[-1]:
            self.body.append(new_head)
            if len(self.body) > self.length:
                self.body.pop(0)
    
    def grow(self) -> None:
        """
        Grow the snake by adding a segment to its body.
        """
        self.body.append(self.position)
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value: tuple[int, int]):
        if not (0 <= value[0] < self.game_board.width // 20 and 0 <= value[1] < self.game_board.height // 20):
            raise ValueError("Position out of bounds")
        self._position = value
    
    @property
    def direction(self):
        return self._direction
    
    @direction.setter
    def direction(self, value: str):
        if value not in ['up', 'down', 'left', 'right']:
            raise ValueError("Invalid direction")
        self._direction = value
    
    @property
    def length(self):
        return len(self.body)
    
    @length.setter
    def length(self, value: int):
        self._length = max(value, 1)  # Ensure the length is at least 1

    def _get_keys_pressed(self) -> dict[str, bool]:
        """
        Get a dictionary of key states from pygame.
        
        Returns:
            dict[str, bool]: A dictionary where keys are 'UP', 'DOWN', 'LEFT', 'RIGHT' and values are True if the corresponding key is pressed.
        """
        return {
            'UP': pygame.key.get_pressed()[pygame.K_UP],
            'DOWN': pygame.key.get_pressed()[pygame.K_DOWN],
            'LEFT': pygame.key.get_pressed()[pygame.K_LEFT],
            'RIGHT': pygame.key.get_pressed()[pygame.K_RIGHT]
        }
