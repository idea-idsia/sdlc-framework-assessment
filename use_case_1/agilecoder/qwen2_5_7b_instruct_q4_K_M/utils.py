"""
Utility Functions
"""
import random
def generate_random_position(grid_dimensions):
    return (random.randint(0, grid_dimensions[0] - 1), random.randint(0, grid_dimensions[1] - 1))