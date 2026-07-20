import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Snake and Food Classes
class Snake:
    def __init__(self):
        self.body = [(400, 300), (410, 300), (420, 300)]
        self.direction = pygame.Vector2(10, 0)

    def move(self):
        head_pos = self.body[0]
        new_head = self.direction.rotate(head_pos)
        if not self.collision(new_head):
            self.body.insert(0, tuple(new_head))
            if len(self.body) > len(snake.body):
                self.body.pop()

    def collision(self, pos):
        return any(pos == b for b in self.body[1:])


class Food:
    def __init__(self):
        self.pos = (pygame.display.get_surface().get_width() // 2, pygame.display.get_surface().get_height() // 2)

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.pos, (10, 10)))


# Initialize Snake and Food
snake = Snake()
food = Food()

clock = pygame.time.Clock()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the snake
        snake.move()

        # Check for collision with food
        if snake.body[0] == food.pos:
            food.pos = (pygame.display.get_surface().get_width() // 2, pygame.display.get_surface().get_height() // 2)
            snake.body.append(snake.body[-1])

        screen.fill(BLACK)
        snake.draw()
        food.draw()
        pygame.display.flip()

        clock.tick(10)  # Limit the frame rate to 10 FPS for simplicity

    pygame.quit()


if __name__ == "__main__":
    main()