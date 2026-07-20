import tkinter as tk

class GameBoard:
    def __init__(self, master):
        self.master = master
        self.grid_dimensions = (20, 20)
        self.cell_size = 30
        self.canvas = tk.Canvas(master, width=self.grid_dimensions[0] * self.cell_size,
                                height=self.grid_dimensions[1] * self.cell_size)
        self.canvas.pack()

    def draw_grid(self, snake_body, food_position):
        self.canvas.delete("all")
        for row in range(self.grid_dimensions[1]):
            for col in range(self.grid_dimensions[0]):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                # Draw grid lines
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black")

        # Draw snake
        for body_part in snake_body:
            x, y = body_part[0] * self.cell_size, body_part[1] * self.cell_size
            self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size,
                                         fill="green", outline="")

        # Draw food
        if food_position:
            x, y = food_position[0] * self.cell_size, food_position[1] * self.cell_size
            self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size,
                                         fill="red", outline="")