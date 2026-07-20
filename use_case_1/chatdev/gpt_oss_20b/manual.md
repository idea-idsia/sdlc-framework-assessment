# Snake Game Manual

> **Version**: 1.0.0  
> **Author**: [Your Name]  
> **Date**: 2025‑12‑03  

---

## Table of Contents

| Section | Description |
|---------|-------------|
| 1. Introduction | What the game is and why you’ll love it |
| 2. Prerequisites | What you need to run the game |
| 3. Installation | Step‑by‑step setup guide |
| 4. File Structure | What each file does |
| 5. Running the Game | How to launch and play |
| 6. Controls & Gameplay | Detailed keybindings and mechanics |
| 7. Customisation | Tweaking grid size, colours, speed |
| 8. Troubleshooting | Common issues & fixes |
| 9. Credits & License | Who made it & legal info |

---

## 1. Introduction

Welcome to the classic **Snake Game** written in **Python** using the **pygame** library.  
- Move the snake around a grid, eat food to grow longer, and try to survive as long as possible.  
- The game features smooth pixel‑based animations, a simple scoring system, and a “Game Over” screen with the option to restart.

---

## 2. Prerequisites

| Item | Minimum Version | Why |
|------|-----------------|-----|
| Python | 3.8 or newer | The project uses modern Python syntax (f‑strings, type hints). |
| pip | Comes with Python | For installing dependencies. |
| Virtual Environment (recommended) | Any | Keeps project dependencies isolated. |

---

## 3. Installation

1. **Clone the repository (or download the ZIP)**  
   ```bash
   git clone https://github.com/your‑repo/snake‑game.git
   cd snake‑game
   ```

2. **Create a virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   The project uses only `pygame`, so the `requirements.txt` is trivial.  
   ```bash
   pip install -r requirements.txt
   ```
   If you’re not using the `requirements.txt`, you can install manually:  
   ```bash
   pip install pygame
   ```

4. **Run the game**  
   ```bash
   python main.py
   ```

---

## 4. File Structure

```
snake‑game/
├─ constants.py      # Grid, screen, colour constants
├─ snake.py          # Snake class – movement, growth, animation
├─ food.py           # Food generation & visual effect
├─ game.py           # Core game loop, rendering, input handling
├─ main.py           # Entry point
└─ requirements.txt # pip dependencies
```

### `constants.py`

- Grid dimensions (`GRID_WIDTH`, `GRID_HEIGHT`)  
- Cell size (`CELL_SIZE`) – size of each square in pixels  
- Screen size calculated from grid and cell size  
- Colour tuples for rendering  

### `snake.py`

- Implements the snake as a deque of grid coordinates.  
- Handles direction changes, movement, growth flag, and pixel‑based animation for smooth motion.  

### `food.py`

- Randomly places food on an unoccupied cell.  
- Provides a fading circle effect when food is consumed.  

### `game.py`

- Main game class: initialises pygame, handles the main loop, input, collision logic, scoring, and drawing.  
- Contains `reset()` to start a new game after a “Game Over”.  

### `main.py`

- Simple bootstrap file that creates a `Game` instance and calls `run()`.

---

## 5. Running the Game

Once you’ve installed everything, simply run:

```bash
python main.py
```

A window titled **“Snake Game”** will open.  
If the window does not appear:

- Verify that you’re in the correct directory (contains `main.py`).  
- Make sure `pygame` was installed successfully (`pip list | grep pygame`).  

---

## 6. Controls & Gameplay

| Key | Action |
|-----|--------|
| **Arrow keys** | Change the snake’s direction (right, left, up, down). |
| **R** | Restart the game after a “Game Over”. |
| **ESC** | Close the game window. |

### Gameplay Rules

1. **Movement** – The snake moves automatically in its current direction every 150 ms (configurable via `move_delay`).  
2. **Food** – When the snake’s head reaches the food cell, the score increases by 1, the snake grows by one segment, and new food appears elsewhere.  
3. **Collisions** –  
   - Hitting the grid boundary → **Game Over**.  
   - Colliding with the snake’s own body → **Game Over**.  
4. **Score** – Displayed in the top‑left corner.  
5. **Game Over** – A flashing message appears. Press **R** to play again.  

---

## 7. Customisation

Feel free to tweak the following settings in `constants.py` to change the game’s feel:

- **Grid size**  
  ```python
  GRID_WIDTH = 20
  GRID_HEIGHT = 20
  ```
  Larger values increase difficulty but require more screen space.

- **Cell size**  
  ```python
  CELL_SIZE = 30
  ```
  Smaller cells make the snake appear slimmer and the grid more packed.

- **Initial snake settings** (in `snake.py` or `game.py`’s `reset()`):  
  ```python
  init_pos=(GRID_WIDTH // 4, GRID_HEIGHT // 2)
  init_length=3
  init_dir=(1, 0)  # Moving right
  ```

- **Speed**  
  In `Game.reset()` adjust `self.move_delay` (in milliseconds). Lower values mean faster movement.

- **Colours** – All RGB tuples in `constants.py` can be replaced to suit your theme.

---

## 8. Troubleshooting

| Symptom | Possible Cause | Fix |
|---------|----------------|-----|
| `ModuleNotFoundError: No module named 'pygame'` | pygame not installed | Run `pip install pygame` or `pip install -r requirements.txt` |
| Window freezes or runs too slowly | Insufficient CPU / low FPS | Reduce `CELL_SIZE` or increase `move_delay` |
| Snake flickers or jumps | Mis‑aligned pixel animation | Ensure your pygame version is 2.0+ (smooth animation depends on it) |
| Game Over immediately | Snake colliding with boundary at start | Check initial position (it should be inside bounds) |

---

## 9. Credits & License

- **Author:** [Your Name] – 2025  
- **License:** MIT License (see `LICENSE` file)  

Feel free to fork, modify, and share. If you discover bugs or want to add features, create a pull request or open an issue.

---

**Enjoy the game!**