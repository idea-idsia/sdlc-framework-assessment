class Food:
    def __init__(self):
        # Initialize food position randomly
        self.x = random.randint(0, 9)
        self.y = random.randint(0, 9)
    def update(self):
        # Update food position randomly
        if random.random() < 0.1:
            self.x = random.randint(0, 9)
            self.y = random.randint(0, 9)