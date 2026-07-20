class Snake:
    def __init__(self):
        self.position = [(0, 0)]  # Initial position
        self.length = 1  # Initial length
        self.direction = "right"  # Initial direction

    def move(self):
        head_x, head_y = self.position[0]

        if self.direction == "right":
            new_head = (head_x + 1, head_y)
        elif self.direction == "left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "down":
            new_head = (head_x, head_y + 1)

        self.position.insert(0, new_head)  # Add new head
        self.position.pop()  # Remove tail