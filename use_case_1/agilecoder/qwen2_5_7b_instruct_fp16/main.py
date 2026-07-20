"""
This module contains the Game class.
"""
from tkinter import Tk, Canvas
import time
from snake import Snake, Direction
from grid import Grid
from food import Food
class Game:
    def __init__(self):
        root = Tk()
        canvas = Canvas(root, width=500, height=500)
        canvas.pack()
        grid_size = 10
        grid = Grid(grid_size)
        snake_x, snake_y = grid_size // 2, grid_size // 2 - 1
        snake = Snake(canvas, grid, snake_x, snake_y, Direction.RIGHT)
        food = Food(grid)
        # Bind arrow keys to control the snake's movement
        root.bind('<Left>', lambda event: snake.set_direction(Direction.LEFT))
        root.bind('<Right>', lambda event: snake.set_direction(Direction.RIGHT))
        root.bind('<Up>', lambda event: snake.set_direction(Direction.UP))
        root.bind('<Down>', lambda event: snake.set_direction(Direction.DOWN))
        def run_game():
            score = 0
            while True:
                try:
                    # Move the snake and update positions
                    snake.move()
                    if (snake.head_x, snake.head_y) == food.position:
                        score += 1
                        snake.grow()  # Call grow method when snake eats food
                        food.generate(snake.body)
                    # Update the canvas with snake positions
                    for segment in snake.body:
                        x, y = segment
                        grid.set_position(x, y, 'S')
                    # Display the current score
                    canvas.create_text(250, 10, text=f"Score: {score}", fill="black", font=("Arial", 16))
                    root.update_idletasks()
                    time.sleep(0.1)  # Adjust the speed of the game
                except Exception as e:
                    print(e)
                    break
            canvas.create_text(250, 300, text=f"Game Over! Score: {score}", fill="red", font=("Arial", 24))
            root.after_idle(lambda: root.quit())
        # Start the Tkinter main loop
        root.after(100, run_game)
        root.mainloop()
if __name__ == '__main__':
    Game()