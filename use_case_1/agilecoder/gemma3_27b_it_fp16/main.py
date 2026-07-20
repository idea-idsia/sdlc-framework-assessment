'''
Main file for the Snake game.
Initializes the game and runs the main loop.
'''
import tkinter as tk
import snake
import food
class Game:
    def __init__(self, grid_width, grid_height, initial_direction="right"):
        '''
        Initializes the game with grid dimensions and initial direction.
        '''
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.snake = snake.Snake((grid_width // 2, grid_height // 2), 3)
        self.food = food.Food(grid_width, grid_height)
        self.score = 0
        self.game_over_flag = False
        self.direction = initial_direction
    def run(self, master):
        '''
        Sets up the Tkinter window, binds key events, and starts the game loop.
        '''
        self.master = master
        master.title("Snake Game")
        self.canvas = tk.Canvas(master, width=self.grid_width * 20, height=self.grid_height * 20, bg="white")
        self.canvas.pack()
        self.master.bind("<Key>", self.handle_key)
        self.update_display()
        self.game_loop()
    def handle_key(self, event):
        '''
        Handles key presses to change the snake's direction.
        '''
        if event.keysym == "Up":
            self.direction = "up"
        elif event.keysym == "Down":
            self.direction = "down"
        elif event.keysym == "Left":
            self.direction = "left"
        elif event.keysym == "Right":
            self.direction = "right"
    def update_display(self):
        '''
        Updates the canvas with the current game state.
        '''
        self.canvas.delete("all")  # Clear the canvas
        # Draw the snake
        for x, y in self.snake.get_body():
            self.canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="green")
        # Draw the food
        x, y = self.food.get_position()
        self.canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="red")
        # Display the score
        self.canvas.create_text(10, 10, text=f"Score: {self.score}", fill="black")
        if self.game_over_flag:
            self.canvas.create_text(self.grid_width * 10, self.grid_height * 10, text="Game Over!", fill="black", font=("Arial", 20))
    def game_loop(self):
        '''
        Updates the game state and redraws the canvas.
        '''
        self.update()
        self.master.after(100, self.game_loop)
    def update(self):
        '''
        Updates the snake's position and checks for collisions.
        '''
        if self.game_over_flag:
            return
        self.snake.move(self.direction)
        if self.snake.check_collision(self.grid_width, self.grid_height):
            self.game_over_flag = True
            return
        if self.snake.get_head_position() == self.food.get_position():
            self.snake.grow()
            self.food.position = self.food.generate_new_position(self.snake.get_body())
            self.score += 1
if __name__ == '__main__':
    root = tk.Tk()
    game = Game(20, 20)  # Pass grid dimensions to the constructor
    game.run(root)  # Pass the Tk root window to the run method
    root.mainloop()