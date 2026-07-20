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