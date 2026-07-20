class Snake:
    def __init__(self, x, y, initial_length, board=None):
        self.head = (x * 20, y * 20)
        # Define snake body positions based on the initial length
        self.body = [(0, 0)] * initial_length
        if board is None:
            raise AttributeError('board attribute not defined')
        else:
            self.board = board
    def move(self, direction):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i - 1]
        if direction == "right":
            self.head = (self.head[0] + 20, self.head[1])
        elif direction == "left":
            self.head = (self.head[0] - 20, self.head[1])
        elif direction == "up":
            self.head = (self.head[0], self.head[1] - 20)
        elif direction == "down":
            self.head = (self.head[0], self.head[1] + 20)
    def grow(self):
        new_head = self.head
        for i in range(len(self.body) - 1, 0, -1):
            new_head = self.body[i]
        self.body.insert(0, new_head)
        return new_head
    def check_collision(self):
        # Check collision with game board boundaries
        if not (0 <= self.head[0] < self.board.width and 0 <= self.head[1] < self.board.height):
            return True
        for i in range(len(self.body) - 1, 0, -1):
            if self.head == self.body[i]:
                return True
        return False