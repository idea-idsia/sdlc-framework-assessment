# Snake Game User Manual

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [How to Play](#how-to-play)
5. [Game Controls](#game-controls)
6. [Game Over and Restarting](#game-over-and-restarting)
7. [Troubleshooting](#troubleshooting)

## Introduction

Welcome to the Snake Game! This is a classic grid-based game implemented in Python using the Pygame library. The objective of the game is to control a snake that moves around the screen, eats food to grow longer, and avoids colliding with the walls or itself.

## Features

- **Grid-Based Game Board:** A defined 10x10 grid displayed on the screen.
- **Snake Initialization:** The snake starts in the center of the board, moving right initially.
- **Snake Movement:** Use arrow keys to control the direction of the snake.
- **Food Generation:** Food appears at random positions and the snake grows when it eats the food.
- **Collision Handling:** Game ends if the snake collides with the boundaries or itself.
- **Score Display:** Current score is displayed on the screen.
- **Game Over Condition:** Displays a game over message and allows restarting the game.

## Installation

### Prerequisites
Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/).

### Install Dependencies
1. Clone the repository or download the project files.
2. Navigate to the project directory in your terminal or command prompt.
3. Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the required dependencies using `pip`:
    ```bash
    pip install pygame
    ```

### Alternative Installation Method

Alternatively, you can use the provided `install_requirements.txt` file to install all necessary dependencies at once:

```bash
pip install -r install_requirements.txt
```

## How to Play

1. Make sure your virtual environment is activated.
2. Run the main game script:
    ```bash
    python main.py
    ```
3. The game window will open, and the snake will start moving automatically.

## Game Controls

- **Arrow Keys:** Change the direction of the snake (up, down, left, right).

## Game Over and Restarting

When the game ends due to a collision, a "Game Over" message is displayed in red at the center of the screen. To restart the game:

1. Press the `R` key on your keyboard.
2. The game will reset to its initial state with a new random food position.

## Troubleshooting

- **No Window Appears:** Make sure you have installed Pygame correctly and are running the script in an environment that supports window creation (not all remote or headless environments can display windows).
- **Snake Moves Too Fast:** You can adjust the game speed by changing the frame rate in `main.py`:
    ```python
    pygame.time.Clock().tick(15)  # Lower this number for a slower snake, increase it for a faster one.
    ```

If you encounter any other issues or have suggestions for improvements, please feel free to submit an issue on our GitHub repository.

## Enjoy the Game!

Have fun playing the Snake Game! We hope you enjoy your experience and perhaps even create some high scores. Happy gaming!

---

This manual provides comprehensive instructions for installing, running, and playing the Snake game, ensuring that users can get started quickly and easily.