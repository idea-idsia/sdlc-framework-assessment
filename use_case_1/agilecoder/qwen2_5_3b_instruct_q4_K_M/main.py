def play_snake_game():
    """
    A function to initialize and run the snake game.
    """
    # Initialize variables
    width, height = 20, 15
    grid = [[' '] * width for _ in range(height)]
    # Initial position of the head of the snake
    x, y = width // 2 - 1, height // 2
    direction = 'right'
    snake = [(x, y)]
    # Randomly place food on the board
    def spawn_food(grid):
        empty_cells = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == ' ':
                    empty_cells.append((i, j))
        x, y = random.choice(empty_cells)
        grid[x][y] = '*'
    spawn_food(grid)
    # Function to update the position of snake
    def move_snake(snake):
        new_head = None
        if direction == 'up':
            new_head = (snake[0][0], max(0, snake[0][1] - 1))
        elif direction == 'down':
            new_head = (snake[0][0], min(len(grid)-1, snake[0][1] + 1))
        elif direction == 'left':
            new_head = (max(0, snake[0][0] - 1), snake[0][1])
        else:  # right
            new_head = (min(len(grid[0])-1, snake[0][0] + 1), snake[0][1])
        return new_head
    # Main game loop
    while True:
        # Clear the screen
        clear()
        # Draw grid and snake
        for i in range(height):
            print(' '.join(grid[i]))
        if len(snake) > 1 and (snake[-1][0], snake[-1][1]) not in snake[:-1]:
            snake.pop(0)
        if move_snake(snake) in snake or \
           any(move_snake(snake)[0] < 0 or move_snake(snake)[0] >= len(grid[0]) or \
               move_snake(snake)[1] < 0 or move_snake(snake)[1] >= len(grid)):
            print("Game Over!")
            break
        if grid[move_snake(snake)[0]][move_snake(snake)[1]] == '*':
            snake.append(move_snake(snake))
            spawn_food(grid)
        else:
            snake.append(move_snake(snake))
if __name__ == "__main__":
    play_snake_game()