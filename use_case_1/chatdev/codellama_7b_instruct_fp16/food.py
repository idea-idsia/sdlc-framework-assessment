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