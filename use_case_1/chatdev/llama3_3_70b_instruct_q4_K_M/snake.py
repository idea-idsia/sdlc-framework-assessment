# Import necessary libraries
import pygame
'''
This file contains the implementation of the Snake class.
It represents a snake in the game, with methods to move and grow.
'''
class Snake:
    def __init__(self, block_size):
        # Initialize the snake's body and head
        self.body = [(200, 200), (220, 200), (240, 200)]
        self.head = self.body[-1]
        self.block_size = block_size
        # Set up the direction
        self.direction = "right"
        self.grown = False
    def move_up(self):
        # Change the snake's direction to up
        if self.direction != "down":
            self.direction = "up"
    def move_down(self):
        # Change the snake's direction to down
        if self.direction != "up":
            self.direction = "down"
    def move_left(self):
        # Change the snake's direction to left
        if self.direction != "right":
            self.direction = "left"
    def move_right(self):
        # Change the snake's direction to right
        if self.direction != "left":
            self.direction = "right"
    def update_head(self):
        # Update the snake's head based on its direction
        if self.direction == "up":
            new_head = (self.head[0], self.head[1] - self.block_size)
        elif self.direction == "down":
            new_head = (self.head[0], self.head[1] + self.block_size)
        elif self.direction == "left":
            new_head = (self.head[0] - self.block_size, self.head[1])
        elif self.direction == "right":
            new_head = (self.head[0] + self.block_size, self.head[1])
        self.body.append(new_head)
        self.head = new_head
        if not self.grown:
            self.body.pop(0)
        else:
            self.grown = False
    def grow(self):
        # Mark the snake as grown
        self.grown = True