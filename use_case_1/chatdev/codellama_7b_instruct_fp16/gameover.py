import tkinter as tk
from snake import Snake
from food import Food
from score import Score
from game_over import GameOver
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
class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.body = [{'x': 250, 'y': 250}]
        self.direction = "right"
    def move(self):
        if self.direction == "right":
            new_position = {'x': self.body[-1]['x'] + 25, 'y': self.body[-1]['y']}
        elif self.direction == "left":
            new_position = {'x': self.body[-1]['x'] - 25, 'y': self.body[-1]['y']}
        elif self.direction == "up":
            new_position = {'x': self.body[-1]['x'], 'y': self.body[-1]['y'] - 25}
        elif self.direction == "down":
            new_position = {'x': self.body[-1]['x'], 'y': self.body[-1]['y'] + 25}
        if self.collide(new_position):
            return
        self.canvas.delete("snake")
        self.body.append(new_position)
        self.canvas.create_rectangle(self.body[-1]['x'], self.body[-1]['y'], self.body[-1]['x'] + 25, self.body[-1]['y'] + 25, fill="green", tags="snake")
    def collide(self, position=None):
        if not position:
            position = self.body[-1]
        if position['x'] < 0 or position['x'] > 400 or position['y'] < 0 or position['y'] > 400:
            return True
        for segment in self.body[:-1]:
            if segment == position:
                return True
        return False
class Food:
    def __init__(self, canvas):
        self.canvas = canvas
    def spawn(self):
        while True:
            x = random.randint(0, 400)
            y = random.randint(0, 400)
            if (x, y) not in self.body:
                break
        self.x = x
        self.y = y
        self.color = "red"
    def draw(self):
        self.canvas.create_rectangle(self.x, self.y, self.x + 25, self.y + 25, fill=self.color)
class Score:
    def __init__(self):
        self.value = 0
    def increase(self):
        self.value += 1
    def get_score(self):
        return self.value
class GameOver:
    def __init__(self, gui):
        self.gui = gui
        self.game_over_message = "Game Over!"
    def display(self):
        self.gui.score_label["text"] = self.game_over_message
root = tk.Tk()
root.title("Snake Game")
gui = GUI(root)
gui.pack()
root.mainloop()