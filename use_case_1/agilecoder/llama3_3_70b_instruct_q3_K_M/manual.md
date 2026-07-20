# Snake Game Manual
## Introduction
The Snake game is a classic game where the player controls a snake that moves around the screen, eating food and growing in length. The game ends when the snake collides with the boundaries or its own body.

## Installation
To play the game, you need to have Python and the Pygame library installed on your computer. You can install Pygame by running the following command in your terminal:
```bash
pip install pygame
```
## Game Overview
The game is played on a 10x10 grid, where the snake moves around and eats food. The player can control the snake using the arrow keys.

## Main Functions
* **Game Board**: The game board is a 10x10 grid where the snake moves around.
* **Snake Initialization**: The snake starts at a random position on the game board with an initial length of 3 units.
* **Snake Movement**: The snake moves continuously in the chosen direction (up, down, left, or right) until the player changes the direction using the arrow keys.
* **Food Generation**: Food is generated at random positions on the game board, and the snake can eat it to grow in length.
* **Collision Handling**: The game checks for collisions between the snake and the boundaries, as well as collisions between the snake's head and its own body.
* **Score Display**: The current score (i.e., the length of the snake) is displayed on the screen.

## How to Play
1. Run the game by executing the `main.py` file.
2. Use the arrow keys to control the snake's direction.
3. Eat food to grow in length and increase your score.
4. Avoid colliding with the boundaries or your own body.

## Game Over Condition
The game ends when the snake collides with the boundaries or its own body. When this happens, a "Game Over" message is displayed on the screen, and you can restart the game by pressing the Space bar or quit the game by pressing the Esc key.

## Requirements
* Python 3.x
* Pygame library (version 2.0.0 or later)

## Troubleshooting
If you encounter any issues while playing the game, make sure that you have the latest version of Pygame installed and that your Python environment is properly configured. If you still experience problems, feel free to reach out to us for support.