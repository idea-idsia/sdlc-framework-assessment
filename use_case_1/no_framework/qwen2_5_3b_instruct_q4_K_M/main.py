import os
import random

# Constants
ROWS, COLS = 20, 20
UP, DOWN, LEFT, RIGHT = 'w', 's', 'a', 'd'
score = 0


def clear_screen():
    # Clear screen function for Windows and Unix systems.
    os.system('cls' if os.name == 'nt' else 'clear')


class SnakeGame:
    def __init__(self):
        self.grid = [[' '] * COLS for _ in range(ROWS)]
        self.snake = [(5, 5)]  # Initial position
        self.direction = RIGHT

        # Position for the food
        self.food_pos = (random.randint(0, ROWS - 1), random.randint(0, COLS - 1))

    def display_grid(self):
        clear_screen()
        for row in range(ROWS):
            print(' '.join([self.grid[row][col] if (row, col) != self.food_pos else 'O'
                            for col in range(COLS)]))

    def move_snake(self):
        x, y = self.snake[0]
        dx, dy = self.direction
        new_head = (x + dx, y + dy)

        if 0 <= new_head[0] < ROWS and 0 <= new_head[1] < COLS:
            # Check for snake body collision before moving the head.
            if new_head in self.snake[1:]:
                return False

            # Remove last segment of the snake
            tail = self.snake.pop()
            self.grid[tail[0]][tail[1]] = ' '

            # Place new head and update grid with the character representing the snake's body
            self.snake.insert(0, new_head)
            self.grid[new_head[0]][new_head[1]] = '\u25CB'  # Unicode for square
            if new_head == self.food_pos:
                score += 1
                self.food_pos = (random.randint(0, ROWS - 1), random.randint(0, COLS - 1))
        else:
            return False

        return True

    def handle_input(self):
        pressed_key = input('Press arrow keys to move: ')

        if pressed_key == UP and self.direction != DOWN:
            self.direction = UP
        elif pressed_key == DOWN and self.direction != UP:
            self.direction = DOWN
        elif pressed_key == LEFT and self.direction != RIGHT:
            self.direction = LEFT
        elif pressed_key == RIGHT and self.direction != LEFT:
            self.direction = RIGHT

    def play_game(self):
        game_over = False

        while not game_over:
            game_over = self.move_snake()
            self.display_grid()
            if not game_over:
                self.handle_input()


game = SnakeGame()
game.play_game()