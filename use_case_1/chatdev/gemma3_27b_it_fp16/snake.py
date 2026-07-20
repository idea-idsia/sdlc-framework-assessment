'''
Represents the snake in the game.
'''
import pygame
class Snake:
    def __init__(self, width, height):
        """
        Initializes the snake.
        Args:
            width: The width of the game screen.
            height: The height of the game screen.
        """
        self.width = width
        self.height = height
        self.body = [pygame.Rect(50, 50, 20, 20)]
        self.direction = "right"  # Initial direction
    def move(self):
        """
        Moves the snake in its current direction.
        """
        head = self.body[0]
        if self.direction == "right":
            new_head = pygame.Rect(head.x + 20, head.y, 20, 20)
        elif self.direction == "left":
            new_head = pygame.Rect(head.x - 20, head.y, 20, 20)
        elif self.direction == "up":
            new_head = pygame.Rect(head.x, head.y - 20, 20, 20)
        elif self.direction == "down":
            new_head = pygame.Rect(head.x, head.y + 20, 20, 20)
        self.body.insert(0, new_head)
        self.body.pop()  # Remove the last segment to maintain length
    def grow(self):
        """
        Grows the snake by adding a segment.
        """
        head = self.body[0]
        if self.direction == "right":
            new_segment = pygame.Rect(head.x + 20, head.y, 20, 20)
        elif self.direction == "left":
            new_segment = pygame.Rect(head.x - 20, head.y, 20, 20)
        elif self.direction == "up":
            new_segment = pygame.Rect(head.x, head.y - 20, 20, 20)
        elif self.direction == "down":
            new_segment = pygame.Rect(head.x, head.y + 20, 20, 20)
        self.body.insert(0, new_segment)
    def check_wall_collision(self):
        """
        Checks if the snake has collided with the walls.
        """
        head = self.body[0]
        if head.x < 0 or head.x >= self.width or head.y < 0 or head.y >= self.height:
            return True
        return False
    def check_self_collision(self):
        """
        Checks if the snake has collided with itself.
        """
        head = self.body[0]
        for i in range(1, len(self.body)):
            if head.colliderect(self.body[i]):
                return True
        return False
    def change_direction(self, new_direction):
        """
        Changes the direction of the snake, preventing it from moving directly backwards.
        """
        if new_direction != self.direction:
            if self.direction == "right" and new_direction == "left":
                pass
            elif self.direction == "left" and new_direction == "right":
                pass
            elif self.direction == "up" and new_direction == "down":
                pass
            elif self.direction == "down" and new_direction == "up":
                pass
            else:
                self.direction = new_direction