"""
Snake Class
"""
import pygame
class Snake:
    def __init__(self, game_board):
        self.game_board = game_board
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = "right"
        self.screen = game_board.screen
    def draw(self):
        for segment in self.body:
            rect = pygame.Rect(segment[0] * 20, segment[1] * 20, 20, 20)
            pygame.draw.rect(self.screen, (0, 255, 0), rect)  # Green snake
    def update(self):
        head_position = self.body[0]
        new_head = None
        if self.direction == "right":
            new_head = (head_position[0] + 1, head_position[1])
        elif self.direction == "left":
            new_head = (head_position[0] - 1, head_position[1])
        elif self.direction == "down":
            new_head = (head_position[0], head_position[1] + 1)
        elif self.direction == "up":
            new_head = (head_position[0], head_position[1] - 1)
        # Check if the snake hits the boundary
        grid_dimensions = self.game_board.grid_dimensions
        if not (0 <= new_head[0] < grid_dimensions[0]) or not (0 <= new_head[1] < grid_dimensions[1]):
            raise ValueError("Snake hit the boundary")
        # Update the body
        self.body.insert(0, new_head)
        if len(self.body) > 3:  # Temporary growth logic for demonstration
            self.body.pop()
    def set_direction(self, direction):
        self.direction = direction
    def grow(self):
        self.body.append((self.body[-1][0], self.body[-1][1]))  # Grow the snake by appending a new segment at tail