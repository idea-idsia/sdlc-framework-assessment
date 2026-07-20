'''
Utility functions for drawing and animations.
'''
import pygame
def draw_text(screen, text, color, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))
def handle_animations(screen, cell_size, snake, food):
    if 'food_eaten' in dir(food) and food.food_eaten:
        draw_text(screen, "Food Eaten!", (0, 255, 0), 36, 10, SCREEN_HEIGHT // 2)