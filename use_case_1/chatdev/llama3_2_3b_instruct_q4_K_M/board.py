class Game:
    # ...
    def update(self):
        if not self.snake.check_collision():
            return True
        self.board.reset_board()
        self.snake.update()
        self.food.update()
        # Check for boundary collisions and score updates
        if (self.snake.x < 0 or self.snake.x >= self.width // 50) or \
           (self.snake.y < 0 or self.snake.y >= self.height // 50):
            self.score -= 10
        elif self.snake.head_position in self.snake.body[:-1]:
            return False
        if random.random() < 0.1:
            self.score += 10
        # Check for food collision and score update
        if (self.snake.x == self.food.x * 50) and \
           (self.snake.y == self.food.y * 50):
            self.score += 10
            self.food.update()