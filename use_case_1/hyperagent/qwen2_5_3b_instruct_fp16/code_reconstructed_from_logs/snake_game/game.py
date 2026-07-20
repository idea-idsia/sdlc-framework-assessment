grid_size=10
def initialize_game():
    global board, snake_head, snake_direction, snake_body, food_position

    # Initialize game board
    board = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    # Snake Initialization
    snake_head = [5, 5]  # Starting position
    snake_direction = 'right'  # Initial direction (for simplicity, we start moving right)
    snake_body = [[5, 4], [5, 3]]  # Initial snake body segments

    # Food Generation
    food_position = [np.random.randint(0, grid_size), np.random.randint(0, grid_size)]
    while any(food_position == segment for segment in snake_body):
        food_position = [np.random.randint(0, grid_size), np.random.randint(0, grid_size)]

initialize_game()

# Display the initial game board
print("\n".join([''.join(row) for row in board]))