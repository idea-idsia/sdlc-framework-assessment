import random

class Snake:
    def __init__(self, grid_dimensions):
        self.grid_dimensions = grid_dimensions
        self.body = []
        self.direction = 'RIGHT'
        self.score = 0

    def initialize_snake(self):
        start_x, start_y = 5, 5
        for i in range(3):
            self.body.append((start_x - i, start_y))

    def move(self):
        head_x, head_y = self.body[0]

        if self.direction == 'RIGHT':
            new_head = (head_x + 1, head_y)
        elif self.direction == 'LEFT':
            new_head = (head_x - 1, head_y)
        elif self.direction == 'UP':
            new_head = (head_x, head_y - 1)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + 1)

        self.body.insert(0, new_head)
        self.body.pop()

    def change_direction(self, direction):
        if (direction == 'UP' and self.direction != 'DOWN') or \
           (direction == 'DOWN' and self.direction != 'UP') or \
           (direction == 'LEFT' and self.direction != 'RIGHT') or \
           (direction == 'RIGHT' and self.direction != 'LEFT'):
            self.direction = direction

    def eat_food(self, food_position):
        if self.body[0] == food_position:
            self.body.append(self.body[-1])
            return True
        return False

    def check_collision(self):
        head_x, head_y = self.body[0]
        if (head_x < 0 or head_x >= self.grid_dimensions[0] or
                head_y < 0 or head_y >= self.grid_dimensions[1]):
            return True
        for body_part in self.body[1:]:
            if self.body[0] == body_part:
                return True
        return False