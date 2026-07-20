import random
import pygame
class Food:
    def __init__(self, screen):
        self.screen = screen
        self.food_position = (random.randint(0, 39) * 20, random.randint(0, 29) * 20)
    def generate_new_food(self, snake_body):
        while True:
            new_position = (random.randint(0, 39) * 20, random.randint(0, 29) * 20)
            if new_position not in snake_body:
                self.food_position = new_position
                break
    def draw_food(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.food_position[0], self.food_position[1], 20, 20))