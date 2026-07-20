'''
Snake class to represent the snake in the game.
'''
import pygame
from colors import GREEN, RED  # Import colors from new module
class Snake:
    def __init__(self, grid):
        self.grid = grid
        self.body = [(grid.width // 2, grid.height // 2)]
        self.direction = pygame.K_RIGHT  # Initial direction
    def move(self, food):
        if self.direction == pygame.K_UP:
            new_head = (self.body[0][0], self.body[0][1] - 1)
        elif self.direction == pygame.K_DOWN:
            new_head = (self.body[0][0], self.body[0][1] + 1)
        elif self.direction == pygame.K_LEFT:
            new_head = (self.body[0][0] - 1, self.body[0][1])
        elif self.direction == pygame.K_RIGHT:
            new_head = (self.body[0][0] + 1, self.body[0][1])
        self.body.insert(0, new_head)
        if not self.eat_food(food):
            self.body.pop()
    def change_direction(self, key):
        opposite_directions = {
            pygame.K_UP: pygame.K_DOWN,
            pygame.K_DOWN: pygame.K_UP,
            pygame.K_LEFT: pygame.K_RIGHT,
            pygame.K_RIGHT: pygame.K_LEFT
        }
        if key in opposite_directions and opposite_directions[key] != self.direction:
            self.direction = key
    def eat_food(self, food):
        return self.body[0] == food.position
    def check_collision(self):
        head_x, head_y = self.body[0]
        # Check for collision with walls
        if head_x < 0 or head_x >= self.grid.width or head_y < 0 or head_y >= self.grid.height:
            return True
        # Check for collision with itself
        if self.body[0] in self.body[1:]:
            return True
        return False
    def draw(self, screen, cell_size):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN,
                             (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))