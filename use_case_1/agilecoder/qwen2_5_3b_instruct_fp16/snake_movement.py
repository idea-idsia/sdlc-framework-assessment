'''
This file handles the movement of the snake using arrow keys.
'''
import keyboard
def move_snake(direction):
    '''Move the snake according to the given direction.'''
    global snake_positions, new_direction
    if direction == 'left':
        new_direction = 'left'
        for i in range(SNAKE_LENGTH - 1, 0, -1): # Update positions from tail to head
            snake_positions[i] = (snake_positions[i - 1][0], snake_positions[i - 1][1])
    elif direction == 'right':
        new_direction = 'right'
        for i in range(SNAKE_LENGTH):
            snake_positions[i] = (snake_positions[i + 1][0], snake_positions[i + 1][1]) # Update positions from head to tail
    elif direction == 'up':
        new_direction = 'up'
        for i in range(0, SNAKE_LENGTH - 1): 
            snake_positions[i] = (snake_positions[i + 1][0], snake_positions[i + 1][1])
    elif direction == 'down':
        new_direction = 'down'
        for i in range(SNAKE_LENGTH):
            snake_positions[i] = (snake_positions[i - 1][0], snake_positions[i - 1][1]) # Update positions from head to tail
new_direction = INITIAL_DIRECTION
initialize_snake()
while True:
    if keyboard.is_pressed('right'):
        move_snake(new_direction)
    elif keyboard.is_pressed('left'):
        move_snake(new_direction)
    elif keyboard.is_pressed('up'):
        move_snake(new_direction)
    elif keyboard.is_pressed('down'):
        move_snake(new_direction)