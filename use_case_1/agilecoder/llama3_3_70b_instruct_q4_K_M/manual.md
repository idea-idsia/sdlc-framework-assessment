# Snake Game Manual
## Introduction
The Snake game is a classic game where the player controls a snake that moves around the screen, eating food and growing in length. The game ends when the snake collides with the wall or its own body.

## Installing Dependencies
To play the game, you need to have Python and Pygame installed on your computer. You can install Pygame by running the following command in your terminal:
```bash
pip install pygame
```
Alternatively, you can install it using conda:
```bash
conda install pygame -c conda-forge
```
## Running the Game
To run the game, navigate to the directory where the game files are located and run the following command:
```bash
python main.py
```
This will launch the game window, and you can start playing.

## Gameplay
The game is controlled using the arrow keys:

* Up arrow: Move the snake up
* Down arrow: Move the snake down
* Left arrow: Move the snake left
* Right arrow: Move the snake right

The goal is to eat the food pellets that appear on the screen. Each time you eat a food pellet, your snake will grow in length.

## Scoring
Your score is displayed at the top of the game window and increments each time you eat a food pellet.

## Game Over
The game ends when:

* The snake collides with the wall
* The snake collides with its own body

When the game ends, a "Game Over" message will be displayed on the screen.

## Restarting the Game
To restart the game, simply close the game window and run the `main.py` file again.

## Main Menu
Before starting the game, you can select a difficulty level from the main menu. The difficulty levels are:

* Easy
* Medium
* Hard

You can navigate through the options using the up and down arrow keys and select an option by pressing the return key.

## Customization
The game can be customized by modifying the `game.py` file. You can change the game board size, snake speed, and food spawn rate to create a unique gaming experience.

## Troubleshooting
If you encounter any issues while running the game, make sure that:

* Pygame is installed correctly
* The game files are in the correct directory
* The `main.py` file is run from the correct directory

If you still encounter issues, feel free to reach out to us for support.