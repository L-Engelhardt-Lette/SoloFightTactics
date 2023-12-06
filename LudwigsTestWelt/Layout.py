import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the screen dimensions and grid
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
GRID_SIZE = (5, 8)  # 5 rows by 8 columns for both players combined
TILE_SIZE = (SCREEN_WIDTH // GRID_SIZE[1], SCREEN_HEIGHT // (GRID_SIZE[0] + 2))  # additional 2 rows for shop and info

# Constants for the shop tiles