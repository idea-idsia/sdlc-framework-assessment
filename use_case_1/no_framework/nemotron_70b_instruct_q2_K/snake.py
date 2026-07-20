class Snake:
    def __init__(self, initial_length, starting_position, direction):
        self.body = [(starting_position[0] - i, starting_position[1]) for i in range(initial_length)]
        self.direction = direction

    def update(self, game_board, food):
        head = self.body[-1]
        if self.direction == 'RIGHT':
            new_head = (head[0] + 1, head[1])
        # ... implement other directions ...
        self.body.append(new_head)
        if self.body[-1] == food.position:
            food.generate(game_board, self)
            self.grow()
        else:
            self.body.pop(0)

    def change_direction(self, direction):
        # ... implement direction changes ...

    def is_collision(self):
        head = self.body[-1]
        if (head[0] < 0 or head[0] >= game_board.width or
            head[1] < 0 or head[1] >= game_board.height or
            head in self.body[:-1]):
            return True
        return False

    def grow(self):
        # ... implement snake growth ...