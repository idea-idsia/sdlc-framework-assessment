*snake.py**
```python
'''
Represents the snake in the game.
'''

2


class Snake:
    def __init__(self, width, height):
        '''
        Initializes the snake with a given width and height.

        Args:
            width (int): The width of the snake's body.
            height (int): The height of the snake's body.
        '''
        self.width = width
        self.height = height
        self.body = [(100, 50), (90, 50), (80, 50)]  # Initial length: 3 segments

    def move(self, snake_body, time):
        '''
        Moves the snake based on its current body and a given time.

        Args:
            snake_body (list): The list of points representing the snake's body.
            time (int): The time elapsed since the last frame.
        '''
        head_x, head_y = self.body[0]
        new_head_x, new_head_y = head_x + 10 * time, head_y
        self.body.insert(0, (new_head_x, new_head_y))
        if len(self.body) > self.width:
            self.body.pop()

    def draw(self, screen):
        '''
        Draws the snake on the given screen.

        Args:
            screen (pygame.Surface): The surface to draw on.
        '''
        for point in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (point[0], point[1], 10, 10))

    def check_collisions(self, food, board):
        '''
        Checks if the snake has collided with the food or its own body.

        Args:
            food (Food): The Food object to check for collision.
            board (Board): The Board object to get the snake's body.
        '''
        head_x, head_y = self.body[0]
        if (head_x < 0 or head_x >= board.width or
                head_y < 0 or head_y >= board.height):
            print("Game Over")
            return True
        elif (head_x, head_y) in [point for point in food.food_body]:
            # Eat the food and grow the snake
            food.generate_new_food()
            self.body.insert(0, (head_x, head_y))
            return True
        else:
            self.body.pop()

    def get_snake_body(self):
        '''
        Gets the list of points representing the snake's body.

        Returns:
            list: The list of points.
        '''
        return [point for point in self.body]
```

**food.py**
```python
'''
Represents a food item in the game.
'''

import random

class Food:
    def __init__(self, width, height):
        '''
        Initializes the food with a given width and height.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
        '''
        self.width = width
        self.height = height
        self.food_body = [(random.randint(0, width-10) // 10 * 10,
                          random.randint(0, height-10) // 10 * 10)]

    def generate_new_food(self):
        '''
        Generates a new food item at a random position on the board.
        '''
        while True:
            x, y = random.randint(0, self.width-10) // 10 * 10,
                  random.randint(0, self.height-10) // 10 * 10
            if (x, y) not in [point for point in self.food_body]:
                self.food_body = [(x, y)]
                break

    def draw(self, screen):
        '''
        Draws the food on the given screen.

        Args:
            screen (pygame.Surface): The surface to draw on.
        '''
        pygame.draw.rect(screen, (255, 0, 0), (self.food_body[0][0], self.food_body[0][1], 10, 10))

    def get_food_body(self):
        '''
        Gets the list of points representing the food's body.

        Returns:
            list: The list of points.
        '''
        return [point for point in self.food_body]
```

**board.py**
```python
'''
Represents a game board with a given width and height.
'''

class Board:
    def __init__(self, width, height):
        '''
        Initializes the board with a given width and height.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
        '''
        self.width = width
        self.height = height

    def draw(self, screen):
        '''
        Draws the board on the given screen.

        Args:
            screen (pygame.Surface): The surface to draw on.
        '''
        for y in range(0, self.height, 10):
            for x in range(0, self.width, 10):
                pygame.draw.rect(screen, (128, 128, 128), (x, y, 10, 10))

    def get_snake_body(self):
        '''
        Gets the list of points representing the snake's body.

        Returns:
            list: The list of points.
        '''
        return [point for point in snake.get_snake_body()]
```

**clock.py**
```python
'''
Represents a clock object to manage time elapsed since the last frame.
'''

class Clock:
    def __init__(self):
        '''
        Initializes the clock.
        '''
        self.time = 0

    def get_time(self):
        '''
        Gets the time elapsed since the last frame.

        Returns:
            int: The time elapsed.
        '''
        return self.time
    def tick(self, delta_time):
        '''
        Ticks the clock by a given amount of time.

        Args:
            delta_time (int): The time to add to the clock.
        '''
        self.time += delta_time

if __name__ == '__main__':
    main()