import tkinter as tk
from random import randint

# Constants
GRID_SIZE = 20
SNAKE_LENGTH = 5
FOOD_COLOR = 'red'
BODY_PARTS = []
DIRECTIONS = {'UP': (0, -1), 'DOWN': (0, 1), 'LEFT': (-1, 0), 'RIGHT': (1, 0)}
SPEED = 150

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=GRID_SIZE * 20, height=GRID_SIZE * 20, bg='black')
        self.canvas.pack()

        # Set initial snake direction to right
        self.direction = 'RIGHT'

        # Create snake and food
        self.snake_x = [5] * SNAKE_LENGTH
        self.snake_y = [10] * SNAKE_LENGTH
        self.food_x, self.food_y = 12, 10

        for x, y in zip(self.snake_x, self.snake_y):
            BODY_PARTS.append(self.canvas.create_rectangle(x * GRID_SIZE, y * GRID_SIZE,
                                                          (x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE, fill='green'))

        # Create food
        self.canvas.create_rectangle(self.food_x * GRID_SIZE, self.food_y * GRID_SIZE,
                                     (self.food_x + 1) * GRID_SIZE, (self.food_y + 1) * GRID_SIZE, fill=FOOD_COLOR)

        # Bind keypress events to change the snake direction
        root.bind('<KeyPress-Up>', lambda event: self.change_direction('UP'))
        root.bind('<KeyPress-Down>', lambda event: self.change_direction('DOWN'))
        root.bind('<KeyPress-Left>', lambda event: self.change_direction('LEFT'))
        root.bind('<KeyPress-Right>', lambda event: self.change_direction('RIGHT'))

        # Game loop
        self.root.after(SPEED, self.update)

    def change_direction(self, direction):
        if (direction == 'UP' and self.direction != 'DOWN') or \
           (direction == 'DOWN' and self.direction != 'UP') or \
           (direction == 'LEFT' and self.direction != 'RIGHT') or \
           (direction == 'RIGHT' and self.direction != 'LEFT'):
            self.direction = direction

    def update(self):
        # Update snake position
        head_x = BODY_PARTS[0].x1 // GRID_SIZE + DIRECTIONS[self.direction][0]
        head_y = BODY_PARTS[0].y1 // GRID_SIZE + DIRECTIONS[self.direction][1]

        if (head_x, head_y) == (self.food_x, self.food_y):
            # Snake eats food
            BODY_PARTS.append(self.canvas.create_rectangle(head_x * GRID_SIZE, head_y * GRID_SIZE,
                                                          (head_x + 1) * GRID_SIZE, (head_y + 1) * GRID_SIZE, fill='green'))
            self.score += 1

            # Generate new food position
            while True:
                self.food_x = randint(0, 29)
                self.food_y = randint(0, 19)
                if not any((self.food_x == x and self.food_y == y for x, y in BODY_PARTS)):
                    break

        # Update snake body
        for i, part in enumerate(BODY_PARTS):
            new_x = (BODY_PARTS[i].x1 // GRID_SIZE + DIRECTIONS[self.direction][0]) % 30
            new_y = (BODY_PARTS[i].y1 // GRID_SIZE + DIRECTIONS[self.direction][1]) % 20

            BODY_PARTS[i] = self.canvas.coords(part, new_x * GRID_SIZE, new_y * GRID_SIZE,
                                              (new_x + 1) * GRID_SIZE, (new_y + 1) * GRID_SIZE)

        # Check for collision with boundaries
        if head_x < 0 or head_x >= 30 or head_y < 0 or head_y >= 20:
            self.game_over()

        # Check for collision with itself
        for body_part in BODY_PARTS[1:]:
            if (head_x, head_y) == (body_part.x1 // GRID_SIZE, body_part.y1 // GRID_SIZE):
                self.game_over()

        # Redraw food and score
        self.canvas.create_rectangle(self.food_x * GRID_SIZE, self.food_y * GRID_SIZE,
                                     (self.food_x + 1) * GRID_SIZE, (self.food_y + 1) * GRID_SIZE, fill=FOOD_COLOR)

        # Game loop continues
        self.root.after(SPEED, self.update)

    def game_over(self):
        for body_part in BODY_PARTS:
            self.canvas.delete(body_part)
        score_text = self.canvas.create_text(200, 100, text=f"Game Over! Score: {self.score}", fill="white", font=('Helvetica', 24))
        self.root.after(SPEED * 3, lambda: self.restart(score_text))

    def restart(self, score_text):
        # Clear the canvas and reset game state
        for body_part in BODY_PARTS:
            self.canvas.delete(body_part)
        self.score = 0

        # Create snake and food again
        self.snake_x = [5] * SNAKE_LENGTH
        self.snake_y = [10] * SNAKE_LENGTH
        for x, y in zip(self.snake_x, self.snake_y):
            BODY_PARTS.append(self.canvas.create_rectangle(x * GRID_SIZE, y * GRID_SIZE,
                                                          (x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE, fill='green'))
        self.food_x, self.food_y = 12, 10
        self.canvas.create_rectangle(self.food_x * GRID_SIZE, self.food_y * GRID_SIZE,
                                     (self.food_x + 1) * GRID_SIZE, (self.food_y + 1) * GRID_SIZE, fill=FOOD_COLOR)

# Create the main window and start the game
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()