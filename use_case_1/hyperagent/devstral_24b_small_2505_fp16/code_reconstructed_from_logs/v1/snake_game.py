import random

# Constants
GRID_WIDTH = 10
GRID_HEIGHT = 10
SNAKE_INITIAL_LENGTH = 3
DIRECTION_RIGHT = 'RIGHT'

class SnakeGame:
    def __init__(self):
        self.grid = [[' ' for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.snake = [(GRID_HEIGHT // 2, GRID_WIDTH // 2 - i) for i in range(SNAKE_INITIAL_LENGTH)]
        self.direction = DIRECTION_RIGHT
        self.place_snake()
        self.food_position = None

    def place_snake(self):
        for y, x in self.snake:
            self.grid[y][x] = 'S'

    def move_snake(self):
        head_y, head_x = self.snake[0]
        if self.direction == DIRECTION_RIGHT:
            new_head = (head_y, head_x + 1)
        # Add more directions as needed

        if not self.is_valid_move(new_head):
            return False  # Collision detected or out of bounds

        self.snake.insert(0, new_head)
        self.grid[new_head[0]][new_head[1]] = 'S'
        tail_y, tail_x = self.snake.pop()
        self.grid[tail_y][tail_x] = ' '

        return True

    def is_valid_move(self, position):
        y, x = position
        if not (0 <= y < GRID_HEIGHT and 0 <= x < GRID_WIDTH) or position in self.snake:
            return False
        return True

    def generate_food(self):
        while True:
            y = random.randint(0, GRID_HEIGHT - 1)
            x = random.randint(0, GRID_WIDTH - 1)
            if (y, x) not in self.snake:
                break
        self.food_position = (y, x)
        self.grid[y][x] = 'F'

    def display_grid(self):
        for row in self.grid:
            print(' '.join(row))
        print()

def main():
    game = SnakeGame()
    game.generate_food()
    while True:
        game.display_grid()
        if not game.move_snake():
            break
        # Add food consumption and other logic here

if __name__ == '__main__':
    main()