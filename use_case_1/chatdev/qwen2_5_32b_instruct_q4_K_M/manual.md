Here is a detailed user manual (`manual.md`) for the Snake game built using Pygame:

---

# Snake Game User Manual

## Table of Contents
1. Introduction
2. Installation and Setup
3. How to Play
4. Main Features
5. Troubleshooting

---

## 1. Introduction

Welcome to the Snake game! This is a classic arcade-style game where you control a snake that grows longer with each food item it eats. The objective of the game is to guide the snake around a grid, consuming as much food as possible without colliding with its own body or the edges of the screen.

## 2. Installation and Setup

### Prerequisites
- Python 3.x installed on your system.
- Pygame library (required for running the game).

### Installing Dependencies
1. **Using pip**:
   ```sh
   pip install pygame
   ```

2. **Using conda**:
   ```sh
   conda install -c conda-forge pygame
   ```

### Running the Game

Once you have installed Pygame, navigate to the directory containing your Snake game files and run the following command:

```sh
python main.py
```

## 3. How to Play

### Controls
- **Move Up**: Press `W` or `Up Arrow`
- **Move Down**: Press `S` or `Down Arrow`
- **Move Left**: Press `A` or `Left Arrow`
- **Move Right**: Press `D` or `Right Arrow`

### Objective
Guide the snake to eat food items that appear randomly on the grid. Each time the snake eats a piece of food, it grows longer and your score increases.

### Game Over
The game ends when:
- The snake collides with itself.
- The snake hits the edge of the screen.

## 4. Main Features

### Grid-Based Gameplay
The game is played on a grid where each cell has a fixed size (`GRID_SIZE`).

### Snake Movement and Growth
- **Movement**: The snake moves in discrete steps, changing direction based on user input.
- **Growth**: Eating food increases the length of the snake.

### Food Placement
Food items appear randomly within the grid. If the snake eats the food, a new piece of food is placed at another random location.

### User Interface (UI)
- **Score Display**: Displays your current score in the top-left corner.
- **Game Over Screen**: Shows "Game Over!" message when the game ends.

## 5. Troubleshooting

### Common Issues
1. **Pygame Not Found**:
   - Ensure Pygame is installed using `pip install pygame`.
   
2. **Sound Files Missing**:
   - The game requires sound files (`eat_food.wav` and `game_over.wav`). If these are missing, you'll need to place them in a directory named `sounds/`.

### Additional Tips
- Make sure your Python environment has the necessary permissions to run scripts.
- Ensure that the working directory contains all required files (including the sound files).

---

Feel free to reach out if you encounter any issues or have suggestions for improving the game!

Enjoy playing Snake!

---

This manual should provide a comprehensive guide on how to install, set up, and play the Snake game. It also includes troubleshooting tips to help users resolve common issues they might face while running the game.

If you need further customization or additional features added to this manual, please let me know!