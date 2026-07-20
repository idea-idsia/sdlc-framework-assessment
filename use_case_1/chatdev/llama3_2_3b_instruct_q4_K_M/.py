def update(self):
    # Update snake position based on direction
    if self.snake.direction == "right":
        self.snake.x += 10
    elif self.snake.direction == "left":
        self.snake.x -= 10
    elif self.snake.direction == "up":
        self.snake.y -= 10
    elif self.snake.direction == "down":
        self.snake.y += 10
    # Update food position randomly
    if random.random() < 0.1:
        self.food.x = random.randint(0, 9)
        self.food.y = random.randint(0, 9)
def draw(self):
    # Draw game board and objects on canvas
    self.board.draw_board()
    self.snake.draw(self.canvas)
    self.food.draw(self.canvas)