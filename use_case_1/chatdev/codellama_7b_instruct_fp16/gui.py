import tkinter as tk
from snake import Snake
from food import Food
class GUI:
    def __init__(self, master):
        self.master = master
        self.create_widgets()
    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack()
        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)
        self.score_label = tk.Label(self.master, text="Score: 0")
        self.score_label.pack()
    def update(self):
        self.snake.move()
        self.food.spawn()
        if self.snake.collide():
            self.game_over()
    def game_over(self):
        self.master.quit()