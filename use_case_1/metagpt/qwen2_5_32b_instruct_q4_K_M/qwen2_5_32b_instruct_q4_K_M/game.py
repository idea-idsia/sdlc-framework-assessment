## game.py

import random
import pygame


class Food:
    def __init__(self):
        self.position = (0, 0)
    
    def randomize_position(self, snake_segments: list[tuple[int, int]], width: int = 1000, height: int = 600) -> None:
        """
        Randomizes the position of the food on the screen.
        
        :param snake_segments: List of tuples representing the segments of the snake to avoid placing food on.
        :param width: The width of the game window.
        :param height: The height of the game window.
        """
        while True:
            x = random.randint(0, (width // 20) - 1) * 20
            y = random.randint(0, (height // 20) - 1) * 20
            if (x, y) not in snake_segments:
                self.position = (x, y)
                break


class Snake:
    def __init__(self, start_pos: tuple[int, int], start_direction: tuple[int, int]):
        """
        Initializes the snake with a starting position and direction.
        
        :param start_pos: The initial position of the snake's head.
        :param start_direction: The initial direction in which the snake is moving.
        """
        self.segments = [start_pos]
        self.direction = start_direction
    
    def move(self, direction: tuple[int, int]) -> None:
        """
        Moves the snake one step in the given direction and updates its segments.
        
        :param direction: The direction to move the snake.
        """
        head_x, head_y = self.segments[0]
        dx, dy = direction
        new_head = (head_x + dx * 20, head_y + dy * 20)
        self.segments.insert(0, new_head)
        self.segments.pop()
    
    def grow(self) -> None:
        """
        Grows the snake by adding a segment at its current tail position.
        """
        last_segment = self.segments[-1]
        self.segments.append(last_segment)


class Game:
    def __init__(self, width: int = 1000, height: int = 600):
        """
        Initializes the game with given dimensions and creates snake and food objects.
        
        :param width: The width of the game window.
        :param height: The height of the game window.
        """
        self.width = width
        self.height = height
        self.snake = Snake((20, 20), (1, 0))
        self.food = Food()
        self.food.randomize_position(self.snake.segments, width=self.width, height=self.height)
    
    def run(self) -> None:
        """
        Main game loop that handles events and updates the game state.
        """
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        
        clock = pygame.time.Clock()
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.snake.move((0, -1))
            elif keys[pygame.K_DOWN]:
                self.snake.move((0, 1))
            elif keys[pygame.K_LEFT]:
                self.snake.move((-1, 0))
            elif keys[pygame.K_RIGHT]:
                self.snake.move((1, 0))
            
            if self.check_collision():
                running = False
            
            screen.fill((0, 0, 0))  # Fill the screen with black
            pygame.draw.rect(screen, (255, 0, 0), (*self.food.position, 20, 20))  # Draw food
            for segment in self.snake.segments:
                pygame.draw.rect(screen, (0, 255, 0), (*segment, 20, 20))  # Draw snake
            
            if self.snake.segments[0] == self.food.position:  # Check if the snake ate food
                self.snake.grow()
                self.food.randomize_position(self.snake.segments, width=self.width, height=self.height)
            
            pygame.display.flip()  # Update display
            clock.tick(10)  # Cap frame rate to 10 FPS
        
        pygame.quit()
    
    def check_collision(self) -> bool:
        """
        Checks if the snake has collided with itself or the walls.
        
        :return: True if there is a collision, False otherwise.
        """
        head_x, head_y = self.snake.segments[0]
        return (head_x < 0 or head_x >= self.width or
                head_y < 0 or head_y >= self.height or
                len(set(self.snake.segments)) != len(self.snake.segments))
