# Import necessary libraries
import pygame
import sys
import random
from gameboard import GameBoard
from snake import Snake
from food import Food
'''
This is the main file for the Snake Game implementation using Pygame.
It initializes the game, handles user input, and controls the gameplay.
'''
class SnakeGame:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        # Set up some constants
        self.width = 800
        self.height = 600
        self.block_size = 20
        # Create the game board
        self.game_board = GameBoard(self.width, self.height, self.block_size)
        # Create the snake and food
        self.snake = Snake(self.block_size)
        self.food = Food(self.block_size)
        # Set up the display
        self.display = pygame.display.set_mode((self.width, self.height))
        # Set up the clock
        self.clock = pygame.time.Clock()
        # Initialize the score
        self.score = 0
    def draw_game_board(self):
        # Draw the game board
        self.game_board.draw(self.display)
    def move_snake(self):
        # Move the snake based on user input or automatic movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.snake.move_up()
        elif keys[pygame.K_DOWN]:
            self.snake.move_down()
        elif keys[pygame.K_LEFT]:
            self.snake.move_left()
        elif keys[pygame.K_RIGHT]:
            self.snake.move_right()
        # Update the snake's head position
        self.snake.update_head()
    def generate_food(self):
        # Generate food at a random position on the game board
        self.food.generate(self.game_board.width, self.game_board.height)
    def check_collision(self):
        # Check for collisions between the snake and the game board boundaries, its own body, or the food
        if (self.snake.head[0] < 0 or self.snake.head[0] >= self.game_board.width or 
            self.snake.head[1] < 0 or self.snake.head[1] >= self.game_board.height):
            # Collision with game board boundaries
            return "game_over"
        for block in self.snake.body[:-1]:
            if block == self.snake.head:
                # Collision with snake's own body
                return "game_over"
        if self.snake.head == self.food.position:
            # Collision with food
            return "food_consumed"
    def update_score(self):
        # Update the score when the snake consumes food
        self.score += 1
    def play_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # Move the snake
            self.move_snake()
            # Check for collisions
            collision = self.check_collision()
            if collision == "game_over":
                # Display game over screen with option to restart or quit
                self.display.fill((0, 0, 0))
                font = pygame.font.Font(None, 36)
                text = font.render("Game Over! Press 'R' to restart or 'Q' to quit.", True, (255, 255, 255))
                text_rect = text.get_rect(center=(self.width / 2, self.height / 2))
                self.display.blit(text, text_rect)
                pygame.display.flip()
                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                # Restart the game by resetting all variables
                                self.snake.body = [(200, 200), (220, 200), (240, 200)]
                                self.snake.head = self.snake.body[-1]
                                self.score = 0
                                waiting = False
                            elif event.key == pygame.K_q:
                                pygame.quit()
                                sys.exit()
            elif collision == "food_consumed":
                self.update_score()
                self.generate_food()
                self.snake.grow()
            # Draw everything
            self.draw_game_board()
            for block in self.snake.body:
                pygame.draw.rect(self.display, (0, 255, 0), pygame.Rect(block[0], block[1], self.block_size, self.block_size))
            pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(self.food.position[0], self.food.position[1], self.block_size, self.block_size))
            font = pygame.font.Font(None, 36)
            text = font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.display.blit(text, (10, 10))
            pygame.display.flip()
            # Cap the frame rate
            self.clock.tick(60)
if __name__ == "__main__":
    game = SnakeGame()
    game.play_game()