'''
Contains core logic for the Snake Game. 
Handles the initialization of the game board,
handling snake movement, food generation,
collision detection and more.
'''
import pygame
from constants import *
import random
class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width * CELL_SIZE, height * CELL_SIZE))
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = 'RIGHT'
        self.food_position = self.generate_food()
        self.game_over = False
    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    self.change_direction(event.key)
            if not self.game_over:
                self.move_snake()
                self.check_collisions()
            else:  # Game over state handling
                self.draw_game_over()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        self.reset_game()
            self.draw_game()  # Fix the AttributeError by adding this method.
            clock.tick(10)  # Frame rate
    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != 'DOWN':
            self.direction = 'UP'
        elif key == pygame.K_DOWN and self.direction != 'UP':
            self.direction = 'DOWN'
        elif key == pygame.K_LEFT and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif key == pygame.K_RIGHT and self.direction != 'LEFT':
            self.direction = 'RIGHT'
    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == 'UP':
            new_head = (head_x, head_y - 1)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + 1)
        elif self.direction == 'LEFT':
            new_head = (head_x - 1, head_y)
        else:
            new_head = (head_x + 1, head_y)
        self.snake.insert(0, new_head)
        if new_head != self.food_position:
            self.snake.pop()
        else:
            self.food_position = self.generate_food()
    def check_collisions(self):
        head = self.snake[0]
        if (head[0] < 0 or head[0] >= self.width
                or head[1] < 0 or head[1] >= self.height):
            self.game_over = True
        for body_part in self.snake[1:]:
            if head == body_part:
                self.game_over = True
                break
    def generate_food(self):
        while True:
            position = (random.randint(0, self.width - 1),
                        random.randint(0, self.height - 1))
            if position not in self.snake:
                return position
    def reset_game(self):
        # Reset the game state for a new round
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = 'RIGHT'
        self.food_position = self.generate_food()
        self.game_over = False
    def draw_game(self):  # Added method to fix the AttributeError.
        self.screen.fill((0, 0, 0))  # Clear screen
        for part in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0),
                             [part[0] * CELL_SIZE,
                              part[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE])
        pygame.draw.rect(self.screen, (255, 0, 0), [
                         self.food_position[0] * CELL_SIZE,
                         self.food_position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE])
    def draw_game_over(self):
        font = pygame.font.SysFont('arial', 36)
        text = font.render("Game Over! Press 'R' to restart", True, (255, 0, 0))
        self.screen.blit(text, [self.width * CELL_SIZE / 4,
                                self.height * CELL_SIZE / 3])