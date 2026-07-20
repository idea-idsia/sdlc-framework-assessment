import random
import time
import msvcrt  # For Windows-based systems

# Game constants
BOARD_WIDTH = 10
BOARD_HEIGHT = 10
SNAKE_INITIAL_LENGTH = 3
DELAY = 0.15  # Lower value for faster speed


def main():
    # Initialize game variables
    snake = [(5, 5), (5, 4), (5, 3)]  # Snake starts in the middle
    food = None
    direction = 'right'
    score = 0
    game_over = False

    def generate_food():
        nonlocal food
        while True:
            food = (random.randint(0, BOARD_HEIGHT - 1), random.randint(0, BOARD_WIDTH - 1))
            if food not in snake:
                break

    def draw_board():
        # Clear the screen
        print('\n' * 50)

        # Draw score
        print(f"Score: {score}")
        print("Press Space to restart | Esc to exit")
        print("-" * (BOARD_WIDTH * 2 + 1))

        # Create a board filled with empty spaces
        board = [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

        # Draw snake
        for i, segment in enumerate(snake):
            y, x = segment
            if i == 0:
                board[y][x] = 'O'  # Head of the snake
            else:
                board[y][x] = '#'  # Body of the snake

        # Draw food
        if food is not None:
            y, x = food
            board[y][x] = 'F'

        # Print the board
        for row in board:
            print('|' + '|'.join(row) + '|')
        print("-" * (BOARD_WIDTH * 2 + 1))

    def change_direction(new_direction):
        nonlocal direction
        if new_direction == 'up' and direction != 'down':
            direction = 'up'
        elif new_direction == 'down' and direction != 'up':
            direction = 'down'
        elif new_direction == 'left' and direction != 'right':
            direction = 'left'
        elif new_direction == 'right' and direction != 'left':
            direction = 'right'

    # Main game loop
    while True:
        if not game_over:
            draw_board()

            # Generate initial food
            if food is None:
                generate_food()

            # Move snake
            head_y, head_x = snake[0]
            dy, dx = 0, 0

            if direction == 'up':
                dy = -1
            elif direction == 'down':
                dy = 1
            elif direction == 'left':
                dx = -1
            elif direction == 'right':
                dx = 1

            new_head = (head_y + dy, head_x + dx)

            # Check for collisions with walls
            if new_head[0] < 0 or new_head[0] >= BOARD_HEIGHT or new_head[1] < 0 or new_head[1] >= BOARD_WIDTH:
                game_over = True

            # Check for collisions with self
            if new_head in snake:
                game_over = True

            # Update snake position
            snake.insert(0, new_head)

            # Check if food is eaten
            if new_head == food:
                score += 1
                generate_food()
            else:
                snake.pop()  # Remove tail to maintain length

            time.sleep(DELAY)

        else:
            # Game Over screen
            print("\nGame Over!")
            print(f"Final Score: {score}")
            print("Press Space to restart | Esc to exit")

            # Wait for input
            while True:
                if msvcrt.kbhit():
                    key = ord(msvcrt.getch())
                    if key == 32:  # Space key
                        snake = [(5, 5), (5, 4), (5, 3)]
                        direction = 'right'
                        score = 0
                        game_over = False
                        break
                    elif key == 27:  # Esc key
                        return

        # Handle keyboard input for movement
        if msvcrt.kbhit():
            key = ord(msvcrt.getch())
            if key == 72:  # Up arrow
                change_direction('up')
            elif key == 80:  # Down arrow
                change_direction('down')
            elif key == 75:  # Left arrow
                change_direction('left')
            elif key == 77:  # Right arrow
                change_direction('right')


if __name__ == "__main__":
    main()