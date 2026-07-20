'''
Snake class to handle the snake's movement and drawing.
Manages the position of the snake and its direction.
'''
import pygame
class Snake:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.length = 1
        self.positions = [(0, 0)]
        self.direction = (1, 0)
    def move(self):
        head_x, head_y = self.positions[0]
        new_direction = self.direction
        new_head_x = (head_x + new_direction[0] * self.grid_size) % (600 // self.grid_size)
        new_head_y = (head_y + new_direction[1] * self.grid_size) % (600 // self.grid_size)
        new_head_pos = (new_head_x, new_head_y)
        if new_head_pos in self.positions:
            return False
        self.positions.insert(0, new_head_pos)
        if len(self.positions) > self.length:
            self.positions.pop()
        return True
    def change_direction(self, new_direction):
        x, y = new_direction
        if (x, y) != (-self.direction[0], -self.direction[1]):
            self.direction = (x, y)
    def draw(self, screen):
        for position in self.positions:
            rect = pygame.Rect(position[0] * self.grid_size, position[1] * self.grid_size, self.grid_size, self.grid_size)
            pygame.draw.rect(screen, COLORS['GREEN'], rect)