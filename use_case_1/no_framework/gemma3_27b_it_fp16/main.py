import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Define grid size and block size
grid_size = 20
block_size = 20

# Define screen dimensions
screen_width = 600
screen_height = 400

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Define snake initial position and length
snake_x = grid_size * block_size / 2
snake_y = grid_size * block_size / 2
snake_list = []
snake_length = 1

# Define food position
food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

# Define initial direction
direction = "RIGHT"

# Define clock for controlling game speed
clock = pygame.time.Clock()

# Define font for displaying score
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# Function to display score
def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])


# Function to draw the snake
def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], block_size, block_size])


# Function to display game over message
def game_over_message(score):
    my_font = pygame.font.SysFont("times new roman", 50)
    message = my_font.render("Game Over!", True, red)
    screen.blit(message, [screen_width / 6, screen_height / 3])

    score_font = pygame.font.SysFont("comicsansms", 35)
    value = score_font.render("Your Score: " + str(score), True, white)
    screen.blit(value, [screen_width / 6, screen_height / 3 + 50])

    restart_font = pygame.font.SysFont("times new roman", 30)
    restart_message = restart_font.render("Press 'R' to restart or 'Q' to quit", True, white)
    screen.blit(restart_message, [screen_width / 6, screen_height / 3 + 100])


# Game loop
def gameLoop():
    game_over = False
    game_close = False
    score = 0

    # Initial Snake Position
    snake_x = grid_size * block_size / 2
    snake_y = grid_size * block_size / 2
    snake_list = []
    snake_length = 1
    direction = "RIGHT"

    # Initial Food Position
    food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

    while not game_over:

        while game_close == True:
            screen.fill(black)
            game_over_message(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "LEFT"
                if event.key == pygame.K_RIGHT:
                    direction = "RIGHT"
                if event.key == pygame.K_UP:
                    direction = "UP"
                if event.key == pygame.K_DOWN:
                    direction = "DOWN"

        if direction == "LEFT":
            snake_x -= block_size
        if direction == "RIGHT":
            snake_x += block_size
        if direction == "UP":
            snake_y -= block_size
        if direction == "DOWN":
            snake_y += block_size

        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for self-collision
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Check for boundary collision
        if snake_x < 0 or snake_x >= screen_width or snake_y < 0 or snake_y >= screen_height:
            game_close = True

        # Check for food collision
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
            snake_length += 1
            score += 10

        draw_snake(block_size, snake_list)
        display_score(score)
        pygame.display.update()
        clock.tick(15)  # Adjust for game speed
    pygame.quit()
    quit()


# Start the game
gameLoop()