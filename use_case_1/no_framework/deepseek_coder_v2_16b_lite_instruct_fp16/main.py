import tkinter as tk
from random import randint

class SnakeGame(tk.Tk):
    def __init__(self, grid_size=10, cell_size=50):
        super().__init__()
        self.title("Snake Game")
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.snake = [(4, 4), (3, 4), (2, 4)]  # Initial snake position
        self.direction = "Right"  # Initial direction
        self.food = (randint(0, grid_size - 1), randint(0, grid_size - 1))
        while self.food in self.snake:
            self.food = (randint(0, grid_size - 1), randint(0, grid_size - 1))
        self.score = 0

        self.canvas = tk.Canvas(self, width=grid_size * cell_size, height=grid_size * cell_size)
        self.canvas.pack()
        self.bind_all("<Key>", self.on_key_press)
        self.game_loop()

    def on_key_press(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    def game_loop(self):
        if self.check_collision():
            return
        head = self.snake[0]
        x, y = head
        if self.direction == "Up":
            y -= 1
        elif self.direction == "Down":
            y += 1
        elif self.direction == "Left":
            x -= 1
        elif self.direction == "Right":
            x += 1
        new_head = (x, y)
        if new_head == self.food:
            self.snake.insert(0, new_head)
            self.score += 1
            self.generate_food()
        else:
            self.snake.insert(0, new_head)
            tail = self.snake.pop()
            self.draw_cell(tail[0], tail[1], "white")
        self.draw_cell(new_head[0], new_head[1], "green")
        if not self.food:
            self.generate_food()
        self.after(150, self.game_loop)

    def generate_food(self):
        x = randint(0, self.grid_size - 1)
        y = randint(0, self.grid_size - 1)
        while (x, y) in self.snake:
            x = randint(0, self.grid_size - 1)
            y = randint(0, self.grid_size - 1)
        self.food = (x, y)
        self.draw_cell(self.food[0], self.food[1], "red")

    def draw_cell(self, x, y, color):
        self.canvas.create_rectangle(x * self.cell_size, y * self.cell_size, (x + 1) * self.cell_size, (y + 1) * self.cell_size, fill=color)

    def check_collision(self):
        head = self.snake[0]
        if head[0] < 0 or head[0] >= self.grid_size or head[1] < 0 or head[1] >= self.grid_size:
            return True
        for segment in self.snake[1:]:
            if head == segment:
                return True
        return False

    def restart(self):
        self.destroy()
        SnakeGame()

if __name__ == "__main__":
    game = SnakeGame()
    game.mainloop()