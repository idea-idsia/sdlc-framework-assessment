import random
import os
import termios
import sys

class SnakeGame:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]
        self.snake = [(height // 2, width // 2)]
        self.direction = (0, 1)  # Starting direction: right
        self.food = None
        self.score = 0
        self.place_food()

    def display_grid(self):
        os.system('clear')  # Clear the console
        for row in self.grid:
            print(' '.join(row))
        print(f"Score: {self.score}")

    def set_direction(self, direction):
        if direction == 'UP' and self.direction != (1, 0):  # Prevent reverse movement
            self.direction = (-1, 0)
        elif direction == 'DOWN' and self.direction != (-1, 0):
            self.direction = (1, 0)
        elif direction == 'LEFT' and self.direction != (0, 1):
            self.direction = (0, -1)
        elif direction == 'RIGHT' and self.direction != (0, -1):
            self.direction = (0, 1)

    def move_snake(self):
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        if not (0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width) or new_head in self.snake:
            print("Game Over!")
            exit()

        self.snake.insert(0, new_head)

        # Check for food collision
        if new_head == self.food:
            self.score += 1
            self.place_food()
        else:
            self.snake.pop()  # Remove the tail

        self.update_grid()

    def update_grid(self):
        # Clear the grid
        for row in range(self.height):
            for col in range(self.width):
                self.grid[row][col] = ' '
        # Draw the snake
        for x, y in self.snake:
            if 0 <= x < self.height and 0 <= y < self.width:  # Ensure it's within bounds
                self.grid[x][y] = '#'
        # Place food on the grid
        if self.food:
            fx, fy = self.food
            if 0 <= fx < self.height and 0 <= fy < self.width:
                self.grid[fx][fy] = 'F'

    def place_food(self):
        while True:
            fx, fy = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            if (fx, fy) not in self.snake:
                break
        self.food = (fx, fy)

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ch

    def main_loop(self):
        while True:
            key = self.get_key()
            if key == '\x1b':  # ESC key
                break
            elif key == 'w':
                self.set_direction('UP')
            elif key == 's':
                self.set_direction('DOWN')
            elif key == 'a':
                self.set_direction('LEFT')
            elif key == 'd':
                self.set_direction('RIGHT')

            self.move_snake()
            self.display_grid()

if __name__ == "__main__":
    game = SnakeGame()
    game.display_grid()
    game.main_loop()