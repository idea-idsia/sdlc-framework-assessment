'''
Contains display functions for the Snake Game.
Handles drawing the snake, food, and game over screen.
'''
import pygame
from constants import *
def draw_game(screen, width, height, snake, food_position):
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN,
                         (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED,
                     (food_position[0] * CELL_SIZE, food_position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    # Adding text for instructions and score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: {}".format(len(snake) - 3), True, WHITE)
    screen.blit(text, (50, 10))
    text_instructions = font.render("Use arrow keys to move", True, WHITE)
    screen.blit(text_instructions, (width * CELL_SIZE // 2 - 7 * len('Use arrow keys to move'), 10))
def draw_game_over(screen, width, height):
    gameover_font = pygame.font.Font(None, 48)
    text = gameover_font.render("Game Over", True, WHITE)
    screen.blit(text, (width * CELL_SIZE // 2 - len('Game Over')*15, height * CELL_SIZE // 2))
    restart_text = gameover_font.render("Press 'R' to Restart", True, WHITE)
    screen.blit(restart_text, (width * CELL_SIZE // 2 - len('Press R to Restart')*8, height * CELL_SIZE // 2 + 50))