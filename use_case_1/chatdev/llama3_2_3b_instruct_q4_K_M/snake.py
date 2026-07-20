class Snake:
    # ...
    def update(self):
        # Update snake position based on direction
        if self.direction == "right":
            self.x += 10
        elif self.direction == "left":
            self.x -= 10
        elif self.direction == "up":
            self.y -= 10
        elif self.direction == "down":
            self.y += 10
    def draw(self, canvas):
        # Draw snake body on canvas.
        for point in self.body:
            x1 = int(point[0])
            y1 = int(point[1])
            if (x1 >= 0 and x1 < canvas.width // 50) and \
               (y1 >= 0 and y1 < canvas.height // 50):
                canvas.create_oval(x1, y1, x1 + 5, y1 + 5)
    def reset_position(self):
        # Update snake position based on direction
        if self.direction == "right":
            self.x += 10
        elif self.direction == "left":
            self.x -= 10
        elif self.direction == "up":
            self.y -= 10
        elif self.direction == "down":
            self.y += 10