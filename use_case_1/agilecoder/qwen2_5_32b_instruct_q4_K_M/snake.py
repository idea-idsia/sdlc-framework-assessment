'''
The Snake class represents the snake in the Snake game.
It handles the movement, drawing, growing, and resetting of the snake.
'''
import pygame
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
class Snake:
    def __init__(self, start_x=400, start_y=300):
        self.length = 1
        self.positions = [(start_x, start_y)]  # Starting in the middle of screen
        self.direction = 'RIGHT'
        # Initial movement to ensure continuous motion from the beginning.
        self.move(None)
    def move(self, food_position=None):
        head_x, head_y = self.get_head_position()
        if self.direction == 'UP':
            new_head_pos = (head_x, head_y - 10)
        elif self.direction == 'DOWN':
            new_head_pos = (head_x, head_y + 10)
        elif self.direction == 'LEFT':
            new_head_pos = (head_x - 10, head_y)
        else:  # RIGHT
            new_head_pos = (head_x + 10, head_y)
        self.positions.insert(0, new_head_pos)  
        if food_position and new_head_pos != food_position:
            self.positions.pop()
    def get_head_position(self):
        return self.positions[0]
    def change_direction(self, direction):
        self.direction = direction
    def grow(self):
        tail_x, tail_y = self.positions[-1]
        if self.direction == 'UP':
            new_tail_pos = (tail_x, tail_y + 10)
        elif self.direction == 'DOWN':
            new_tail_pos = (tail_x, tail_y - 10)
        elif self.direction == 'LEFT':
            new_tail_pos = (tail_x + 10, tail_y)
        else: # RIGHT
            new_tail_pos = (tail_x - 10, tail_y)
        self.positions.append(new_tail_pos)
    def reset_snake(self):
        self.length = 1
        self.positions = [(400, 300)]
        self.direction = 'RIGHT'
        # Ensure initial movement after reset.
        self.move(None)
    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, WHITE, [p[0], p[1], 10, 10]) # White color