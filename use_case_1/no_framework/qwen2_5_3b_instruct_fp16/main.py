import random

# Game Constants
SCREEN_WIDTH = 50
SCREEN_HEIGHT = 20
GRID_SIZE = 10
SNAKE_SIZE = GRID_SIZE * 3
SNAKE_COLOR = '\x1b[36m'  # Cyan color for snake and food
BOUNDARY_COLOR = '\x1b[37;41m'  # Yellow background for boundary

# ASCII Representation
UP_ARROW, DOWN_ARROW, LEFT_ARROW, RIGHT_ARROW = u'\u25B6', u'\u25BC', u'\u2190', u'\u2192'
GRID_CHAR = 'o'

class SnakeGame:
    def __init__(self):
        self.grid_width = SCREEN_WIDTH // GRID_SIZE
        self.grid_height = SCREEN_HEIGHT // GRID_SIZE
        self.snake = [(self.grid_width // 2, self.grid_height // 2)]
        self.direction = RIGHT_ARROW
        self.score = 0

    def generate_food(self):
        while True:
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            if (x, y) not in self.snake:
                return x, y

    def move_snake(self):
        head_x, head_y = self.snake[0]
        new_head = {
            UP_ARROW: (head_x, head_y - 1),
            DOWN_ARROW: (head_x, head_y + 1),
            LEFT_ARROW: (head_x - 1, head_y),
            RIGHT_ARROW: (head_x + 1, head_y)
        }[self.direction]

        if new_head in self.snake or not (0 <= new_head[0] < self.grid_width and 0 <= new_head[1] < self.grid_height):
            return False

        # Update snake's head
        self.snake.insert(0, new_head)

        # Check if we ate the food
        if self.snake[0] == self.food:
            self.score += 1
            self.generate_food()
        else:
            self.snake.pop()

        return True

    def update_display(self):
        print('\n' * SCREEN_HEIGHT)  # Clear the screen
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                if (x, y) == self.food:
                    print(SNAKE_COLOR + GRID_CHAR + '\033[0m', end='')
                elif (x, y) in self.snake:
                    print(SNAKE_COLOR + GRID_CHAR + '\033[0m', end='')
                else:
                    print(BOUNDARY_COLOR + ' ' + BOUNDARY_COLOR, end='')  # Boundary color
            print()
        print(f'Score: {self.score}')

    def handle_input(self):
        try:
            key = ord(input()) - ord(' ')
            if key in [ord(k) for k in (UP_ARROW, DOWN_ARROW, LEFT_ARROW, RIGHT_ARROW)]:
                self.direction = key
        except EOFError:
            pass  # Ignore ctrl + D

if __name__ == '__main__':
    game = SnakeGame()
    food_x, food_y = game.generate_food()

    while True:
        game.update_display()
        if not game.move_snake():
            break
        game.handle_input()